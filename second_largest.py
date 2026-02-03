nums=[10,45,20,35]
large=second=nums[0]
for n in nums:
    if n>large:
        second=largest
    largest=n
else:
    n>second and n!=largest
    second=n
print("second largest:",second)    