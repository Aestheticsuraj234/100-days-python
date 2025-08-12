chai = "Ginger chai"


def prepare_chai(order):
    print("Preparing" , order)

prepare_chai(chai)


def make_chai(tea , milk , sugar):
    print(tea , milk , sugar)
    
make_chai("black" , "milk" , "sugar")

make_chai(tea="black" , milk="milk" , sugar="sugar")
def special_chai(*ingredients , **extras):
    print("Ingredients: " , ingredients)
    print("Extras: " , extras)
    

special_chai("Cinnamon" , "Cardmom" , sweetener="Sugar" , milk="Milk" , water="Water")    