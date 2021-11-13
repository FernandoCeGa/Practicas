#!/bin/bash

apt install ssmtp
clear

if [[ $1 == "" || $2 == "" || $3 == "" || $4 == "" ]]; then
	echo "[!] Hacen falta parametros."
	exit
else
	user_email=$1
	user_password=$2
	host_name=$3
fi

cant_be=(" " "|" "°" "¬" "!" "\"" "$" "%" "&" "/" "(" ")" "=" "'" "?" "\¿" "¡" "´" "¨" "+" "*" "~" "{" "[" "^" "}" "]" "\`" "," ";" ":" "-" "_" "<" ">" "é" "ý" "ú" "í" "ó" "á" "É" "Ý" "Ú" "Í" "Ó" "Á" "ë" "ÿ" "ü" "ï" "ö" "ä" "Ë" "Ü" "Ï" "Ö" "Ä")
# Verificamos el correo del usuario
for character in ${cant_be[@]}; do
	if [[ $user_email == *"$character"* ]]; then
		echo "[!] El correo no puede contener el siguiente caracter: '$character'."
		exit
	fi
done
if [[ $user_email == *"gmail.com"* ]]; then
	echo "[*] Correo valido."
else
	echo "[!] Correo invalido."
fi



# Verificamos la contraseña
if [[ "${#user_password}" -ge 8 ]]; then
	echo "[*] Contraseña valida."
else
	echo "[!] Contraseña invalida."
	exit
fi


cat > /etc/ssmtp/ssmtp.conf <<EOF
#
# Config file for sSMTP sendmail
#
# The person who gets all mail for userids | 1000
# Make this empty to disable rewriting.
#root=postmaster
SERVER=$user_email

# The place where the mail goes. The actual machine name is required no
# MX records are consulted. Commonly mailhosts are named mail.domain.com
mailhub=smtp.gmail.com:587
#Or whatever domain you using

AuthUser=$user_email
AuthPass=$user_password
UseTLS=YES
UseSTARTTLS=YES

# Where will the mail seem to come from?
rewriteDomain=gmail.com
#Or whatever @domain.com you using
# The full hostname
hostname=$host_name
#Get the hostname by issuing the command hostname

# Are users allowed to set their own From: address?
# YES - Allow the user to specify their own From: address
# NO - Use the system generated From: address
FromLineOverride=YES
EOF

declare -i counter=0
for param in $@; do
	if [[ $counter -ge 3 ]]; then
		receiver_email="$receiver_email $param"
	fi
	counter=$counter+1
done

echo "[+] Escibe el mensaje"
echo "::: *Al finalizar presionar 'enter' y luego"
echo ":::  'Ctrl + D'"
ssmtp $receiver_email
