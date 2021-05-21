from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def home():
    
    a = request.args.get('a', "good")
    
    return 'Hello, {}!'.format(a)

if __name__ == '__main__':
    app.run(debug=True)