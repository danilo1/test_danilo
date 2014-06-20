#Eliminates the punctuation from a text file and print it in a seperate file
import string
filename = r'essays.txt'
textfile = open(filename, 'r')
file = open('output.txt', 'w')

for line in textfile:
        out = line.translate(string.maketrans("",""), string.punctuation)
        file.write(out) # put all document in a new file
file.close()
	
