Este es un script en bash para envio de correos

[*] El codigo debe de ser ejecutado como super usuario, como se muestra en el siguiente ejemplo:

===> Cerec@Kimjiroshi ~/Documents/Practica8$ sudo ./Application.sh

[*] El codigo debe de contener 3 parametros: 1. Correo, 2. Contraseña, 3. Hostname. Ejemplo:

===> Cerec@Kimjiroshi ~/Documents/Practica8$ sudo ./Application.sh "correo@gmail.com" "contraseña_del_correo" "el_host"

[*] Hay unos o mas parametros que se deben de agregar, me refiero al destinatario, para agregarlo(s) hay 
que hacer lo siguiente:

===> Cerec@Kimjiroshi ~/Documents/Practica8$ sudo ./Application.sh "correo@gmail.com" "contraseña_del_correo" "el_host"
===> "destinatario1" "destinatario2" "destinatario3"

[*] Como en cualquier correo es necesario agregarle el texto, el mismo còdigo se lo solicitara, y una 
vez que termine su mensaje debe de presionar las siguientes teclas:

===> 1. Enter
===> 2. Ctrl + D
