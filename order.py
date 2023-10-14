#!/user/bin/python3

import orders

Open orders.json in read mode

with open(orders.json) as a file:
    data = json.load(file)

    #read a jon file and create a dictionary

    data = json.load(file)

    print(data)

