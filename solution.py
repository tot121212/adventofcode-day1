list1 = []
list2 = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sep = line.split("   ")
        list1.append(int(sep[0]))
        list2.append(int(sep[1]))

list1.sort(), list2.sort()
difference_between_list_elements = sum([abs(a-b) for a,b in zip(list1, list2)])
print(difference_between_list_elements)