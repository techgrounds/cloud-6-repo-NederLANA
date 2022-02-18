#The output should be:
#True

def rtn(x):
	return(x)

foo = rtn(3)

if foo < rtn(4): #foo is defined as = rtn(3). So it must be less than rtn(4) to return a true.
	print(True)
else:
	print(False)