from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbOreum

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# 리뷰 작성하기
@app.route('/review', methods=['POST'])
def make_review():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }

    db.review.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '작성완료!!'})

# POST한 리뷰 보여주기
@app.route('/review', methods=['GET'])
def view_reviews():
    reviews = list(db.review.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})

# 서버
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)