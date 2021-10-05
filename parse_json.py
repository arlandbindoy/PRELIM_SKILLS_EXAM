import json
import csv

with open('covid_cases.json','r') as json_file:
    ourjson = json.load(json_file)

data = ourjson['records']
file = open('file.csv','w')
csvw = csv.writer(file)

num = 0
for i in data:
    if num ==0:
        header = i.keys()
        csvw.writerow(header)
        num +=1

    csvw.writerow(i.values())
    
file.close()
