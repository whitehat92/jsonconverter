import sys
import json
file = sys.argv[1]

with open(file, "r") as filetoread:
    maindata = filetoread.read()
    mainobjct = maindata[maindata.find("{") : maindata.rfind("}")+1]
    objectjson = json.dumps(mainobjct)
    if "{" in objectjson and "}" in objectjson:
        print(objectjson.replace("{", "{"+"\n"),objectjson.replace("}","\n"+"}"))

