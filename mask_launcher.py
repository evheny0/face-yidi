import subprocess
from pathlib import Path
import sys
import os


NAMES = ["Кирилл","Александр","Никита","Виталий","Павел","Дмитрий","Владимир","Станислав","Валентин","Алексей","Андрей","Олег","Руслан","Евгений","Анатолий","Вячеслав","Матвей","Илья","Максим","Виктор","Михаил","Геннадий","Владислав","Егор","Сергей","Антон","Артем","Ростислав","Юрий","Денис","Глеб","Вадим","Игорь","Георгий","Ян","Ярослав","Герман","Валерий","Борис","Иван","Давид","Даниил","Ирина","Алина","Антонина","Евгения","Наталья","Елена","Анна","Екатерина","Валентина","Ольга","Елизавета","Алена","Марина","Надежда","Ксения","Татьяна"]
BATCH_SIZE = 10

def initFolder(name):
  if not os.path.exists(name):
    os.makedirs(name)
  return name;


rootdir = Path(sys.argv[1])
file_list = [f for f in rootdir.glob('**/*') if f.is_file()]

for filepath in file_list:
  if filepath.suffix != '.jpeg' and filepath.suffix != '.jpg' and filepath.suffix != '.png':
      continue
  initFolder(sys.argv[2] + str(filepath.parents[0]))
  subprocess.Popen(["python", "feature.py", str(filepath)])

