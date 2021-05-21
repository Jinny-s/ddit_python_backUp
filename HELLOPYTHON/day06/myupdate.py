import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')

curs = conn.cursor() # java에서 statement

sql = "update hello set col02='샤브샤브', col03='영덕대게' where col01 = 1"
cnt = curs.execute(sql)
print("cnt",cnt)
conn.commit()
 
conn.close()
