import json
from os import path as p, system as cmd

class Translator():
    def __init__(self) -> None:
        self.modFilePath = input('Path to .reds file: ')
        self.jsonFilePath = input('path to .json file: ')
        self.modFile = ''
        self.jsonFile = ''

        self.modFileName = self.modFilePath.split('\\')
        self.modFileName = self.modFileName[::-1][0]
        
        self.modFileDir = self.modFilePath.replace(self.modFileName, '')

    def ReadMod(self):
        with open(self.modFilePath, 'r') as file:
            self.modFile = file.read()
    
    def ReadJson(self):
        with open(self.jsonFilePath, 'r') as file:
            self.jsonFile = json.load(file)

    def TranslateMod(self):
        for i in self.jsonFile['entries']:
            self.modFile = self.modFile.replace(self.jsonFile['entries'][i]['key'], self.jsonFile['entries'][i]['value'])

    def RewriteMod(self):
        newModFileDir = p.join(self.modFileDir, 'Localization', self.jsonFile['lang'])
        newModFilePath = p.join(newModFileDir, self.modFileName)
        cmd(f'md {newModFileDir}')
        with open(newModFilePath, 'w') as file:
            file.write(self.modFile)



if __name__ == '__main__':
    cmd('cls')
    app = Translator()
    app.ReadMod()
    app.ReadJson()
    app.TranslateMod()
    app.RewriteMod()
