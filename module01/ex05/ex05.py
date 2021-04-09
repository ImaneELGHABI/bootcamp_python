class Evaluator:
	def zip_evaluate(words, coefs):
		count=0
		if(isinstance(words,list) and isinstance(coefs,list)):
			if(len(words)==len(coefs)):
				for i,j in zip(words,coefs):
					count+=len(i)*j
				print(count)  
			else:
				print(-1)
		else:
			print(-1)

	def enumerate_evaluate(words, coefs):
		count=0
		if(isinstance(words,list) and isinstance(coefs,list)):
			if(len(words)==len(coefs)):
				for i,j in enumerate(words):
					count+=len(j)*coefs[i]
				print(count)
			else:
				print(-1)
		else:
			print(-1)

words=input()
coefs=input()
Evaluator.zip_evaluate(words,coefs)
Evaluator.enumerate_evaluate(words,coefs)

		 
