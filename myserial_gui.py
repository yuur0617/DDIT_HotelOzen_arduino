import sys
import serial
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from daoParking import DaoParking

SERIAL_PORT = 'COM4'
BAUD_RATE = 9600

class CarSensorApp:
    def __init__(self):

        self.dp = DaoParking()
        self.area = '';
        self.se = 0;
        
        try:
            self.serial_port = serial.Serial(SERIAL_PORT, BAUD_RATE)
        except serial.SerialException as e:
            print("시리얼 포트를 열 수 없습니다:", e)
            sys.exit(1)


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_car_image)
        self.timer.start(10)  # 1초마다 업데이트

    def update_car_image(self):

        sensor_value = self.serial_port.readline().strip().decode() 
        
       
        values = sensor_value.split() # 주어진 문자열을 공백을 기준으로 분리하여 리스트로 만듭니다.
        
        self.area = values[0][0]  # A, B, C 중 첫 글자
        self.se = values[0][1:]  # 첫 번째 글자를 제외한 나머지는 숫자로 변환하여 할당

        result = self.dp.selectParking(self.area)
        print(result[0]['area'], result[0]['se'])
        print(self.area, self.se)
        
        if result[0]['area'] == self.area:
            if result[0]['se'] != self.se:
                self.dp.updateParKing(self.area, self.se)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    car_sensor_app = CarSensorApp()
    sys.exit(app.exec_())
