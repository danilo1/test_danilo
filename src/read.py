#counts the number of words in a text file
filename = r'essays.txt'


numlines = 0

textfile = open(filename, 'r')



for line in textfile:
	numlines+=1
	
print numlines