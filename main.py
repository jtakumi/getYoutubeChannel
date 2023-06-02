import makeCsv,makeJsonFile,os
from getYoutubeChannel import getYoutubeChannel
from filesManager import fileManager

def main():
        gYC = getYoutubeChannel()
        keyWord = input("please input the search key word.\n")
        createDir = input("would you create directory? \n if you'd like to create directory, please enter directory name. Or it's not, please press enter key. \n")
        if createDir == '':
                fileName = 'gotYoutubeChannel/' + keyWord + '.json'
        else:
               fileM = fileManager()
               fileM.makeDir(createDir)
               keyWord = keyWord + '.json'
               fileName = os.path.join('gotYoutubeChannel/',createDir,keyWord)
        gYC.getChannelInfo(fileName,keyWord)

if __name__ == '__main__':
    main()