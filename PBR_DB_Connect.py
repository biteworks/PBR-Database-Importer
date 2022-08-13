import json
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class PBR_DB_Connect:
    def __init__(self, category):
        self.apiURL = 'https://api.physicallybased.info/'
        self.category = category
        self.presetsList = ""
        self.presetsNamesList = []

    def getApiData(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        req = requests.get(self.apiURL + self.category, verify=False)
        if req.status_code == 200:
            self.presetsList = json.loads(req.text)
            self.writeCache()
        else:
            print('No connection to API')
        return

    def writeCache(self):
        pathToScript = os.path.realpath(__file__)
        pathToAddon = os.path.dirname(pathToScript)
        pathToCacheFolder = os.path.join(pathToAddon, "cache")
        if not os.path.exists(pathToCacheFolder):
            os.makedirs(pathToCacheFolder)
        cacheFile = os.path.join(pathToCacheFolder, self.category + ".json")
        file = open(cacheFile, "w")
        file.write(json.dumps(self.presetsList))
        file.close
        return

    def readCache(self):
        pathToScript = os.path.realpath(__file__)
        pathToAddon = os.path.dirname(pathToScript)
        pathToCacheFolder = os.path.join(pathToAddon, "cache")
        cacheFile = os.path.join(pathToCacheFolder, self.category + ".json")
        if os.path.exists(cacheFile):
            file = open(cacheFile, "r")
            self.presetsList = json.loads(file.read())
        return

    def getListOfNames(self):
        self.readCache()
        for item in self.presetsList:
            temp = (item["name"], item["name"], item["description"])
            self.presetsNamesList.append(temp)

        return self.presetsNamesList

    def getAttributes(self, name):
        self.readCache()

        for obj in self.presetsList:
            if obj["name"] == name:
                return obj
