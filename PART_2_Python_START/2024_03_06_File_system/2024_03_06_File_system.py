# import zipfile
#
# # for i in zipfile:
# #     print(i)
#
#
#
#
# zipfilename = "./test.zip"
#
# dictionary = './dictionary.txt'
#
# zip_file = zipfile.ZipFile(zipfilename)
#
# PassFile = open(dictionary, 'r')
#
# password = None
# for line in PassFile.readlines():
#     password = line.strip('\n')
#     try:
#         zip_file.extractall(pwd=password.encode())
#         print("-" * 11)
#         print("Result" + password)
#         PassFile.close()
#     except Exception as e:
#         print(password)
#
# PassFile.close()

import os

#приложение шпион
def file_collector(path):
	path = os.path.normpath(path)
	result =  {"dirs":[],"files":[]}
	for path, dirnames, filenames in os.walk(path):
		for dir in dirnames:
			result["dirs"].append(dir)
		for file in filenames:
			result["files"].append(file)
	with open("skiper.txt",'w') as file:
		file.write("\n{:-<50}\n".format("Directories"))
		for dir in result["dirs"]:
			file.write(f"\t{dir}\t")
		file.write("\n{:-<50}\n".format("Files"))
		for files in result["files"]:
			file.write(f"\t{files}\n")

path = 'Вставить путь'
file_collector(path)