#The output should be:
#4
#16129

def square(x):
	return x**2

nr = square(2)
print(nr)

foo = 127    #foo needs to be defined at the top before it is called to a following variable.
big = square(foo)
print(big)
