list=[1,2,3,2,4,1,5,3]
result=[]
for num in list:
    if num not in result:
        result.append(num)
print(result)


