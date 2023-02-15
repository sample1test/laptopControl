import pymongo
import json
from bson.json_util import dumps
from aMainTopFunctions import *
from bHomeFunctions import *
from cYouTubeFunctions import *
from dGoogleChromeFunctions import *
from eFMoviesFunctions import *
from fPrimeVideosFunctions import *
from gNetflixFunctions import *
from hMainBottomFunctions import *

client = pymongo.MongoClient("mongodb+srv://controlLaptop:controlLaptop@controllaptop.tshkzxy.mongodb.net/test")

fNames = ["volumeIncrease", "previousTrack", "backSeek", "pause", "forwardSeek", "nextTrack", "volumeDecrease", "escape", "desktop", "fullScreen", "one", "two", "three", "four", "nextTab", "newTabYT", "escapeYT", "volUpYT", "startYT", "iButtonYT", "fullScreenYT", "volDownYT", "saveMusicYT", "newTabGC", "saveLinkGC", "newTabFM", "click1FM", "volUpFM", "startFM", "click2FM", "fullScreenFM", "volDownFM", "newTabN", "volUpN", "skipIntroN", "fullScreenN", "volDownN", "newTabAP", "volUpAP", "startAP", "fullScreenAP", "volDownAP", "scrollUpMain", "clickMain", "moveUpMain", "closeTabMain", "refreshMain", "scrollDownMain", "moveleftMain", "movedownMain", "moverightMain", "goBackMain"]
fValues = [volumeIncrease, previousTrack, backSeek, pause, forwardSeek, nextTrack, volumeDecrease, escape, desktop, fullScreen, one, two, three, four, nextTab, newTabYT, escapeYT, volUpYT, startYT, iButtonYT, fullScreenYT, volDownYT, saveMusicYT, newTabGC, saveLinkGC, newTabFM, click1FM, volUpFM, startFM, click2FM, fullScreenFM, volDownFM, newTabN, volUpN, skipIntroN, fullScreenN, volDownN, newTabAP, volUpAP, startAP, fullScreenAP, volDownAP, scrollUpMain, clickMain, moveUpMain, closeTabMain, refreshMain, scrollDownMain, moveleftMain, movedownMain, moverightMain, goBackMain]

searchNames = ["searchYouTube","searchGoogleChrome","searchFMovies","searchFMovies","searchNetflix","searchPrime"]
searchValues = [searchYouTube, searchGoogleChrome, searchFMovies, searchFMovies, searchNetflix, searchPrime]

change_stream = client.laptopCommands.commandsCollection.watch()
for change in change_stream:
    # print(type(change))
    functionName = change['fullDocument']['functionName']
    searchData = change['fullDocument']['searchData']

    if functionName in fNames:
        fValues[fNames.index(functionName)]()
    else:
        searchValues[searchNames.index(functionName)](searchData)