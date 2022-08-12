import requests
import json
import os


class PBR_DB_Connect:
    def __init__(self, category):
        self.apiURL = 'https://api.physicallybased.info/'
        self.category = category
        self.presetsList = ""
        self.presetsNamesList = []
        self.getApiData()

    def getApiData(self):
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

    def getListOfNames(self):
        for item in self.presetsList:
            temp = (item["name"], item["name"], item["description"])
            self.presetsNamesList.append(temp)

        return self.presetsNamesList

    def getMaterialAttributes(self, materialName):
        return
