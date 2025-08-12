flavours = ["Ginger" , "Out of Stock" , "Lemon" , "Discontinued" , "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item Found")

print(f"out side of the loop")    