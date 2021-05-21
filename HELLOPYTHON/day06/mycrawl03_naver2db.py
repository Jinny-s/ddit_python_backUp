import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertDdeok(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    curs = conn.cursor() # java에서 statement
    sql = "insert into ddeok(title,link,description,bloggername,bloggerlink,postdate) values (%s,%s,%s,%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)

    conn.commit()
    conn.close()
    return cnt


client_id = "zrbQWjrUE7xe6GeKL0vs"
client_secret = "2sYWnEzERV"
encText = urllib.parse.quote("로제떡볶이")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'xml')
    
    items = soup.select("item")
    tuts = []
    for i, item in enumerate(items):
        title       = item.title.text
        link        = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate    = item.postdate.text
        
        tuts.append((title,link,description,bloggername,bloggerlink,postdate))
        
    cnt = insertDdeok(tuts)
    print("cnt :",cnt)
        
else : 
    print("Error Code:" + rescode)
    
    


