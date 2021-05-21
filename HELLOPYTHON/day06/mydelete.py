import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')

curs = conn.cursor() # java에서 statement

sql = "delete from hello where col01 = 6"
cnt = curs.execute(sql)
print("cnt",cnt)
conn.commit()
 
conn.close()
