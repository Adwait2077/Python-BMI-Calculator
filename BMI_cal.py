print("This is Body Mass Index Calculator")
name = str(input("Please enter your name: "))
print()
print("Hello" + " " + name +"," + " Welcome to Body Mass Index Calculator!!!")
print()
print("To calculate your BMI we will require your height and weight measurements ")

# 1st input for height
height = float(input("Please enter your height in meters :\n "))
print("The height entered is " + str(height) + " meters.")
print()
# 2nd input for weight
weight = int(input("Enter your weight in kilograms:\n "))
print("The weight entered is " + str(weight) + " kilograms.")
calculation = (weight / height ** 2)
BMI = int(calculation)
print()
print("Your Body Mass Index is " ,BMI)

if BMI < 18.5:
  print("You are underweight!!")
elif BMI < 25:
  print("You are Healthy!!")
elif BMI < 30:
  print("You are overweight!!")
else:
  print("You are Obese!!")