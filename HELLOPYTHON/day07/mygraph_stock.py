import numpy as np
import matplotlib.pyplot as plt
import pymysql
import random

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

def getPrices(s_code):
    ret = []
    sql = "select s_price from stock where s_code = '{}' order by crawl_date".format(s_code)
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    return ret

def getCodes():
    codes = []
    sql = "select s_code from stock group by s_name"
    curs.execute(sql)
    rows = curs.fetchall()

    for row in rows:
        codes.append(row[0])
    return codes

fig = plt.figure()
ax = plt.axes(projection='3d')

for i, code in enumerate(getCodes()):
    a = np.array(getPrices(code))
    z = a / a[0]
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    ax.plot3D(x+i, y, z)

conn.close()

ax.set_title('Stock Flow')
plt.show()