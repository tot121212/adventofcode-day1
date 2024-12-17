list1 = []
list2 = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sep = line.split("   ")
        list1.append(int(sep[0]))
        list2.append(int(sep[1]))

# take list 2 and find how many instances of list element exist and add to a new list in ascending order
list3 = []
for i in list1:
    list3.append(i * (list2.count(i)))

similarity_score = sum(list3)
print(similarity_score)

#list1.sort(), list2.sort()
#difference_between_list_elements = sum([abs(a-b) for a,b in zip(list1, list2)])
#print(difference_between_list_elements)

