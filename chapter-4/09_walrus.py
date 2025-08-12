# value = 13

# remainder = value % 5

# if remainder:
#     print(f"{value} is not divisible by 5")


value = 13

if(remainder := value % 5):
    print(f"{value} is not divisible by 5 remainder is {remainder}")
    
available_sizes = ["small" , "medium" , "large"]

if(requested_size := input("Choose your cup size (small , medium , large): ").lower()):
    if requested_size not in available_sizes:
        print(f"Sorry , We don't have {requested_size} size available")
    else:
        print(f"Your cup is {requested_size}")
        