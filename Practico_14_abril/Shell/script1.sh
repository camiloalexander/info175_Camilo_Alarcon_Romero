#! /bin/bash   
#el interprete del resto de comandos

# Primer script 
#un comentario

echo Hola mundo  
#comando


#para ejecutar   ./script1.sh

#chmod 777 script1.sh    le damos los permisos


STRING="HELLO WORLD" #declaramos la variable
echo $STRING #imprimir la varaible en la shell


###############condiciones
VALID_PASSWORD="secret"
echo "INGRESE LA PASSWORD"
read PASSWORD
#importante los espacios al inicio y al final de los corchetes
if [ "$PASSWORD" == "$VALID_PASSWORD" ]; then
	echo "Acceso concedido"
else
	echo "Acceso denegado"
fi



