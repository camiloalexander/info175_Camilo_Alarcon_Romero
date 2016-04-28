#! /bin/bash  
usuario=$(hostname -s)  #obtenemos el nombre del usuario
cd /home/$usuario/Escritorio  #nos movemos inicialmente a escritorio
echo
echo "Ingrese carpeta fuente (Ej: /home/ SU USER /Escritorio/ ... / A RESPALDAR ): "
read Fuente   #leemos el directorio que queremos respaldar (direccion completa)
echo
echo "Ingrese carpeta destino (Ej: /home/ SU USER /Escritorio/ ... / GUARDAR EN ): "
read Destino	#leemos el directorio donde queremos guardar el respaldo (direccion completa)
echo

echo "Backup Initializing"
fecha=$(date +%Y_%m_%d_)  #obtenemos la fecha actual
#cd /home/alexndr/Escritorio/Respaldar

#Fuente="/home/$usuario/Escritorio/Respaldar"
#mkdir -m 777 /home/$usuario/Escritorio/$Destino
mkdir -m 777 /$Destino  #creamos una carpeta en escritorio donde se guardara el backup
#Destino="/home/$usuario/Escritorio/Backup"
#nombre=$basename /home/$usuario/Escritorio/Respaldar/
archivo="$fecha${Fuente##*/}.tar"  #nombre del archivo que contiene el respaldo
tar czf $Destino/$archivo $Fuente  #realiza el backup

echo 
echo "Quiere mover su Backup a otro directorio? (s/n):"
read opcion
if [ "$opcion" == "s" ]; then
	echo "Escriba a donde lo va a mover (Ej: /home/ SU USER /Escritorio/ ... / A MOVER ): "
	read move
	mv $Destino/$archivo $move  #el usuario puede mover el respaldo a otro directorio
	echo "Backup Finished"
	echo 
	echo "Fecha de respaldo:"
	date		#muestra la fecha en que se realizo el ultimo respaldo
	echo
	ls -lh $Destino  #lista los archivos dentro de la carpeta de destino
else
	echo "Backup Finished"
	echo 
	echo "Fecha de respaldo:"
	date		#muestra la fecha en que se realizo el ultimo respaldo
	echo
	ls -lh $Destino  #lista los archivos dentro de la carpeta de destino
fi
