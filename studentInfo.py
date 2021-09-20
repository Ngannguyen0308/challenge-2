import os, sys
import re
import pandas as pd

path = "D:\IntroCSE\Challenge_2\Data"
dirs = os.listdir(path)

list1 = []
for i in dirs:
    name = os.path.splitext(i)
    list1.append(name[0])

list = {'StudentID' : [], 'Surname': [], 'Firstname' : [] , 'Code' : []}


for item in list1:
    parts = item.split('_')

    parts[1] = re.sub(r"(\w)([A-Z])", r"\1 \2", parts[1])
    *sur, first = parts[1].split()
    sur = ' '.join(sur)

    list['StudentID'].append(parts[0])
    list['Surname'].append(sur)
    list['Firstname'].append(first)
    list['Code'].append(parts[2])
    

df = pd.DataFrame(list, columns= ['StudentID' ,'Surname', 'Firstname', 'Code'])
df.to_csv('csv/student.csv')
print(df)
