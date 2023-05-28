import makeCsv,makeJsonFile
from getYoutubeChannel import getYoutubeChannel

def main():
        gYC = getYoutubeChannel()
        print("please input the search key word.")
        keyWord = input()
        fileName = 'gotYoutubeChannel/' + keyWord + '.json'
        gYC.getChannelInfo(fileName,keyWord)

if __name__ == '__main__':
    main()