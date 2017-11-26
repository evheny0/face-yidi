from flask import Flask
from flask import request
import uuid
import test_single

app = Flask("hashleta")

@app.route("/image", methods=['POST'])
def processImage():
	image = request.files['image']
	filePath = f'./uploaded/{str(uuid.uuid4())}.jpg'
	image.save(filePath)
	predictions = test_single.testImage(filePath)
	return predictions

if __name__ == "__main__":
	app.run(port=8080)