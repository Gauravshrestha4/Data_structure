#pattern 1 method 1
x=0
while x!=10:
	print("* "*x)
	x+=1
#pattern 1 method 2
x=1
while x<=10:
	count=1
	string=""
	while count<=x:
		string+="* "
		count+=1
	print(string)
	x+=1

#pattern 2 method 1
x=1
while x<=10:
	print(" "*(10-x) + "* "*x)
	x+=1

#pattern 2 method 2
x=1
while x<=10:
	count=1
	string=""
	while count<=10-x:
		string+=" "
		count+=1
	count=1
	while count<=x:
		string+="* "
		count+=1
	print(string)
	x+=1