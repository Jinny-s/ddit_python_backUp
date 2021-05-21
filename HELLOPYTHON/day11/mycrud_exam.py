from flask import Flask, render_template, jsonify, request
from day11.mydao_exam import DaoExam

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/exam')
def exam():
    de = DaoExam()
    examList = de.myselect()
    return render_template('exam.html', examList=examList)

@app.route('/add.ajax', methods=['POST'])
def ajax_add():
    e = request.get_json()
    de = DaoExam()
    cnt = de.myinsert(e['e_id'], e['kor'], e['eng'], e['math'])
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/upd.ajax', methods=['POST'])
def ajax_upd():
    e = request.get_json()
    de = DaoExam()
    cnt = de.myupdate(e['kor'], e['eng'], e['math'], e['e_id'])
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg)

@app.route('/del.ajax', methods=['POST'])
def ajax_del():
    p = request.get_json()
    de = DaoExam()
    cnt = de.mydelete(p['e_id'])
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg)

if __name__ == '__main__':
    app.run(debug=True)