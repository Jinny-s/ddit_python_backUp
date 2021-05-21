from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
 
def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "select s_price from stock where s_name = '{}' order by crawl_date".format(s_name)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
        
    conn.close()
    return ret

fig = plt.figure()
ax = plt.axes(projection='3d')

s0 = np.array(getPrices('삼성전자'))
s1 = np.array(getPrices('삼성전자우'))

z0 = (s0 / s0[0]) * 100
z1 = (s1 / s1[0]) * 100
x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

ax.plot3D(x, y, z0,'maroon')
ax.plot3D(x+0.5, y, z1, 'red')
ax.set_title('Stock Flow')
plt.show()