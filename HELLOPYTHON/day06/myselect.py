import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "select col01,col02,col03 from hello"
curs.execute(sql)

rows = curs.fetchall()
for row in rows:
    print(row)

conn.close()





# try:
#     with conn.cursor() as curs:
#         sql = "SELECT * FROM hello"
#         curs.execute(sql)
#         rs = curs.fetchall()
#
#         for row in rs:
#             for data in row:
#                 print(data, end=' ')
#             print()
# finally:
#     conn.close()
