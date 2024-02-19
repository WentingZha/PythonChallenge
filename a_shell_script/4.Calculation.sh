#Remember to set a space between the command elements 
plus(){
	#echo "Input parameter $1 and $2"
	#return $(($1+$2))
	return `expr 1 + 2`
}
#plus 1 2
#plus
#echo "The result of plus is $?"

minus(){
	#echo "Input parameter $1 and $2"
	#return $(($1-$2))
	return `expr 2 - 1`
}
#minus
#echo "The result of minus is $?"

multiply(){
	echo "Input parameter $1 and $2"
	return `expr $1 \* $2 `
}
#multiply 1 2
#echo "The result of multiply is $?"

devide(){
	echo "Input parameter $1 and $2"
	return `expr $1 / $2 `
}
#devide 2 1
#echo "The result of devide is $?"

mode(){
	#echo "Input parameter $1 and $2"
	return `expr $1 % $2`
}
mode 4 3
echo "The result of mode is $?"

read -n 1 -p "Press any key to continue..."