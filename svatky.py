#svatky
from pyfiglet import Figlet
import datetime
import json
import time


with open("svatky-db.json", "r", encoding="utf-8") as f: 
    data = json.load(f)         # nacte .json

    today = datetime.datetime.now()
    month_index = today.month - 1
    day_key = f"{today.day}."

    month_obj = data[month_index]
    name = month_obj.get(day_key, "")


    f = Figlet(font='slant')
    print(f.renderText('ceske svatky'))
    
    t = datetime.datetime.now()
    print(t)

    print("Kdo má svátek")
    print("1) DNES")
    print("2) ZITRA")

    a = input("vyber jednu z moznosti: ")

    if a == "1":
        if name:
            print(f"Dnes má svátek {name}")

        else:
            print("Spatna moznost!")

    if a == "2":
        if name:
            print()

input("Stiskni enter pro ukonceni...")