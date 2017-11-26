from flask import Flask
from flask import request
from flask import render_template
import uuid
import base64
import test_single
import sys
from flask import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/image", methods=['POST'])
def processImage():
	print('request received')
	try:
		image = request.form['image']
		# print(image)
		imageData = base64.b64decode(image.split(',')[1])
		filePath = f'./uploaded/{str(uuid.uuid4())}.png'
		with open(filePath, 'wb') as fh:
			fh.write(imageData)
		predictions = test_single.testImage(filePath)
		if not predictions:
			return "Face not found"
		print(predictions)
		# response = app.response_class(
	 #        response=json.dumps(data),
	 #        status=200,
	 #        mimetype='application/json'
	 #    )
		return str(predictions)
	except:
		e = sys.exc_info()[0]
		print(e)
	return "Error"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
