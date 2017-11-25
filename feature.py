from PIL import Image, ImageDraw
import numpy as np
import face_recognition
import sys
import os
from pathlib import Path


def initFolder(name):
  if not os.path.exists(name):
    os.makedirs(name)
  return name;

def transform_name(filename):
  return "transformed/" + filename + ".png"

def make_square(im, min_size=300):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def crop_image(filename):
  image=Image.open(transform_name(filename))
  image.load()

  image_data = np.asarray(image)
  image_data_bw = image_data.max(axis=2)
  non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
  non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
  if (not non_empty_rows) or (not non_empty_columns):
    return
  cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

  image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

  new_image = Image.fromarray(image_data_new)
  new_image.save(transform_name(filename))

def scale_image(filename):
  basewidth = 300
  img = Image.open(transform_name(filename))
  wpercent = (basewidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
  img.save(transform_name(filename)) 

def face_features(filename):
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(filename)

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) == 0:
      print("No face detected")
      return

    for face_landmarks in face_landmarks_list:
        # pil_image = Image.fromarray(image)
        pil_image = Image.new('RGBA', (len(image), len(image[0])))
        d = ImageDraw.Draw(pil_image, 'RGBA')

        # d.polygon(face_landmarks['left_eyebrow'], fill=(0, 0, 0, 256))
        # d.polygon(face_landmarks['right_eyebrow'], fill=(0, 0, 0, 256))
        d.line(face_landmarks['left_eyebrow'], fill=(0, 0, 0, 256), width=5)
        d.line(face_landmarks['right_eyebrow'], fill=(0, 0, 0, 256), width=5)

        d.polygon(face_landmarks['top_lip'], fill=(0, 0, 0, 256))
        d.polygon(face_landmarks['bottom_lip'], fill=(0, 0, 0, 256))
        d.line(face_landmarks['top_lip'], fill=(0, 0, 0, 256), width=5)
        d.line(face_landmarks['bottom_lip'], fill=(0, 0, 0, 256), width=5)

        d.line(face_landmarks['nose_bridge'], fill=(0, 0, 0, 256), width=5)
        d.line(face_landmarks['nose_tip'], fill=(0, 0, 0, 256), width=5)
        d.line(face_landmarks['chin'], fill=(0, 0, 0, 256), width=5)

        d.polygon(face_landmarks['left_eye'], fill=(0, 0, 0, 256))
        d.polygon(face_landmarks['right_eye'], fill=(0, 0, 0, 256))

        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 256), width=5)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 256), width=5)

        pil_image.save(transform_name(filename))




    ###### CROP IMAGE
    crop_image(filename)
    ######

    ###### SCALE IMAGE
    scale_image(filename)
    ######

    image=Image.open(transform_name(filename))
    make_square(image).save(transform_name(filename))



rootdir = Path(sys.argv[1])
file_list = [f for f in rootdir.glob('**/*') if f.is_file()]


for filepath in file_list:
  if filepath.suffix != '.jpeg' and filepath.suffix != '.jpg' and filepath.suffix != '.png':
      continue
  initFolder("transformed/" + str(filepath.parents[0]))
  face_features(str(filepath))

