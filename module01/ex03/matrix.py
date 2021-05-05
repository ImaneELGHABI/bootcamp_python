class Matrix(object):
	def __init__(self,data):
		if not isinstance(data,list):
			if not isinstance(data,tuple):
				raise ValueError('ERROR')
			elif isinstance(data,tuple):
				if isinstance(data[0],int) and isinstance(data[1],int):
					L=[]
					D=[]
					for i in range(data[1]):
						L.append(0)
					for j in range(data[0]):
						D.append(L)
					self.data=D
				elif isinstance(data[0],list) and isinstance(data[1],tuple):
					if not (isinstance(data[1][0],int) and isinstance(data[1][1],int)):
						raise ValueError('ERROR')
					elif (isinstance(data[1][0],int) and isinstance(data[1][1],int)):
						"""
						lignes=len(data[0])
						colonnes=len(data[0][0])
						shape=(lignes,colonnes)
						L=[]
						D=[]
						for i in range(data[1][1]):
							L.append(0)
						for j in range(data[1][0]):
							D.append(L)
						self.data=D
						self.shape=shape
						"""
						self.data=data[0]
						self.shape=data[1]
		elif isinstance(data,list):
			for i in data:
				if not isinstance(i,list):
					raise ValueError('ERROR')
				elif isinstance(i,list):
					self.data=data
					lignes=len(data)
					colonnes=len(data[0])
					shape=(lignes,colonnes)
					self.shape=shape

	def __add__(self, M):
		if self.shape[0]==len(M[0]):
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					self.data[i][j]+=M[i][j]
		return self.data

	def __radd__(self,scalar):
		for i in range(self.shape[1]):
			for j in range(self.shape[0]):
				self.data[j][i]+=scalar
		return self.data

	def __sub__(self,M):
		if self.shape[0]==len(M[0]):
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					self.data[i][j]-=M[i][j]
		return self.data

	def __rsub__(self,scalar):
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				self.data[i][j]-=scalar
		return self.data


	def __mul__(self, matrix):
		result=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		if self.shape[1]==len(matrix):
			for i in range(self.shape[0]):
				for j in range(len(matrix[0])):
					for k in range(self.shape[1]):
						result[i][j]+=self.data[i][j]*matrix[j][i]
			return result

	def __rmul__(self, vector):
		result=[]
		if self.shape[1]==len(vector):
			for i in range(self.shape[0]):
				s=0
				r=self.data[i]
				for j in range(self.shape[1]):
					s+=r[j]*vector[j]
				result.append(s)
			return result
				
			

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return f"Matrix({str(self)})"
		

data=([[1,2,3],
	[4,5,6],
	[2,4,6]])
#data=(2,3)
data1=[[2,2,2],[2,2,2],[2,2,2]]
vec=[1, 1, 1]
D=Matrix(data)
D1=Matrix(data1)
#print(D)
#print(D1)
#print("Matrix+scalar:\n")
#print(Matrix(data1).__radd__(2))
#print("Matrix+Matrix:\n")
#print(Matrix(data).__add__(data1))
#print("Matrix-scalar:\n")
#print(Matrix(data).__rsub__(2))
#print("Matrix-Matrix:\n")
#print(Matrix(data).__sub__(data1))
#print("Matrix/Matrix:\n")
#print(Matrix(data).__truediv__(data1))
#print("Matrix*Matrix:\n")
#print(Matrix(data).__mul__(data1))
#print("Matrix*vector:\n")
#print(Matrix(data).__rmul__(vec))
print(Matrix(data).__str__())
print(Matrix(data).__repr__())		
