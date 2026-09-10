import json

def jsonhandling1(filepath):
    with open(filepath) as data:
      finaldata=json.load(data)
      return finaldata
    