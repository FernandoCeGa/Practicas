from ftplib import FTP
from typing import List
import re


class FTPConnection:
	def __init__(self, host, port, user, pssw):
		self.host = ""
		self.port = 0
		self.user = ""
		self.pssw = ""
		self.setHost(host)
		self.setPort(port)
		
		if user != "" and pssw != "":
			self.setUser(user)
			self.setPssw(pssw)

	############################################################
	def setHost(self, host):
		expr = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
		found = expr.search(host)
		if(found):
			print("[*] Host valido.")
			self.host = found.group()
		elif(" " not in host):
			print("[*] Host valido.")
			self.host = host
		else:
			print(f"[!] Su host '{host}' no es valido.")

	def getHost(self):
		return self.host

	############################################################
	def setPort(self, port):
		try:
			print("[*] Port valido.")
			self.port = int(port)
		except:
			print(f"[!] El puerto '{puerto}' no es valido.")

	def getPort(self):
		return self.port

	############################################################
	def setUser(self, user):
		if(len(user) > 1):
			print("[*] Usuario valido.")
			self.user = user
		else:
			print(f"[!] La longitud de su usuario '{user}' es demasiado corto")
			
	def getUser(self):
		return self.user

	################################################################
	def setPssw(self, pssw):
		if(len(pssw) >= 4):
			print("[*] Contraseña valida.")
			self.pssw = pssw
		else:
			print(f"[!] La longitud de la contraseña es demasiado corta")

	def getPssw(self):
		return self.pssw

	################################################################
	def saveFile(self, con: FTP, remote_file_path:str, local_file_path:str):
		with open(local_file_path,'wb') as local_file:
			con.retrbinary(f'RETR {remote_file_path}', local_file.write)

	def getTxtFile(self, con: FTP, file_path:str):
		listado = []
		con.retrlines(f'RETR {file_path}', listado.append)
		return listado

	def listFolder(self, con: FTP, directory:str):
	    print(directory)
	    listado = []
	    con.retrlines(f'LIST {directory}', listado.append)
	    return listado

	def getFileDir(self, con: FTP, directory:str):
		listado = self.listFolder(con,directory)
		return [file_info for file_info in listado if file_info.startswith('-')],  \
			[file_info for file_info in listado if not file_info.startswith('-')]

	 

	def getFileName(self, file_info:str) -> str:
		return ''.join(file_info.split()[8:])

	def ftpConnection(self, host, port, user:str="", pssw:str="", save_path:str=""):
		ftp = FTP()
		
		try:
			ftp.connect(host=host, port=port)
			ftp.login(user, pssw)
			print(":[*] Conexion fue exitosa.")
			actual_path = ''	
			l_file, l_dir = self.getFileDir(ftp, actual_path)
			
			for file_info in l_file:
				if(".msg" in str(l_file) or ".txt" in str(l_file) or "README" in str(l_file)):
					print("::[*] Archivo encontrado.")
					file_name = self.getFileName(file_info)
					self.saveFile(ftp, f'{actual_path}/{file_name}', f'{save_path}/{file_name}')
			ftp.close()
		except:
			print("[!] No se pudo establecer una conexion.")
			print("Intente mas tarde")
