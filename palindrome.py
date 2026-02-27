n=int(input("enter the number: "))
temp=n
r=0
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
if (temp==rev):
    print("palindrome")
else:
    print("not palindrome")
    
