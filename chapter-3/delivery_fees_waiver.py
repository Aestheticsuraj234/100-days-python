order_amount = int(input("Enter your order amount: "))

delivery_fees =  0 if order_amount > 300 else 30


print(f"Delivery Fees: {delivery_fees}")
    
    