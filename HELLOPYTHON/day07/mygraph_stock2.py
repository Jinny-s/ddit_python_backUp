from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
import random

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()
sql = "select s_name, s_price from stock order by s_code, crawl_date"

curs.execute(sql)
rows = curs.fetchall()
new = []
names = []
for i, row in enumerate(rows):
    new.append(row[1])
conn.close()

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(0, len(new), 10):
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    
    a = np.array(new[i:i+10])
    
    z = (a / a[0])
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    ax.plot3D(x+i, y, z, c = color)

ax.set_title('Stock Flow')
plt.show()