a=[1,2,3,4,5]
num=int(input("enter your search element: "))
for i in a:
    if(num==i):
        print("element is found")
        break
    else:
        print("not found")
