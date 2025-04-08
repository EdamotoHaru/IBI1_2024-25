weight = float(input("Enter your weight in kg: "))
age = int(input("Enter your age in years: "))
type = input("Enter the type of drug (120mg/5ml & 250mg/5ml) using 1 or 2: ")
if 0 < age < 18:
    dosage_per_kg = 15 # Dosage for children
if 18 <= age:
    dosage_per_kg = 25 # Dosage for adults
def dosage_calculator(weight, dosage_per_kg):
    if 10 < weight < 200: # I have a body weight larger than 100kg when I was 18 so I set the limit to 200
        # Calculate the dosage based on weight and age
        dosage = weight * dosage_per_kg
        return dosage
    else:
        print("Invalid weight. Please enter a weight between 10 and 200 kg.")
        return None
dosage = dosage_calculator(weight, dosage_per_kg)
def Volumn_calculator(dosage):
    if type == "1":
        volume = dosage / 120 * 5
    elif type == "2":
        volume = dosage / 250
    else:
        print("Invalid drug type. Please enter '1' or '2'.")
        return None
    
    return volume
if dosage is not None:
    volume = Volumn_calculator(dosage)
    if volume is not None:
        print(f"The dosage for a {weight} kg person of age {age} is {dosage:.2f} mg, which is equivalent to {volume:.2f} ml of the drug.")

   