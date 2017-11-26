import test_single
import sys
# from flask import json
import json

filename = sys.argv[1]

predictions = test_single.testImage(filename)

# predictions = [{'name': filename}]

print(json.dumps(predictions))
