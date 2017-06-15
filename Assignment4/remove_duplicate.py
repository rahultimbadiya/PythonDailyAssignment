lst = [1,2,2,4,55,55,6,1,3,4,3,11,12,6]
new_lst = []

#one approach using for loop
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
    else:
        continue

print("The list after removing duplicates is:",new_lst)

#Another approach convert list into set that only contain unique elements
a = set(lst)
print("Using another approach:",list(a))
