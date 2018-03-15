from flask import Flask, request, render_template, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgresql://localhost/test3'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

from model import query_by_hid, query_by_space

"""
	Routing
"""
@app.route('/', methods=['GET'])
def index_page():
	return render_template('index.html')

@app.route('/api/query/hid/<hid>', methods=['GET'])
def query_hid(hid):
	if request.method == 'GET':
		res = query_by_hid(hid)
		if res is None:
			msg = '[Err] 404 Not Found. URL = ' + request.url
			return not_found(msg)
		else:
			return jsonify({"result": res})

@app.route('/api/query', methods=['POST'])
def query():
	req_data = request.get_json()
	hid = None
	res_hid = False
	res_content = False
	res_has_space = False
	
	# Get searching hid
	if 'hid' in req_data:
		hid = req_data["hid"]
		assert isinstance(hid, basestring)
	else:
		msg = '[Err] `hid` field is not sent in POST request body'
		return not_found(msg)
	
	data = query_by_hid(hid)
	
	if data is None:
		msg = '[Err] 404 Not Found. URL = ' + request.url
		return not_found(msg)
	
	if 'res_hid' in req_data:
		res_hid = req_data["res_hid"]
		assert isinstance(res_hid, bool)
	
	if 'res_content' in req_data:
		res_content = req_data["res_content"]
		assert isinstance(res_content, bool)
	
	if 'res_has_space' in req_data:
		res_has_space = req_data["res_has_space"]
		assert isinstance(res_has_space, bool)
	
	if not res_hid:
		del data['hid']
	
	if not res_content:
		del data['content']
	
	if not res_has_space:
		del data['has_space']
	
	return jsonify({"result": data})
	
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