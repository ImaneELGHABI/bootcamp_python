def text_analyzer(infile):
	other,space,lower,upper=0,0,0,0
	lines = infile.readlines()
	for L in lines:
		for i in L:
        		if i.isupper():
            			upper += 1
        		elif i.islower():
            			lower += 1
        		elif i.isspace():
            			space +=1
        		else:
            			other +=1
	return[other,space,lower,upper]

infile=open("ex03.py", "r")
print(text_analyzer(infile))
#print("The text contains "   " characters:\n")
#print(text_analyzer(infile)[3] " upper letters\n")
#print(text_analyzer(infile)[2] " lower letters\n")
#print(text_analyzer(infile)[0] " punctuation marks\n")
#print(text_analyzer(infile)[1] " spaces"\n)
