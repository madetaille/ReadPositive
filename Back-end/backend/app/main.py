from flask import Flask
from flask import request

from API_interface import *
from flask_cors import CORS

import json

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

PROJECT_EXTENSION = ''
api_interface = API_interface()

# Check that arguments are present
def isArgIn(args, struct):
	log_exception_arg = {}

	for arg in args:
		if arg not in struct:
			log_exception_arg['status'] = 'Failed'
			log_exception_arg['reason'] = "'" + arg + "' is required as an argument of this API call."
			return log_exception_arg

	log_exception_arg['status'] = 'Success'
	return log_exception_arg

@app.route('/writeMessage', methods=['POST'])
def write_message():
	"""Write a message to a feed"""

	# get parameters
	req_data = request.get_json()

	# test required arguments
	log_test_args = isArgIn(['link', 'summary', 'publisher', 'company'], req_data)
	if log_test_args['status'] == 'Failed':
		return json.dumps(log_test_args)

	link = req_data['link']
	summary = req_data['summary']
	publisher = req_data['publisher']
	company = req_data['company']

	res = json.dumps(api_interface.write_message(link, summary, publisher, company))
	return res, 200

@app.route('/getFeed', methods=['POST'])
def read_feed():
	"""Read feed"""

	# get parameters
	req_data = request.get_json()

	# test required arguments
	log_test_args = isArgIn(['positivity_threshold'], req_data)
	if log_test_args['status'] == 'Failed':
		return json.dumps(log_test_args)

	positivity_threshold = req_data['positivity_threshold']

	res = json.dumps(api_interface.read_feed(positivity_threshold))
	return res, 200


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)