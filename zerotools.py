#!/usr/bin/dev python
#_*_ codign: utf-8 _*_

#waiting for more...
#wating for moth
import os ,sys
import subprocess, zipfile
from ftplib import FTP
import requests, socket 
import time, random
from bs4 import BeautifulSoup
from colorama  import init
from colored import fg, bg, attr
from progress.spinner import PieSpinner
from progress.bar import Bar
from bnner import *
init(autoreset=True)


#proximo window/linux
#info=input(str("\n\t\t\t[1]windows[proximo]\n\t\t\t[2]Linux[proximo]\n\t\t\t[3]Android: "))
print ("\t\t%sBETA 0.2\n\t\t==> help o h \n\t\t"%(fg(178)))
#revisar
def Ayuda():
            print ("Opciones:\n" )
            print("%s==>%szipcrack o 1:\ directorio del archivo \contraseña para fuerza bruta en formato txt passwd.text\n ejemplo:\n=>zipcrack \dir\dir\dir\n=>zipcrack=>passwd.txt\n=>pw\ ver directorio actual\n"%(fg(165), attr(0)))
            print("%s%s==>%sftp: o 2: conexion de tu ftp\n"%(fg(165),bg(232),attr(0)))
            print("%s==>%sip o 3: Ver Ip online"%(fg(165),attr(0))) 
            print("Observacion:\n\t Si usted tiene el mismo archivo zip y el password donde ejecuta\n\t el programa no es necesario especificar la ruta del directorio\n\t del archivo\n")
            pass
            
            
def zerotlls():
    while True:
        import zbanner
        print("\t\tzipcrack\n opcion:\t\n pw=>directorio\t\n run=>lanzar zpcrack\t\n ran=>fuerza bruta solo numeros\t\n quit=>salir")
        console=input(str("%szerotools=>%s"%(fg(199),attr(0))))
        if console=="run" or console=="r":
            nmzip=input(str("%srun=>zip>%s")%(fg(230),attr(0)))
            zipi=zipfile.ZipFile(nmzip)
            dirub=input(str("%srun=>password>%s")%(fg(230),attr(0)))
            files=open(dirub)
            spinner=PieSpinner()
            for line in files.readlines():
                passw=line.strip('\n')
                spinner.next()
             #observar linea
                try:
                    zipi.extractall(pwd=bytes(passw,'utf-8'))
                    #print ('%s[+]Cargando%s'%(bg(1),attr(0)))
                    print ("[+]Extracion Completa\n Contraseña: ",passw)
                except RuntimeError as TypeError:
                    #print ('[+]')
                    pass
                finally:
                    #print ('.__ningun archivo o contraseña no encontrada__.')
                    pass
             
        elif console=="pw" or console=="p":
                    dirt=subprocess.call('pwd')
                    print(dirt,"[Directorio Raiz]")
                    zerotlls()	
        elif console=="ran" or console=="ra":
            #proximo
            print ("forze random number")
        elif console=="quit" or console=="q":
            break                  
        else:
            pass


def ftp():
    #proximo
    sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connects=False
    ftpc=input("ftp#serve>")
    ftpcs=FTP(ftpc)
    print ("Ingrese Datos:")
    try:
        iftp=input("user#root>")
        iftp2=input("password#root>")
        ftpcs.login(iftp, iftp2)
        print ("Conexion Establecidad")
    except:
        print ("Error Conexion")
        if connects==False:
            while True:
                inp=input("root#root>")
                if inp=="1":
                    na=input("Nombre de Directorio: ")
                    try:
                        ftpcs.mkd(na)
                    except:
                        print ("[-]Archivo no Exitente")
                
                elif inp=="2":
                    op=input("Nombre de Directorio: ")
                    try:
                        ftpcs.cwd(op)
                    except:
                        print ("[-]No exite Directorio")

                elif inp=="3":
                                  ftpcs.dir()
                elif inp=="4":
                                  sys.os(exit)
                else:
                       print ('opps')



def ip():
    url={'url1': 'https://www.miip.es' }
    for x in url.values():
        getu=requests.get(x)
        status=getu.status_code
        if status==200:
            liip=[]
            print ("\t\t\033[32m"+"[Ver mi Ip Online]")
            html=BeautifulSoup(getu.text,"html.parser")
            add=html.header.h2
            for i in add:
                inip=liip.append(i)
                adn=liip[0]
                print ('\t\033[31m[*]',adn,"\033[31m[*]")
            else:
                pass
    else:
                 pass
                 
                 
   #relleno
    print ("exit")
    write="you program by pass "
    print (write)
    return


if __name__=="__main__":
    while True:
        i=input(str("%szerotools=>%s"%(fg(199),attr(0))))
        if i=="help" or i=="h":
            Ayuda()
        elif i=="zpcrack" or i=="z":
            zerotlls()
        elif i=="ftp" or i=="2":
             ftp()
        elif i=="ip" or i=="3":
              ip()
        elif i=='quit' or i=='q':
            break
        else:
            print("waring%s%s !%s"%(fg(15),bg(1),attr(0)))
#proximos
#reporta falla s4ndr01@tuta.io
