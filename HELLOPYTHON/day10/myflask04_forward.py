from flask import Flask
from flask import render_template

app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
    title = "리스트보기"
    mylist = ['최윤성', '김이현', '공슬기', '김민지']
    objlist = []
    objlist.append({'e_id':'1','e_name':'배고파','birth':'1992년'})
    objlist.append({'e_id':'2','e_name':'꿀꿀이','birth':'1993년'})
    
    return render_template('index.html', title=title, list=mylist, objlist=objlist)

if __name__ == '__main__':
    app.run(debug=True)