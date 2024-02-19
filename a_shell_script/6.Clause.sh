#Check if the process exists
processExist(){
	if [ -z "tasklist | findstr /I notepad++.exe" ]
	then
		echo "The process is not running"
	else
		echo "The process is running"
	fi
}
processExist
read -n 1 -p "Press any key to continue..."