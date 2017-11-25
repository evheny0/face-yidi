import subprocess

NAMES = ["Кирилл","Александр","Никита","Виталий","Павел","Дмитрий","Владимир","Станислав","Валентин","Алексей","Андрей","Олег","Руслан","Евгений","Анатолий","Вячеслав","Матвей","Илья","Максим","Виктор","Михаил","Геннадий","Владислав","Егор","Сергей","Антон","Артем","Ростислав","Юрий","Денис","Глеб","Вадим","Игорь","Георгий","Ян","Ярослав","Герман","Валерий","Борис","Иван","Давид","Даниил","Ирина","Алина","Антонина","Евгения","Наталья","Елена","Анна","Екатерина","Валентина","Ольга","Елизавета","Алена","Марина","Надежда","Ксения","Татьяна"]
BATCH_SIZE = 10

for i in range(len(NAMES)//BATCH_SIZE + 1):
	names = NAMES[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
	namesAsString = " ".join(names)
	subprocess.Popen(["python", "load_images_by_name.py", namesAsString])