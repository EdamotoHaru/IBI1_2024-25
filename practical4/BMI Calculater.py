# BMI Calculator
# First, ask the user for their weight in kg and height in cm (cm is normally used)
# Then, calculate the BMI using the formula
# BMI = weight(kg) / height(m)^2
# Finally, print the BMI and the corresponding weight category
# If the BMI is in the range of 18.5 to 30, print "Normal"
# If the BMI is less than 18.5, print "Underweight"
# If the BMI is greater than 30, print "Overweight"
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
if weight/(height/100)**2 < 18.5:
    a = 'Underweight'
elif weight/(height/100)**2 >= 30:
    a = 'Overweight'
elif 18.5<= weight/(height/100)**2 < 30: 
    a = 'Normal'
print('Your BMI is',weight/(height/100)**2 , 'and you are', a)