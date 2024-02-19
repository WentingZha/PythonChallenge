#!  --not
#-o --or
#-a --and
a = 1
b = 2
c = 3
[!1 -eq 1]
echo "The first result is:$?"
["${a}" -lt 2 -o  "${b}" -gt 3]
echo "The second result is:$?"
["${a}" -lt 2 -a  "${b}" -gt 3]
echo "The third result is:$?"