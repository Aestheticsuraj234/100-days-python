menu = [
    "Masala chai" , 
    "Green chai" , 
    "Lemon chai" , 
    "Spiced chai",
    "Mint chai",
    "iced chai",
    "iced masala chai",
    "iced green chai",
    "iced lemon chai",
    "iced spiced chai",
    "iced mint chai"
]


iced_tea = [tea for tea in menu if "iced" in tea]
print(iced_tea)