# Pure vs impure functions
# Recursive functions
# Lambdas or anonymous functions

def pure_chai(cups):
    return cups * 10


total_chai = 0


def impure_chai(cups):
    global total_chai
    total_chai += cups 
    
    
chai_types = ["light" , "Kadak" , "Ginger" ,"Kadak"]    