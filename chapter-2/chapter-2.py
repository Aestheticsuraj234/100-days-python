masala_spices = ("cardamom" , "cloves" , "cinnamon");


(spice1 , spice2 , spice3) = masala_spices


print(f"Main masala spices: {spice1} , {spice2} , {spice3}")

# in works with tuples

ingredients = ["water" , "milk" , "black tea"]

ingredients.append("sugar")

print(f"INgredients are: {ingredients}")

ingredients.remove("water")

print(f"ingredients are: {ingredients}")



spice_options = ['ginger' , 'cardamom']

chai_ingredients = ['water' , 'milk']

chai_ingredients.extend(spice_options)

chai_ingredients.insert(2 , "black tea")



last_added = chai_ingredients.pop()

print(last_added)
chai_ingredients.reverse()
print(chai_ingredients)

# Set in python

essential_spices = {"cardamom" , "ginger" , "cinnamon"}
optional_spices = {"cloves" , "ginger" , "black pepper"}

# Union
all_spices = essential_spices | optional_spices
print(f"All spices:{all_spices}")

# Intersection
common_spices = essential_spices & optional_spices

print(f"common spices: {common_spices}")


only_in_essential = essential_spices - optional_spices

print(f"Only essential spices:{only_in_essential}")