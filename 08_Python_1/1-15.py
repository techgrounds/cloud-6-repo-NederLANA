#The output should be:
#a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||

foo = ''
for i in range(3):
	foo += 'a'
	for j in range(3):
		foo += '5'
		for k in range(3): #indent so that | is executed 3 times within 5 loop
            #then 5 is in turn executed 3 times within a
			foo += '|'

print(foo)



