from flask import Flask, jsonify, make_response, request
import cv2
app = Flask(__name__)


@app.route("/imageScoring/score", methods=["POST"])
def imagescoring_score():
	# input
	file = request.files['file']
	print('Posted file: %s' % (file))
	# img = cv2.imdecode(file.read())
	# print(img)
	# process something...
	resp_body = {
		'gray': 24,
		'faceCoordinates': [[]]
	}
	res = make_response(jsonify(resp_body), 200)
	return res
