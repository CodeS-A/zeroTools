#!/usr/bin/dev python
#_*_ codign: utf-8 _*_

from colored import fg, bg, attr
import os
import sys
import subprocess
import zipfile
from ftplib import FTP
import requests
import socket 
import time
from bs4 import BeautifulSoup
from colorama  import init

init(autoreset=True)

banner="""

                                            
                 .-----..-----..----..-----.
                 |-- __||  -__||   _||  _  |")
                 |_____||_____||__|  |_____|
                                            
               _______                __        
              |_     _|.-----..-----.|  |.-----.
                |   |  |  _  ||  _  ||  ||__ --|
                |___|  |_____||_____||__||_____|
                                               
         _____2020 © copyright contacct: s4ndr01@tuta.io _______
"""
print(banner)
print("==>escribe help para ver ayuda\n==> vc para ver comandos")
def zerotlls():
    while True:
        console=input(str("zerotools=>"))
        if console=="help":
            print ("Opciones:\n" )
            print("%s==>%szipcrack\ directorio del archivo \contraseña para fuerza bruta en formato txt passwd.text\n ejemple:\n=>zipcrack \dir\dir\dir\n=>zipcrack=>passwd.txt\n=>pw\ ver directorio actual\n"%(fg(158), attr(0))) 
            print("%s==>%sip\ imprime tu ip oline\n"%(fg(158),attr(0)))
            print("%s==>%sftp \ navega desde tu archivos\n"%(fg(158),attr(0))) 
            print("Observacion:\n\t Si usted tiene el mismo archivo zip y el password donde ejecuta\n\t el programa no es necesario especificar la ruta del directorio\n\t del archivo\n")
        elif console=="zpcrack":
             print("\t\tzipcrack\n opcion:\n pw=>directorio\n z=>correr programa")
             try:
                 #observa linea 
                  consolez=input(str("zipcrack=>"))
                  if consolez=="pw":
                       dirt=subprocess.call('pwd')
                       print(dirt,consolez)
                  elif consolez=="zc":
                         nmzip=input(str("=>zipcrack=>"))
                         zipi=zipfile.ZipFile(nmzip)
                         dirub=input(str("=>zipcrack=>"))
                         files=open(dirub)
                         for line in files.readlines():
                                passw=line.strip('\n')
                         #observar linea
                         try:
                                    zipi.extractall(pwd=bytes(passw,'utf-8'))
                                    print ("[+]Extracion Completa",passw)
                         except:
                                    print ('.....')
                  else:
                        print ("end")     
             except TypeError:
                  print("fail")
        
        elif console=="vc":
                          print("\t\t zpcrack: zip cracked\n\t\t ftp: conexion ftp\n\t\t ip: ver ip\n")
        else:
             pass
        
        if console=="ftp":
                  CLA="\x1b[5;30;42m"
                  CLV="\x1b[5;30;42m"
                  CLR="\x1b[5;31;40m"
                  CLC="\x1b[3;33;40m"
                  ZR="\x1b[0m"
                  sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  connects=False
                  print ("Inicie secion:")
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

        if console=="ip":
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
