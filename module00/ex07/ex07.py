#import string
import sys

#punc = string.punctuation

#space = [' ']

A = sys.argv[1]
B = sys.argv[2]

if A.isdigit():
	print("ERROR")
	exit()

if B.isdigit()==False:
	print("ERROR")
	exit()

L= [i for i in A.split() if len(i)>int(B)]
print(L)
