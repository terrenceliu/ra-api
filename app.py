from flask import Flask, request, render_template, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
# 'postgres://zakcbnbwjltjov:c2a731b393554475ddb34e2ae1512c5017fd98420599dad51d762846b4ef53ed@ec2-54-221-212-15.compute-1.amazonaws.com:5432/d81coggjuv9qid'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

from model import query_by_hid

"""
	Routing
"""
@app.route('/api/query_by_hid/<hid>', methods=['GET', 'POST'])
def query(hid):
	if request.method == 'GET':
		res = query_by_hid(hid)
		if res == None:
			msg = '[Err] HID Not Found. HID = ' + hid + ', URL = ' + request.url
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