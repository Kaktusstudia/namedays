#svatky
from pyfiglet import Figlet
import datetime


def Main():
    f = Figlet(font='slant')
    print(f.renderText('ceske svatky'))
    
    t = datetime.datetime.now()
    print(t)

    print("Kdo má svítek..")
    print("dnes")
    print("zitra")

    a = input("vyber jednu z moznosti: \n")


    


Main()