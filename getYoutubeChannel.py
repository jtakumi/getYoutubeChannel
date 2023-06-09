from googleapiclient.discovery import build
import json
from filesManager import fileManager
from makeCsv import makeCSV

class getYoutubeChannel:

    def getChannelInfo(self,fileName,keyWord):
        fileM = fileManager()
        APIKEY = fileM.readFile('','.key')
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        youtube=build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey = APIKEY
        )

        try:
            searchResponse=youtube.search().list(
                q=keyWord,
                part='id,snippet',
                maxResults=25
            ).execute()
        except Exception as e:
            print('An error occurred while fetching search results.')
            return
        channelDataList = []
        with open(fileName,'w',encoding='utf-8') as f:
            for searchResults in searchResponse.get('items',[]):
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
                mkCSV = makeCSV()

                print(searchResults)
                print(json.dumps(channelResponse,indent=2,ensure_ascii=False),file=f)
                

