def chai_customer():
    print("Welcome ! what chai do you want ?")
    
    order = yield

    while True:
        print(f"Preparing {order} chai")
        order = yield
        
stall = chai_customer()

next(stall) # starts the generator

stall.send("Masala Chai")        