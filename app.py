from flask import Flask, render_template, request
from pymongo import MongoClient


# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://controlLaptop:controlLaptop@controllaptop.tshkzxy.mongodb.net/test"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)

db = client.laptopCommands.commandsCollection

fNames = ["volumeIncrease", "previousTrack", "backSeek", "pause", "forwardSeek", "nextTrack", "volumeDecrease", "escape", "desktop", "fullScreen", "one", "two", "three", "four", "nextTab", "newTabYT", "escapeYT", "volUpYT", "startYT", "iButtonYT", "fullScreenYT", "volDownYT", "saveMusicYT", "newTabGC", "saveLinkGC", "newTabFM", "click1FM", "volUpFM", "startFM", "click2FM", "fullScreenFM", "volDownFM", "newTabN", "volUpN", "skipIntroN", "fullScreenN", "volDownN", "newTabAP", "volUpAP", "startAP", "fullScreenAP", "volDownAP", "scrollUpMain", "clickMain", "moveUpMain", "closeTabMain", "refreshMain", "scrollDownMain", "moveleftMain", "movedownMain", "moverightMain", "goBackMain"]



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        functionName = request.form.get("functionName")
        if functionName in fNames:
            db.insert_one({"functionName":functionName, "searchData":""})
            # fValues[fNames.index(functionName)]()
        else:
            searchData = request.form.get("searchData")
            db.insert_one({"functionName":functionName, "searchData":searchData})
            # searchValues[searchNames.index(functionName)](searchData)

        print(functionName)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0")