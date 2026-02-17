size=input("enter size of pizza(s\m\l)?")
bill=0
if size=='S'or size=='s':
    bill=bill+150
    print(f"small pizza cost is{bill}")
elif size=='M'or size=='m':
        bill=bill+250
        print(f"medium pizza cost is {bill}")
else:
        bill=bill+350
        print(f"large pizza cost is {bill}")
add_pepper=input("do you want to add pepper(y/n)?")
if add_pepper=='y' or add_pepper=='Y':
    if size=='S' or size=='s':
        print("pepper cost for small pizza is 30 rupees")
        bill=bill+30
else:
       print("pepper cost for medium/large pizza is 50 rupees")
       bill=bill+50
extra_cheese=input("do you want to add cheese(y/n)?")       
if extra_cheese=='Y'or extra_cheese=='y':
    print("for extra cheese,cost for all types of pizza is 50 rupees ")
    
    bill=bill+50
    print(f"your final bill is{bill}")

