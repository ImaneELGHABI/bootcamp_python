from book import Book
from recipe import Recipe
recipe=Recipe("cookie",3,15,["milk"],"fghjk","dessert")
print(recipe)
book=Book("cookie")
recipe=Recipe("cookie",3,15,["milk"],"fghjk","dessert")
print(recipe)
print(book.creation_time)
print(book.last_update)
book.add_recipe(recipe)
print(book.last_update)
#book.get_recipe_by_name("cookie")
#print(book.get_recipe_by_type("dessert"))
