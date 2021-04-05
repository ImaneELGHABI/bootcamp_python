import sys

if(len(sys.argv)<=1):
	sys.exit(1)
n=int(sys.argv[1])

if(len(sys.argv)>2):
	print("ERROR")
else:
	if(n==0):
		print("I'm Zero")
	if(n%2==0):
		print("I'm Even")
	if(n%2!=0):
		print("I'm Odd")
#if(isinstance(sys.argv[1],int)==False):
#	print("ERROR")
