class Chai:
    temperature = "hot"
    strength = "Strong"
    
    
cutting = Chai()

print(cutting.temperature)


cutting.temperature = "Mild"

print("Afet changing",cutting.temperature)

print("Direct look into the class0" , Chai.temperature)


del cutting.temperature

print(cutting.temperature)