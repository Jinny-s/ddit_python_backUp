from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

def getNames():
    ret = []
    sql = "select s_name from stock group by s_code"
    
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    return np.array(ret)
 
def getPrices(s_name):
    ret = []
    sql = "select s_price from stock where s_name = '{}' order by crawl_date".format(s_name)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    return np.array(ret)

arr_name = getNames()
arrz = []

for i in range(len(arr_name)):
    arrz.append(getPrices(arr_name[i]))

arr_per_z = []
for i in range(len(arr_name)):
    imsi = (arrz[i]/arrz[i][0]) * 100
    arr_per_z.append(imsi)

fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

for i in range(len(arr_name)):
    ax.plot3D(x+i, y, arr_per_z[i])

conn.close()
 
ax.set_title('Stock Flow')
plt.show()