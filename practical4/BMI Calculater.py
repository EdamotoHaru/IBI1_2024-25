weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
if weight/(height/100)**2 < 18.5:
    a = 'Underweight'
elif weight/(height/100)**2 >= 30:
    a = 'Overweight'
elif 18.5<= weight/(height/100)**2 < 30: 
    a = 'Normal'
print('Your BMI is',weight/(height/100)**2 , 'and you are', a)