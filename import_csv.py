import os
import csv
os.chdir("D:\python\code_snippets\Python-CSV")

print(os.getcwd())
with open('names.csv','r') as csv_file:
     csv_reader=csv.reader(csv_file)
     with open('new_name1.csv','w') as new_file:
         csv_writer=csv.writer(new_file,delimiter='\t')
         for line in csv_reader:
#         # print(line[2])
            csv_writer.writerow(line)






