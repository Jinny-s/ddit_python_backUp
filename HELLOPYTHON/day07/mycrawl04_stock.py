import requests
from bs4 import BeautifulSoup
import pymysql

def insertStock(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    curs = conn.cursor() # java에서 statement
    sql = "insert into stock(s_code,s_name,s_price,crawl_date) values (%s,%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)

    conn.commit()
    conn.close()
    return cnt


url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(response.content.decode('euc-kr', 'replace'), 'html.parser')
    
    names = soup.select('.st2')
    time = soup.select_one('.t_11_black').get_text()
    s_time = time.replace('.', '').replace(':','').replace(' ','.')
    crawl_date = str(20) + s_time
    
    tuts = []
    
    for i, name in enumerate(names):
        s_code = name.next_element.attrs['title']
        s_name = name.get_text()
        price = name.find_next_sibling('td').get_text()
        s_price = price.replace(',','')
        
        tuts.append((s_code,s_name,s_price,crawl_date))
    
    cnt = insertStock(tuts)
    print("cnt :",cnt)    

else : 
    print(response.status_code)
    