staff = [("amit" , 16) , ("ram" , 18) , ("shyam" , 20) , ("gita" , 22)]


for name , age in staff:
    if age >= 18:
        print(f"Hello {name} , You are eligible for voting")
        break
else:
    print(f" You are not eligible for voting")
        