import os
import pandas
import pandas as pd
from pathlib import Path


path_list = []
directory = Path("C:/Users/User/PycharmProjects/TOP_Academy/AcademyTOP/HomeWorks/")
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)
        path_list.append(filename.path)

print(path_list)


file = 'path_list'
writer
file.to_excel()
