a=[10,20,30]
large=a[0]
small=a[0]
for i in a:
     if i>large:
         large=i
     if i<small:
        small=i
print(large)
print(small)
