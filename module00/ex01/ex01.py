import sys

n = len(sys.argv)
string="" 
for i in range(1, n):
    string+=" "+sys.argv[i]
S_case= string.swapcase()
print(''.join(reversed(S_case)))
