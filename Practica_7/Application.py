from Connection import *
from ftplib import FTP_PORT
from ftplib import FTP
import argparse
import os


parser = argparse.ArgumentParser(description="Datos para conexion FTP")
parser.add_argument("-host", type=str, help='-host "add the ip address"')
parser.add_argument("-port", type=str, help='-port "add the port"')
parser.add_argument("-user", type=str, help='-user "add the user"')
parser.add_argument("-pssw", type=str, help='-pssw "add password of the user"')
data = parser.parse_args()

host = data.host
port = data.port
user = data.user
pssw = data.pssw

if not os.path.exists("TXT"):
	os.makedirs("TXT")
os.chdir("TXT")

if user == None or pssw == None:
	user = ""
	pssw = ""

if(host != None and port != None):
	ftp_c = Connection(host, port, user, pssw)

	save_path = os.getcwd()
	host = ftp_c.getHost()
	port = ftp_c.getPort()
	user = ftp_c.getUser()
	pssw = ftp_c.getPssw()

	ftp_c.ftpConnection(host, port, user, pssw, save_path)

elif(host != None and port == None):
	port = FTP_PORT
	ftp_c = Connection(host, port, user, pssw)

	save_path = os.getcwd()
	host = ftp_c.getHost()
	port = ftp_c.getPort()
	user = ftp_c.getUser()
	pssw = ftp_c.getPssw()

	ftp_c.ftpConnection(host, port, user, pssw, save_path)
else:
	print("[!] Falto por agregar parametros.")
