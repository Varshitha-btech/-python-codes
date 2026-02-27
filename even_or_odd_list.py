lst=[1,2,3,4,5,6,7,8,9,10]
even_sum=0
odd_sum=0
for n in lst:
    if n%2==0:
        even_sum+=n
    else:
        odd_sum+=n
print(even_sum,odd_sum)