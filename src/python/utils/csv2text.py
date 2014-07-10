''' This python program should read each line of essays.csv and save it as a separate file with a the name essay<lineach line of essays.csv and save it as a separate file with a the name essay<line_number>.txte_number>.txt

That is, the first line should be saved as essay1.txt, the second line as essay2.txt, etc.
''' 






filename = r'/Users/d-jara/test_danilo/test/essays.csv'
f = open(filename)

a =1
line = f.readline()
while line:
    txtfile = open ("essay"+str(a)+".csv", 'w') # here I save each line as a file 
    a += 1 # This variable will change the file number
    txtfile.write(line) # writing the line into the new document 
    line = f.readline() # moving into the new line
    txtfile.close()

f.close()

