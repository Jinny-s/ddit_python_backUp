import pymysql

def insertDdeok(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    curs = conn.cursor() # java에서 statement
    sql = "insert into hello(col01,col02,col03) values (%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)

    conn.commit()
    conn.close()
    return cnt

if __name__ == '__main__':
    tuts = []
    
    tuts.append((4,'4','4'))
    tuts.append((5,'5','5'))
    tuts.append((6,'6','6'))
    cnt = insertDdeok(tuts)
    print("* cnt :",cnt)