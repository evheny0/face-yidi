import sys
from keras import models
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

model = models.load_model('model.h5')

def testImage(imagePath):
    image = load_img(imagePath)
    imageArray = img_to_array(image)
    predictions = model.predict(imageArray)
    return predictions

if __name__ == '__main__':
    test()


