#!/usr/bin/dev python
#_*_ codign: utf-8 _*_

import os ,sys
import subprocess, zipfile
from ftplib import FTP
import requests, socket 
import time
from bs4 import BeautifulSoup
from colorama  import init
from colored import fg, bg, attr
from progress.spinner import Spinner
init(autoreset=True)

banner="""                         
                        ╱╱╱╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮
                        ╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃
                        ╭━━━┳━━┳━┳━┻┫┃┃┣┻━┳━━┫┃╭━━╮
                        ┣━━┃┃┃━┫╭┫╭╮┃┃┃┃╭╮┃╭╮┃┃┃━━┫
                        ┃┃━━┫┃━┫┃┃╰╯┃┃┃┃╰╯┃╰╯┃╰╋━━┃
                        ╰━━━┻━━┻╯╰━━╯╰╯╰━━┻━━┻━┻━━╯              
           
                                               
        _______2020 © copyleft contact: s4ndr01@tuta.io _______
"""
print(banner)
print("\t\t%sBETA 0.1\n\t\t==> help o h para ver ayuda\n\t\t==> vc o c para ver comandos"%(fg(178)))
def zerotlls():
    while True:
        console=input(str("%szerotools=>%s"%(fg(199),attr(0))))
        if console=="help" or console=="h":
            print ("Opciones:\n" )
            print("%s==>%szipcrack o 1:\ directorio del archivo \contraseña para fuerza bruta en formato txt passwd.text\n ejemplo:\n=>zipcrack \dir\dir\dir\n=>zipcrack=>passwd.txt\n=>pw\ ver directorio actual\n"%(fg(165), attr(0)))
            print("%s%s==>%sftp: o 2: conexion de tu ftp\n"%(fg(165),bg(232),attr(0)))
            print("%s==>%sip o 3: Ver Ip online"%(fg(165),attr(0))) 
            print("Observacion:\n\t Si usted tiene el mismo archivo zip y el password donde ejecuta\n\t el programa no es necesario especificar la ruta del directorio\n\t del archivo\n")
        elif console=="zpcrack" or console=="1":
             print  ("""
                        ╋╋╋╋╋╋╋┏━━━┓╋╋╋╋╋╋╋┏┓
                        ╋╋╋╋╋╋╋┃┏━┓┃╋╋╋╋╋╋╋┃┃
                        ┏━━━┳━━┫┃╋┗╋━┳━━┳━━┫┃┏┓
                        ┣━━┃┃┏┓┃┃╋┏┫┏┫┏┓┃┏━┫┗┛┛
                        ┃┃━━┫┗┛┃┗━┛┃┃┃┏┓┃┗━┫┏┓┓
                        ┗━━━┫┏━┻━━━┻┛┗┛┗┻━━┻┛┗┛
                        ╋╋╋╋┃┃
                        ╋╋╋╋┗┛          	     
             	           """) 
             	
             print("\t\tzipcrack\n opcion:\t pw=>directorio\t run=>lanzar zpcrack")
             try:
                 #observa linea 
                  consolez=input(str("zipcrack=>"))
                  if consolez=="pw":
                       dirt=subprocess.call('pwd')
                       print(dirt,consolez)
                       zerotlls()
                  elif consolez=="run":
                         nmzip=input(str("run=>zip>"))
                         zipi=zipfile.ZipFile(nmzip)
                         dirub=input(str("run=>password>"))
                         files=open(dirub)
                         for line in files.readlines():
                                passw=line.strip('\n')
                         #observar linea
                         try:
                                    zipi.extractall(pwd=bytes(passw,'utf-8'))
                                    print ('%s[+]Cargando%s'%(bg(1),attr(0)))
                                    print ("[+]Extracion Completa\n Contraseña: ",passw)
                         except:
                                    print ('.__ningun archivo o contraseña no encontrada__.')
                  else:
                        print ("end")     
             except TypeError:
                  print("fail")
        
        elif console=="vc" or console=="c":
                          print("\t\t zpcrack: zip cracked\n\t\t ftp: conexion ftp\n\t\t ip: ver ip\n")
        else:
             pass
        
        if console=="ftp" or console=="2":
                  CLA="\x1b[5;30;42m"
                  CLV="\x1b[5;30;42m"
                  CLR="\x1b[5;31;40m"
                  CLC="\x1b[3;33;40m"
                  ZR="\x1b[0m"
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

        else:
                  pass

        if console=="ip" or console=="3":
            url={
            	'url1': 'https://www.miip.es' 
            	}
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
                 
                 
    print ("exit")
    write="you program by pass "
    print (write)
    return


zerotlls()
