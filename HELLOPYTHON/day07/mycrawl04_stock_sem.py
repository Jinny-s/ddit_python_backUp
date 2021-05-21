import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
import time

def insertStock(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    curs = conn.cursor() # java에서 statement
    sql = "insert into stock(s_code,s_name,s_price,crawl_date) values (%s,%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)

    conn.commit()
    conn.close()
    return cnt


for i in range(10):

    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(response.content.decode('euc-kr', 'replace'), 'html.parser')
        
        tuts = []
    
        now = datetime.now()
        crawl_date = now.strftime("%Y%m%d.%H%M")
        
        items = soup.select(".st2")
        for i, item in enumerate(items):
            s_code = item.a['title']
            s_name = item.text
            s_price = item.parent.select('td')[1].text.replace(',','')
            
            tuts.append((s_code,s_name,s_price,crawl_date))
        
        cnt = insertStock(tuts)
        print("cnt :",cnt) 
        
    else : 
        print(response.status_code)
        
    time.sleep(60)
    