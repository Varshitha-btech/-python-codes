height = float(input("Enter height in feet: "))

if height >= 3:
    print("You can ride")

    age = int(input("Enter age: "))

    if age <= 12:
        bill = 150
        print(f"Pay {bill} rupees")

    elif age <= 18:
        print("Pay 250 rupees")

    else:
        print("Pay 500 rupees")

else:
    print("You cannot ride")

print("Thank you...!")
