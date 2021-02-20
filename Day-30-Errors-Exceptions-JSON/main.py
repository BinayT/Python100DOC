height = float(input('Your height (in meters): '))
weight = float(input('Your weight (in kg): '))

bmi = weight / height**2
if height > 2.51:
    raise ValueError("Your height exceeds 2.51 meters. Are you taller than Sultan Kosen? :O")
else:
    print(f'Your BMI is of {round(bmi, 2)}')