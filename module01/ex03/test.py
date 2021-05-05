from matrix import Matrix

data=([[1,2,3],
	[4,5,6],
	[2,4,6]])
#data=(2,3)
data1=[[2,2,2],[2,2,2],[2,2,2]]
vec=[1, 1, 1]
D=Matrix(data)
D1=Matrix(data1)
print(D)
print(D1)
print("Matrix+scalar:\n")
print(Matrix(data1).__radd__(2))
print("Matrix+Matrix:\n")
print(Matrix(data).__add__(data1))
print("Matrix-scalar:\n")
print(Matrix(data).__rsub__(2))
print("Matrix-Matrix:\n")
print(Matrix(data).__sub__(data1))
print("Matrix*Matrix:\n")
print(Matrix(data).__mul__(data1))
print("Matrix*vector:\n")
print(Matrix(data).__rmul__(vec))
print(Matrix(data).__str__())
print(Matrix(data).__repr__())	
