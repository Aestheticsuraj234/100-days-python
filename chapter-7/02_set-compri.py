favourite_chais = ["Masala Chai" , "Green Chai" , "Lemon Chai" , "Spiced Chai" , "Mint Chai" , "iced chai" ,"Masala Chai" , "Green Chai" , ]

unique_chai = {chai for chai in favourite_chais if len(chai) > 5}

print(unique_chai)


recipes = {
    "Masala Chai" :["ginger" , "cardmom" , "clove"],
    "Elaichi Chai":["cardamom" , "milk"],
    "Spicy Chai":["ginger" , "black pepper" , "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)