import os,json,shutil

class readFile:

    def readFile(self,dirName,fileName):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dirName,fileName)),"r",encoding='utf-8') as f:
            getFileName = f.readline()
            getFileName = getFileName.replace('\n','')
        return getFileName
    
    def writeFile(self,outPut,dirName,fileName):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dirName,fileName)),"w") as f:
            print(outPut,file=f)


    def jsonRead(self,dirName,fileName):
         with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dirName,fileName)),'r',encoding='utf-8') as f:
                getData = json.load(f)
         return getData
    
    def jsonWrite(self,outPut,dirName,fileName):
          with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dirName,fileName)),'w') as f:
            json.dump(outPut, f, indent = 2, ensure_ascii=False)

    
    def getFileName(self,fileName):
        exExtension = fileName.replace('.json','')
        index = exExtension.find('_')
        getName = exExtension[:index]
        getName = ''.join(getName)
        return getName
    
    def copeFile(self,dirName,copyDir):
        for fileName in os.listdir(dirName):
            filePath = os.path.join(dirName,fileName)
            direction = os.path.join(copyDir,fileName)
            shutil.copy2(filePath,direction)
            print(fileName + " has copied.")
        print("All process done.")
