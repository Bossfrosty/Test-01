name = input('Name: ')
age = int(input('Age: '))
weight = float(input('Weight: '))
height = float(input('Height: '))

print("Name:",name)
print("Age:",age)
print("Weight kg:",weight)
print("Height cm:",height)

bmi = weight / height / height * 10000

if bmi <= 18.4: result="underweight"
elif bmi <= 24.9: result="normal"
elif bmi <= 39.9: result="overweight"
elif bmi >= 40.0: result="obese"

print(f"BMI: {bmi:.2f} Result {result}")