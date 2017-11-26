from flask import Flask
from flask import request
import uuid
import base64
import test_single

app = Flask("hashleta")

@app.route("/image", methods=['POST'])
def processImage():
	print('request received')
	try:
		image = request.files['image']
		filePath = f'./uploaded/{str(uuid.uuid4())}.jpg'
		image.save(filePath)
		predictions = test_single.testImage(filePath)
		return predictions
	except:
		e = sys.exc_info()[0]
		return e


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)