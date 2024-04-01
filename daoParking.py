import cx_Oracle

class DaoParking:
    def __init__(self):
        self.conn = cx_Oracle.connect('TEAM1_202308F/java@112.220.114.130:1521/xe')
        self.cur = self.conn.cursor()
        
    def updateParKing(self, area, se):
        sql = f"""
                UPDATE TB_PARKING_AREA
                SET
                    PAK_SE = '{se}'
                WHERE
                    PAK_AREA = '{area}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        
        rowcnt = self.cur.rowcount
        print("rowcnt:", rowcnt)
        
        return rowcnt
    
    def selectParking(self, area):
        sql = f"""
                SELECT 
                    PAK_AREA, PAK_SE
                FROM
                    TB_PARKING_AREA
                WHERE
                    PAK_AREA = '{area}'
        """
        self.cur.execute(sql)
        recom = self.cur.fetchall()
        myjson = []
        for r in recom:
            myjson.append({'area':r[0], 'se':r[1]})
        return myjson
    
    
    def __del__(self):
        self.cur.close()
        self.conn.close()