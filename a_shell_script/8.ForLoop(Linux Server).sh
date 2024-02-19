#Selection
# "${v}" stand for a variable.We can also use $v, "$v", ${v}
#) stand for the end of a pattern

forLoop(){
	for var in A B C D E
	do 
		echo "{${var}"
	done
}

read -n 1 -p "Press any key to continue..."