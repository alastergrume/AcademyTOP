#��������� ������

import zipfile
#
zipfilename = "test.zip"

dictionary = 'dictionary.txt'
#�������� ������
zip_file = zipfile.ZipFile(zipfilename)
#�������� ������ �������
f = open(dictionary, 'r')
password = None
for line in f.readlines():
	password = line.strip('\n')
	try:
		#extractall - ���������������� ������
		zip_file.extractall(pwd=password.encode())
		print("-"*11)
		print("Result" + password)
		f.close()
	except:
		print(password)
f.close()
#
# #path - ����
# import os
# # ������������ ����
# path = os.path.normpath("C:\Users\Little\Desktop\������ ������")
# # walk - ������������� ����, ������ �� ���������� ����
# for path, dirnames, filenames in os.walk(path):
# 	print(f"path - {path}")
# 	print(f"dirnames - {dirnames}")