int T0 = A0;
int T1 = A1;
int T2 = A2;

char A01 = 65;
char A02 = 66;
char A03 = 67;

void setup() {
  Serial.begin(9600);
  pinMode(T0, INPUT);
  pinMode(T1, INPUT);
  pinMode(T2, INPUT);
}

void loop() {
  int se0, se1, se2;

  se0 = digitalRead(T0); //0,1
  se1 = digitalRead(T1); //0,1
  se2 = digitalRead(T2); 
  
  if (se0 != LOW) {
    // 감지됨
    Serial.print(A01);
    Serial.println(se0);
  }else if(se0 == LOW){
    Serial.print(A01);
    Serial.println(se0);
  }

  if (se1 != LOW) {
    // 감지됨
    Serial.print(A02);
    Serial.println(se1);
  }else if(se1 == LOW){
    Serial.print(A02);
    Serial.println(se1);
  }

  if (se2 != LOW) {
    Serial.print(A03);
    Serial.println(se2); 
  }else if(se2 == LOW){
    Serial.print(A03);
    Serial.println(se2);
  }
  
  delay(1000);
}
