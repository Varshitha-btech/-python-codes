list=[1,2,3,4,5]
k=4
n=len(list)
k=k%n
end_list=list[:-k]
first_list=list[-k:]
print(first_list+end_list)
