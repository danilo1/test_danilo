#Eliminates the punctuation from a text file
filename = r'essays.txt'
import string 

numlines = 0

textfile = open(filename, 'r')
txtfile= open ("output.txt", 'w')# creating a file called output.txt

for line in textfile:
	out = line.translate(string.maketrans("",""), string.punctuation)
	txtfile.write(out)
txtfile.close()
