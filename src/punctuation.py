filename = r'essays.txt'
import string 

numlines = 0

textfile = open(filename, 'r')



for line in textfile:
	out = line.translate(string.maketrans("",""), string.punctuation)
	print out
	
