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
		c = [[0 for i in range(self.shape[0])] for k in range(len(matrix[0]))]
		if self.shape[1]!=len(matrix):
			raise ValueError("The matrices have different len")
		elif self.shape[1]==len(matrix):
			for i in range(self.shape[0]):
				for k in range(len(matrix[0])):
					for j in range(self.shape[1]):
						c[i][k]+=self.data[i][j]*matrix[j][k]
			return c
			
			

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
			
