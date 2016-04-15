#! /bin/bash   
#declaracion de un arreglo con 4 elementos
ARRAY=( 'Debian Linux' 'Redhat Linux' Ubuntu Linux)
#obtener el numero de elementos
ELEMENTS=${#ARRAY[@]}
#imprimir todos los elementos con un for
for(( i=0;i<$ELEMENTS;i++ )); do
	echo ${ARRAY[${i}]}
done
