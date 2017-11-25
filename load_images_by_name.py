from urllib import request
import json
import os
import _thread
import sys

IMAGES_PATH = "./images"

API_URL = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyCl1UzajNrpvya3dCGVvECTtMHiCKiGOIw"
API_CX_KEY = "011644667007826062821:9i8kosv4i2o"
API_SEARCH_TYPE = "image"
API_IMAGE_TYPE = "face"
API_BATCH_SIZE = 10
API_IMAGE_SIZE = "medium"
BASIC_SEARCH_URL = f"{API_URL}?key={API_KEY}&cx={API_CX_KEY}&searchType={API_SEARCH_TYPE}&imageType={API_IMAGE_TYPE}&num={API_BATCH_SIZE}&imageSize={API_IMAGE_SIZE}"

TOTAL_IMAGES = 100

NAMES = sys.argv[1].split(" ")

def loadImages(name):
	nameFolderPath = initFolder(name)
	offset = 1
	threads = []
	while offset < TOTAL_IMAGES:
		loadImagesBatch(name, nameFolderPath, offset)
		offset = offset + API_BATCH_SIZE

def loadImagesBatch(name, folder, offset):
	encodedName = request.pathname2url(name)
	url = f"{BASIC_SEARCH_URL}&q={encodedName}&start={offset}"
	response = json.loads(request.urlopen(url).read())
	for index, item in enumerate(response["items"]):
		filename = f"{folder}/{index + offset}.jpg"
		print(filename)
		try:
			request.urlretrieve(item['link'], filename)
		except:
			print(f"{filename} loading failed!")

def initFolder(name):
	nameFolderPath = f"{IMAGES_PATH}/{name}" 
	if not os.path.exists(nameFolderPath):
		os.makedirs(nameFolderPath)
	return nameFolderPath;

for name in NAMES:
	print(f"Images loading started for name {name}")	
	loadImages(name)
	print(f"Images loading finished for name {name}")