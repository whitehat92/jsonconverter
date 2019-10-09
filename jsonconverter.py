import sys
import json
import demjson
file = sys.argv[1]

with open(file, "r") as filetoread:
    maindata = filetoread.read()
    mainobjct = maindata[maindata.find("{") : maindata.rfind("}")+1]
    objectjson = json.dumps(mainobjct)
    print(demjson.decode(objectjson))
