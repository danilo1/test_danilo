#counts the number of words in a text file
#hi how are you
# TESTING THE GAME
filename = r'essays.txt'


numlines = 0

textfile = open(filename, 'r')



for line in textfile:
	numlines+=1
	
print numlines