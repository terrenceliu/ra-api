from flask import Flask, request, render_template, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgresql://localhost/test3'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

from model import query_by_hid

"""
	Routing
"""
@app.route('/', methods=['GET'])
def index_page():
	return render_template('index.html')

@app.route('/api/query/hid/<hid>', methods=['GET'])
def query(hid):
	print request.get_json(silent=True)
	print request.args
	if request.method == 'GET':
		res = query_by_hid(hid)
		if res == None:
			msg = '[Err] 404 Not Found. URL = ' + request.url
			return not_found(msg)
		else:
			return jsonify({"result": res})

@app.errorhandler(404)
def not_found(message):
	message = {
		'status': 404,
		'message': message,
	}
	resp = jsonify(message)
	resp.status_code = 404
	return resp
	
"""
	Main
"""
if __name__ == '__main__':
	app.run()