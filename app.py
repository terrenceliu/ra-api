from flask import Flask
from flask import Flask, request, render_template, jsonify, abort
from model import session, Catalog
import model

app = Flask(__name__)

"""
	Routing
"""
@app.route('/api/query_by_hid/<hid>', methods=['GET', 'POST'])
def query(hid):
	if request.method == 'GET':
		res = model.query_by_hid(hid)
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