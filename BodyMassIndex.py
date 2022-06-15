height = float(input("Please,Enter your height in cm:"))
weight = float(input("Please,Enter your weight in kq:"))

BIM = weight / (height / 100) ** 2

print(f"Your body index is {BIM}")

if BIM <= 18.5:
    print('You are underweight')
elif BIM <= 24.9:
    print('Awesome.you are healthy')
elif BIM <= 29.9:
    print("You are overweight!!!")
else:
    print('You are obese :(')

