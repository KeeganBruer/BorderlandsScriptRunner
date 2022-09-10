import json
f = open('./config.json')
configuration = json.load(f)

def getConfig(name):
    return configuration[name]