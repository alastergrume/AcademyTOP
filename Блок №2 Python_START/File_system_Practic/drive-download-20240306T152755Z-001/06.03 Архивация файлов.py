# Архивация файлов
import zipfile
zipfilename='my arhiv.zip'
dictionary='dictionary.txt'
#Создание архива
zip_file=zipfile.ZipFile(zipfilename)
# Открытие списка паролей
f=open(dictionary,'r')
password=None
for line in f.readlines():
    password=line.strip('\n')
    try:
        #extractall - разорхивирование архива
        zip_file.extractall(pwd=password.encode())
        print("-"*11)
        print('Rezult: '+password)
        f.close()
        break
    except:
        print(password)
f.close()

# path-пути
import os  # нормализация пути
# path=os.path.normpath ('C:\\Users\\Little\\PycharmProjects\\pythonProject17')
# for path,dirnames,filenames in os.walk(path):
#     print(f'path-{path}')
#     print(f'dirnames-{dirnames}')
#     print(f'filenames-{filenames}')
# методы для работы с файлами
path=os.path.normpath ('C:\\Users\\Little\\PycharmProjects\\pythonProject17')
print(os.path.isabs(path))# проверка абсолютного пути
print(os.path.isfile(path))# проверка пути к файлу
print(os.path.isdir(path))# проверка  пути к папке
print(os.path.islink(path))# проверка пути к ссылке

# создание и удаление папок
path='new_path'
# os.mkdir(path) # создание папки по пути
# os.rmdir(path) # удаление
# переименовать
os.rename(path,'file_2')
os.renames() # делает тоже самое, но удаляет
# директории если они становятся пустыми
os.replace() # делает тоже самое но перезаписывает существующие файлы
os.path.getctime("file.txt") # дата создания
os.path.getmtime("file.txt") # дата правки

#приложение шпион
 def file_collector(path):
     path=os.path.normpath(path)
     result={'dirs':[],'files':[]}
     for path,dirnames,filenames in os.walk(path):
         for dir in dirnames:
             result['dirs'].append(dir)
         for file in filenames:
             result['files'].append(file)
     with open('skiper.txt','w') as file:
         file.write('\n{:-<50}\n').format('Directories'))
         for dir in result['dirs']:
             file.write(f'\t{dir}\t')
         file.write('\n{:-<50}\n').format('Files'))
         for files in result['files']:
             file.write(f'\t{files}\n')
path="вставить путь"
file_collector(path)