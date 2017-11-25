import subprocess
from pathlib import Path
import sys
import os


BATCH_SIZE = 1000

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def initFolder(name):
  if not os.path.exists(name):
    os.makedirs(name)
  return name;


rootdir = Path(sys.argv[1])
file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
file_list = [f for f in file_list if (f.suffix == '.jpeg' or f.suffix == '.jpg' or f.suffix == '.png')]

for filepath in file_list:
  initFolder(sys.argv[2] + str(filepath.parents[0]))

file_list = [str(f) for f in file_list]

for filepath in chunks(file_list, BATCH_SIZE):
  subprocess.Popen(["python", "feature.py", " ".join(filepath)])
