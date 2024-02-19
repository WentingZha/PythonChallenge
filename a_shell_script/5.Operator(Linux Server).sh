#equal [$a = $b]
#not equal [$a != $b]
#check whether the length of the string is 0 [-z $a]
#check whether the length of the string is not 0 [-n "$a"]
#check whether the string is null [$a]

equal(){
	echo "Input $a and $b"
	return ["${a}" -eq "${b}"]
}
equal 1 2
echo $?

notEqual(){
	echo "Input two strings $a and $b"
	return [${a} != ${b}"]
}

lengthEqualToZero(){
	echo "Input string $a"
	return  [-z "$a"]
}

lengthNotEqualToZero(){
	echo "Input string $a"
	return  [-n "$a"]
}



read -n 1 -p "Press any key to continue..."