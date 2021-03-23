#with json

import json
import sys

filetext = sys.argv[1]

dict1 = {}

with open(filetext) as fh:
        for line in fh:
                command, description = line.strip().split(None, 1)
                dict1[command] = description.strip()
out_file = open("jsonconverted", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()
