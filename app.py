from flask import Flask
from flask import jsonify
import corona
app = Flask(__name__)
@app.route('/total', methods=['GET'])
def tot():
    return jsonify(corona.f)
@app.route('/', methods=['GET'])
def index():
    return jsonify(corona.d)
@app.route('/yesterday', methods=['GET'])
def yesterday():
    return jsonify(corona.y)
@app.route('/source', methods=['GET'])
def source():
    return jsonify(corona.s)
@app.route('/source_yesterday', methods=['GET'])
def source_yesterday():
    return jsonify(corona.sy)
if __name__=="__main__":
    app.run(threaded=True, port=5000)
