#The output should be:
#['Dog', 'Cat', 'Fly']
#remove the short_name = [] within the for loop.
#the print function now calls to the short_names list defined at the top.
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
print(short_names)