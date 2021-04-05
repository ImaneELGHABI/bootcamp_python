import sys

def fun(a, b):
	add = a + b
	dif = a - b
	mul = a * b
	div = a / b
	modulus = a % b
	return add, dif, mul, div, modulus

a=int(sys.argv[1])
b=int(sys.argv[2])
print('Sum of ',a ,'and' ,b ,'is :', fun(a, b)[0])
print('Difference of ',a ,'and' ,b ,'is :',fun(a,b)[1])
print('Product of' ,a ,'and' ,b ,'is :',fun(a,b)[2])
print('Division of ',a ,'and' ,b ,'is :',fun(a,b)[3])
print('Modulus of ',a ,'and' ,b ,'is :',fun(a,b)[4])


