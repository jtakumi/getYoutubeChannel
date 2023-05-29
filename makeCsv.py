import csv,json,os
from filesManager import fileManager

class makeCSV:
    def fromJson(jsonDir,jsonFIle,csvDir,csvFile):
        fileM = fileManager()
        jsonData = fileM.jsonRead(jsonDir,jsonFIle)
        csvPath = os.path.join(csvDir,csvFile)
        if len(jsonData) > 0:
            with open(csvPath,'w',encoding='utf-8-sig',newline='') as f:
                fieldNames = ['channel_name','video_count','view_count','subscribers','country']
                writer = csv.DictWriter(f,fieldnames=fieldNames)
                writer.writeheader()
                for item in jsonData:
                    writer.writerow(item)
            print(f'CSV file"{csvFile}" has been created.')
        else:
            print('No found. error 404.')
