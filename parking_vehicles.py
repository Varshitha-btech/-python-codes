v=input("enter vehicle type(b/c/t):")
hours=int(input("enter no.of hours: "))
if(v=='b' or v=='t'):
    charge=20*hours
    print("parking charge:",charge)
elif(v=='c'):
    charge=15*hours
    print("parking charge:",charge)
elif(v=='w'):
    charge=10*hours
    print("parking charge:",charge)
else:
    print("invalid vehicle type")

