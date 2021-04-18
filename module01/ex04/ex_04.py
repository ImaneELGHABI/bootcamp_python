import random
import sys

sys.tracebacklimit = 0

def generator(text, sep=" ", option=None):
	words=text.split(sep)
	if option=="shuffle":
		for j in random.sample(range(len(words)), len(words)):
			print(words[j])	
	elif option=="unique":
		U=list(set(words))
		for j in range(len(U)):
			print(U[j])	
	elif option=="ordered":
		O=sorted(words)
		for j in range(len(O)):
			print(O[j])
	else:
		for j in range(len(words)):
			print(words[j])
	


text="Le Lorem Ipsum est simplement du faux texte. ghjkl; .hjjk"
for i in generator(text, sep=" ", option="shuffle"):
	print(i)						
