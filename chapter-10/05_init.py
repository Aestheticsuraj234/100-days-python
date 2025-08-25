class ChaiOrder:
    def __init__(self , type_ , size):
        self.type = type_
        self.size = size
        
    def summary(self):
        print(f"This chai cup is {self.size} ml in size") # type: ignore
        
        
        
order = ChaiOrder("ginger" , 100)
print(order.summary())        

