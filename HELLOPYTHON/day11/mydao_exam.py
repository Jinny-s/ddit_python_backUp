import pymysql
 
class DaoExam:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    def myselect(self):
        ret = []
        curs = self.conn.cursor()
        sql = "select e_id, kor, eng, math from exam"
        curs.execute(sql)
        
        rows = curs.fetchall()
        for row in rows:
            ret.append({'e_id':row[0],'kor':row[1],'eng':row[2],'math':row[3]})
        
        return ret
    
    def myinsert(self, e_id, kor, eng, math):
        curs = self.conn.cursor()
        sql = "insert into exam (e_id, kor, eng, math) values ('{}',{},{},{})".format(e_id, kor, eng, math)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def myupdate(self, kor, eng, math, e_id):
        curs = self.conn.cursor()
        sql = "update exam set kor={}, eng={}, math={} where e_id='{}'".format(kor, eng, math, e_id)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self, e_id):
        curs = self.conn.cursor()
        sql = "delete from exam where e_id='{}'".format(e_id)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoExam()
    list = de.myselect()
    print(list)
    
    # cnt = de.myinsert('ddit003', 45,20,60)
    # cnt = de.myupdate(100,100,100,'ddit003')
    # cnt = de.mydelete('ddit003')
    # print(cnt)