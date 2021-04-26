class Vector(object):
	def __init__(self, values):
		try:
			if not isinstance(values, list):
				if not isinstance(values, int):
					if not isinstance(values,tuple):
						raise ValueError('Something wrong')
					elif isinstance(values,tuple):
						values= [float(i) for i in range(values[0],values[1])]
				elif isinstance(values,int):
					values= [float(i) for i in range(values)]
			elif isinstance(values,list):
				for i in values:
					if not isinstance(i,float):
						raise ValueError('Error')
			self.values=values
			self.size=len(self.values)
		except:
			print('Error')

	def __add__(self,L):
		if len(L)==self.size:
			for i in range(self.size):
				self.values[i]+=L[i]
			return self.values
		raise ValueError('ERROR: Different sizes.')

	def __radd__(self,a):
		for i in range(self.size):
			self.values[i]+=a
		return self.values

	def __sub__(self,L):
		if len(L)==self.size:
			for i in range(self.size):
				self.values[i]-=L[i]
			return self.values
		raise ValueError('ERROR: Different sizes')

	def __rsub__(self,a):
		for i in range(self.size):
			self.values[i]-=a
		return self.values

	def __truediv__(self,L):
		if len(L)==self.size:
			for i in range(self.size):
				self.values[i]/=L[i]
			return self.values
		raise ValueError('ERROR: Different sizes')	

	def __rtruediv__(self, a):
		for i in range(self.size):
			self.values/=a
		return self.values

	def __mul__(self, L):
		if len(L)==self.size:
			for i in range(self.size):
				self.values[i]*=L[i]
			return self.values
		raise ValueError('ERROR: Different sizes')


	def __rmul__(self,a):
		for i in range(self.size):
			self.values[i]*=a
		return self.values

	def __str__(self):
		return str(self.values)

	def __repr__(self):
		return f"Vector({str(self)})"
