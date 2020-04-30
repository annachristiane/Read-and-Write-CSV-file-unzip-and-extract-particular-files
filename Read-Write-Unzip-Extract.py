# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:11:24 2020

@author: Anna Christiane
"""

import os
from zipfile import ZipFile
import csv
import pandas as pd
import itertools

#on prend tous les fichiers qui existent dans le fichier test
entries = os.listdir('C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/test')
#variable i pour calculer les fichiers FCD.csv
i = 0

for entry in entries: 
    # condition si le fichier qui existe dans test est .zip
    if entry.endswith('.zip'): 
        zipdata = ZipFile(entry)
        entryinfos = zipdata.infolist()
        #je prends le nom de chaque fichier 
        foldern = os.path.basename(entry)
        # je prends la premiere partie du nom "20200106-15110"
        folder_name = foldern[0:14:1]

        for entryinfo in entryinfos:
            if entryinfo.filename.endswith('FCD.csv'):
        #le nouveau nom sera le nom du fichier dans lequel il existe+FCD
                newname = folder_name + '_FCD' + str(i) + '.csv'
                #changer le nom
                entryinfo.filename = newname
                # extract avec le nouveau nom
                zipdata.extract(entryinfo,'C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest')        
    i = i + 1


entries2 = os.listdir('C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest')
length = len(entries2) # from 0 to 5

datenew = ["Date","Time"]
#timenew = "Time"
j = 0
for entry in entries2: 
    if entry.endswith('.csv'):
        file_n = os.path.basename(entry)
        file_date = file_n[0:4:1] + '/' + file_n[4:6:1] + '/' + file_n[6:8:1]
        file_time = file_n[9:11:1] + ':' + file_n[11:13:1]
        datenew.append(file_date)
        datenew.append(file_time)
        #timenew[j] = file_time
        j = j + 2
    
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0,length*2,2):
        writer.writerow([datenew[i],datenew[i+1]])
        
        
new_path = ['C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest/']
entries3 = os.listdir('C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest')
length = len(entries3) # from 0 to 5

for i in range(length):
    new_path.append('C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest/')


#print(entries3)
#for entry in entries3:
#    if entry.endswith('.csv'):
# with open('innovators.csv', 'r', newline='') as f:
#     line_number = 1
#     row_count = sum(1 for row in f)

# with open('innovators.csv', 'r', newline='') as f:
#     csv_reader_object = csv.reader(f)
#     for row in csv_reader_object:
#         for y in row:
#             if y[1] = 
#         print(format(row))
#    line_number = 1
  #  for i in range(length):
     #   row =  next(itertools.islice(csv.reader(f), i, i+1)) 
    #row = next(itertools.islice(csv.reader(f), line_number, line_number+1)) 
   # print(row)
#print(new_path)

# line_number = 2  
# new_path[0] = 'C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest'+'/'+ entries3
# with open(new_path, 'rb') as f:
#     row = next(itertools.islice(csv.reader(f), line_number, line_number+1)) 

#with open('extractedtest/innovators.csv', 'w', newline='') as file:
    
     #   zipname = zip.namelist() #ceux qui existent dnas chaque document .zip
     #   for fileName in zipname: # on choisit seulement les FCD.zip et metadata
                # for filename in os.listdir('C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/test'):                    
         #   if fileName.endswith('.info'):
         #       zip.extract(fileName, 'C:/Users/Anna Christiane/Desktop/ismin/PI/data_client/extractedtest')
          #      print(fileName)

