#!/usr/bin/dev python
#_*_ codign: utf-8 _*_
#import urllib3
import argparse
from colorama import init
import requests
from bs4 import BeautifulSoup
init(autoreset=True)

arg=argparse.ArgumentParser(description=" Lista")
arg.add_argument("h",action="store_true", default=None, help="errores reporta s4ndr01@tuta.io")
arg=arg.parse_args()
url={
	     'url1': 'https://www.miip.es'
	     }
def main():
    for x in url.values():
        getu=requests.get(x)
        status=getu.status_code
    if status==200:
        liip=[]
        print ("\033[32m"+"[Ver mi Ip Online]")
        html=BeautifulSoup(getu.text,"html.parser")
        add=html.header.h2
        for i in add:
            inip=liip.append(i)
            adn=liip[0]
            print ('\033[31m'+"[*]**************[*]\n",adn)
    else:
        pass


main()

#report correo:s4ndr01@tuta.io
#7-03-2020
#................
