# List of lambda functions
conversions = [
    lambda t: t * 1000,         
    lambda kg: kg * 1000,          
    lambda g: g * 1000,            
    lambda mg: mg / 453592.37      
]

# Input from user (in tonnes)
tonnes = float(input("Enter weight in tonnes: "))

# Perform conversions step by step
kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

# Output
print("Weight in kilograms:", kg)
print("Weight in grams:", gm)
print("Weight in milligrams:", mg)
print("Weight in pounds:", lbs)
