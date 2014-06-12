filename = r'essays.txt'
import string 

numlines = 0

textfile = open(filename, 'r')



for line in textfile:
	numlines+=1
	out = line.translate(string.maketrans("",""), string.punctuation)
	print out
	
print numlines