#!/usr/bin/dev python
#-*- coding: "utf-8" -*-
from ftplib import FTP
import socket 
import os 
import time

#Leer Linea 74

#Servidor del Ftp
#Nombre de Usuario
#Contraseña
#write line by codeS
#write script CodeS-A 


#Creamos variables 
#por completar*
CLA="\x1b[5;30;42m"
CLV="\x1b[5;30;42m"
CLR="\x1b[5;31;40m"
CLC="\x1b[3;33;40m"
ZR="\x1b[0m"
print ("%s\t\t[-------------------------------------------------]%s"%(CLC,ZR))
print ("%s\t\t[-------Autor:codeS correo:s4ndr01@tuta.io------]%s"% (CLC,ZR))
print ("%s\t\t[-------------------------------------------------]%s"%(CLC,ZR))


print ("""
              1-Crear Directorio
              2-Abrir Directorio
              3-Ver Toda Las Carpeta y Archivo
          """)

def red():
        #por completar*
	sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sockets.connect("",80)
	connects=False
	print ("Inicie secion:")
	ftpc=input("ftp#serve>")
	ftpcs=FTP(ftpc)
	print ("Ingrese Datos:")
	try:
	     iftp=input("user#root>")
	     iftp2=input("password#root>")
	     ftpcs.login(iftp, iftp2)
	     print ("Done Connect")
	except:
	      print ("Error Conexion")
	      red()
        #hace un ciclo infinito para manejarno dentro del servidor
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
	              pass
	              
	                     
if __name__=="__main__":
    red()
#Hola! ;) 
#¿Como Funciona?
#Son tres opciones
#1- Crear Carpeta
#2- Ver Carpeta
#3- Ver toda la Carpeta
#Es todo :') 
#Mi correo s4ndr01@tuta.io
#Instagram code_bin11
#Twitter sanS01b
#Los conocimiento y uso  de la libreria www.python.org y #https://docs.python.org/3/
#Este Script puede ser distribuido y compartido, el uso de tercero es responsabilidad de quiene usen, favor agregar link
#github.com/codeS-A
#:') bye
#Mier, Julio, 2019
#Vier, Febrero, 2020
