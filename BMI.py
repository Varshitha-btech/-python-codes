weight=int(input("enter weight in kilograms: "))
height=float(input("enter height in meters: "))
BMI=weight/(height)**2
if (BMI<18.5):
    print(f" {BMI: .2f} under weight")
elif(BMI<25):
    print(f" {BMI: .2f} Normal weight")
elif(BMI<30):
    print(f" {BMI: .2f} Over weight")
elif(BMI<35):
    print(f" {BMI: .2f} obese")
else:
    print("consult a doctor immediately")