#no parameter no return
method(){
	echo "method"
}
#method

#method with 2 parameters and no value to return
method2(){
	echo "parameter1 $1"
	echo "parameter2 $2"
}

#method2 1 2

#method with 2 parameters and value to return
method3(){
	echo "parameter1 $1"
	echo "parameter2 $2"
	return $(($1+$2))
}
method3 1 2
echo $?

read -n 1 -p "Press any key to continue..."