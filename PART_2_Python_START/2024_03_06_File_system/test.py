#архивация файлов

import zipfile
#
zipfilename = "test.zip"

dictionary = 'dictionary.txt'
#создание архива
zip_file = zipfile.ZipFile(zipfilename)
#открытие списка паролей
f = open(dictionary, 'r')
password = None
for line in f.readlines():
	password = line.strip('\n')
	try:
		#extractall - разархивирование архива
		zip_file.extractall(pwd=password.encode())
		print("-"*11)
		print("Result" + password)
		f.close()
	except:
		print(password)
f.close()
#
# #path - пути
# import os
# # нормализация пути
# path = os.path.normpath("C:\Users\Little\Desktop\Петров Михаил")
# # walk - относительный путь, пройти по указанному пути
# for path, dirnames, filenames in os.walk(path):
# 	print(f"path - {path}")
# 	print(f"dirnames - {dirnames}")