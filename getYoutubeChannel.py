from googleapiclient.discovery import build
import json
from filesManager import fileManager

class getYoutubeChannel:

    def getChannelInfo(self,fileName,keyWord):
        fileM = fileManager()
        apiKey = fileM.readFile('','.key')
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        youtube=build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey = apiKey
        )

        try:
            searchRespose=youtube.search().list(
                q=keyWord,
                part='id,snippet',
                maxResults=25
            ).execute()
        except Exception as e:
            print('An error occurred while fetching search results.')
            return
        channelDataList = []
        with open(fileName,'w',encoding='utf-8') as f:
            writingCount = 0
            for searchResults in searchRespose.get('items',[]):
                while(writingCount == 0):
                    if searchResults['id']['kind'] !=  'youtube#channel':
                        continue

                    channelId = searchResults['id']['channelId']
                    channelResponse = youtube.channels().list(
                        part = 'statistics,snippet',
                        id = channelId
                    ).execute()

                    channelData = {}
                    channelData['channelName'] = searchResults['snippet']['channelTitle']
                    channelData['videoCount'] = channelResponse['items'][0]['statistics']['videoCount']
                    channelData['viewCount'] = channelResponse['items'][0]['statistics']['viewCount']
                    channelData['subscribers'] = channelResponse['items'][0]['statistics']['subscriberCount']
                    channelData['country'] = channelResponse['items'][0]['snippet'].get('country','')

                    channelDataList.append(channelData)

                    print(searchResults)
                    print(json.dumps(channelResponse,indent=2,ensure_ascii=False),file=f)
                    writingCount += 1

