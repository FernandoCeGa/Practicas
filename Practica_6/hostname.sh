hostname=`hostname -i`
hostname=`nmap $hostname`

ifconfig=`curl ifconfig.me`
ifconfig=`nmap $ifconfig`

echo -e "$hostname \n$ifconfig" > datos.txt

base64 datos.txt > dEncode.txt

rm datos.txt
