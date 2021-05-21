import urllib.request

from bs4 import BeautifulSoup


client_id = "zrbQWjrUE7xe6GeKL0vs"
client_secret = "2sYWnEzERV"
encText = urllib.parse.quote("로제떡볶이")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.select("item")
    for i, item in enumerate(items):
        print(item.title.text)
        print(item.link.text)
        print(item.description.text)
        print()
        print()
        
else : 
    print("Error Code:" + rescode)
    
