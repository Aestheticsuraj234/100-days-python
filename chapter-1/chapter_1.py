# immutable data types = int, float, string, tuple , boolean , 
sugar_amount = 2
print(f"Initial Sugar Amount: {id(sugar_amount)}")

# Mutable Data Types = list, dict, set
spice_mix = set()

spice_mix.add("cumin")
print(f"Updated Spice Mix: {id(spice_mix)}")


is_boiling = True

spice_count = 5

total_actions = spice_count + is_boiling  # upcasting

print(f"Total Actions: {total_actions}")

# Logical Operations (and , or , not)

# String