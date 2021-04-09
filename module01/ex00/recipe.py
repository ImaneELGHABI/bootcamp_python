class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not (isinstance(name,str)):
			raise ValueError("I take only names with type str")
		if not (isinstance(cooking_lvl,int) and cooking_lvl in range(1,6)):
			raise ValueError("I take only int type in range of 1 to 5")
		if not (isinstance(cooking_time,int) and cooking_time>=0):
			raise ValueError("I take only int type with positive numbers")
		if(isinstance(ingredients,list)):
			for i in ingredients:
				if not isinstance(i,str):
					raise ValueError("Only str values")
				
		if not (isinstance(description,str)):
			raise ValueError("Sorry I take only recipe Type")
		if not (isinstance(recipe_type,str) and (recipe_type in ["starter","lunch","dessert"])):
			raise ValueError("Sorry I take only str type")
		self.name=name
		self.cooking_lvl=cooking_lvl
		self.cooking_time=cooking_time
		self.ingredients=ingredients
		self.description=description
		self.recipe_type=recipe_type

	def __str__(self):
		txt=f"name: {self.name}, cooking_lvl: {self.cooking_lvl}, cooking_time: {self.cooking_time}, ingredients: {self.ingredients}, description: {self.description}, recipe_type: {self.recipe_type}"
		return txt

recipe = Recipe("Cake", 3, 30, ["Eggs, flour, milk"], "easy", "dessert")

print(recipe)

