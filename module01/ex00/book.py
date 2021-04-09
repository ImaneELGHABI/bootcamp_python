import datetime
from recipe import Recipe


class Book:
	def __init__(self, name):
		if not isinstance(name, str):
			raise ValueError("")
	#	if not isinstance(self.recipes_list,dict):
	#		raise ValueError("")
		self.name=name
		self.creation_time=datetime.datetime.now()
		self.last_update=datetime.datetime.now()
		self.recipes_list={"starter":[], "lunch":[], "dessert":[]}

	def get_recipe_by_name(self, name):
		for i in self.recipes_list.values():
			for recipe in i:
				if recipe.name==name:
					return recipe

	def get_recipes_by_types(self, recipe_type):
		if recipe_type in self.recipes_list.keys():
			return self.recipes_list[recipe_type]

	def add_recipe(self, recipe):
		for i in self.recipes_list.keys():
			if recipe.recipe_type==i:
				self.recipes_list[i].append(recipe)
				break

