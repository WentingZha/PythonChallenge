#Selection
# "${v}" stand for a variable.We can also use $v, "$v", ${v}
#) stand for the end of a pattern

selection(){
	case "${v}" in 
	"ab") 
		echo "two characters"
		;;
	"cde")
		echo "three characters"
		;;
	esac
}

selection "1"

read -n 1 -p "Press any key to continue..."