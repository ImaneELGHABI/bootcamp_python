cookbook = dict(
        sandwich = {
            'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
            'meal' : "lunch",
            'prep_time' : 10
        },
        cake = {
            'ingredients' : ["flour", "sugar", "eggs"],
            'meal' : "dessert",
            'prep_time' : 60
        },
        salad = {
            'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
            'meal' : "lunch",
            'prep_time' : 15
        })

def aff_recipe(name) :
    if name in cookbook :
        print("\nRecipe for {}:\nIngredients list: {}\nTo be eaten for {}.\nTakes {} minutes of cooking.\n".format(name, cookbook[name]['ingredients'],
            cookbook[name]['meal'], cookbook[name]['prep_time']))
    else :
        print("\nrecipe not found...\n")

def add_new_recipe(name, ingredients, meal, prep_time) :
    cookbook[name] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def del_recipe(name) :
    if name in cookbook :
        cookbook.pop(name)
        print("\n" + name.capitalize() + " has been deleted!\n")
    else :
        print("recipe not found...\n")


def all_recipe() :
    print("\nrecipes :")
    for recipe in cookbook :
        print("- " + recipe)
    print()

while True :
    action = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ")

    if (action == '1') :
        recipe = input("\nPlease enter the recipe name:\n>> ")
        ingredients = input("\nPlease enter the recipe ingredients (separated by spaces):\n>> ").split()
        meal = input("\nPlease enter the meal type:\n>> ")
        prep_time = input("\nPlease enter the preparation time:\n>> ")
        add_new_recipe(recipe, ingredients, meal, prep_time)
        print()

    elif action == '2':
        recipe = input("\nPlease enter the recipe's name to delete:\n>> " )
        del_recipe(recipe)
    elif action == '3':
        recipe = input("\nPlease enter the recipe's name to get its details:\n>> ")
        aff_recipe(recipe)
    elif action == '4':
        all_recipe()
    elif action == '5':
        print("\nCookbook closed.")
        exit()
    else :
        print("\nError: unknown instuction...\n")
