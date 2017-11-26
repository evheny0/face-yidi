from flask import Flask
from flask import request
import uuid
import base64
import test_single
import sys

app = Flask("hackleta")

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
		print(predictions)
		return predictions
	except:
		e = sys.exc_info()[0]
		print(e)
	return "Error"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)