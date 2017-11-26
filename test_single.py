import sys
import keras
from keras import models
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np


model = models.load_model('model.h5')

def inverse_dict(d):
    return {v: k for k, v in d.items()}

data_generator = ImageDataGenerator(rescale=1. / 255)
classes = inverse_dict(data_generator.flow_from_directory(
        directory='./tr3/images2',
        target_size=(150, 150),
        batch_size=1,
        class_mode='categorical'
    ).class_indices)



SIZE = 150

def scale_image(filename):
  basewidth = SIZE
  img = Image.open(filename)
  wpercent = (basewidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
  img.save(filename)

def find_faces(filename):
  image = face_recognition.load_image_file(filename)
  face_locations = face_recognition.face_locations(image)

  if len(face_locations) < 1:
    return False

  top, right, bottom, left = face_locations[0]
  face_image = image[top:bottom, left:right]
  pil_image = Image.fromarray(face_image)
  pil_image.save(filename)
  scale_image(filename)
  img = cv2.imread(filename, 0)
  clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
  cl1 = clahe.apply(img)
  cv2.imwrite(filename, cl1)

  return True

def testImage(imagePath):
	print("Prepare image")
	if not find_faces(imagePath):
		return None

	print("Prepare done")
	Image.open(imagePath).resize((150, 150)).save(imagePath, 'PNG')
	img = Image.open(imagePath).convert('RGB')
	imageArray = np.array([np.array(img)]) * (1.0 / 255.0)
	print("Predict...")
	predictions = model.predict(imageArray)[0]
	result = {}
	for i in range(len(predictions)):
		result[classes[i]] = predictions[i]
	return result

if __name__ == '__main__':
	predictions = testImage('./uploaded/00ad57d9-470e-46a1-b4a1-79ac8f59a12e.png')
	# classses = keras.np_utils.probas_to_classes(predictions)
	print(predictions)


