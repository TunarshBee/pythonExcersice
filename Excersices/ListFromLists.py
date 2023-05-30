list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
newList = []
for element1 in list1:
    if element1 % 2 > 0:
        newList.append(element1)
for element2 in list2:
    if element2 % 2 == 0:
        newList.append(element2)
print("Result is: ", newList)