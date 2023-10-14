#!/usr/bin/python3
#import a module

import json

#string with json format

my_data_JSON = """
{
   "name": "car",
   "type": "Nissan",
   "model": "Liberty",
   "make": "Japan",
   "year": "2014",
   "number": "KDM 001G",
   "millesge": "01200km/h",
   "other specifixcation": {
                               "type": "private",
                               "other feature":["sport","front drive"]
                               }
   "capacity": "seven seater",
   "eng_size": " 2000cc"


}
"""
#convert json string to dictionary
new_dict = json.loads(my_data_JSON)
