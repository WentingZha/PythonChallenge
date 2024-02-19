#'v' -- '' contains no parameters
#"v $1" -- parameters can be added into ""
setVariable(){
	return $1
}
#setVariable 1
#echo $?

#`command`
# $(command)
#echo $(date)

#echo `date`

# "${v}" stand for a variable.We can also use $v, "$v", ${v}
echo "Now $(date)"

read -n 1 -p "Press any key to continue..."