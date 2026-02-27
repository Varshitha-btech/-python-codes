list=[1,3,5,3,7,3,9]
target=3
indices=[]
for i in range(len(list)):
    if list[i] ==target:
        indices.append(i)
print(indices)
