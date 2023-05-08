#List are ordered, changeable and allow for duplicates
list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)
print(type(list1))

list2 = ["A", 1, 2.2, ["B"], [],]
print(list2)

list1[0] = "J"
print(list1)

list1.append("C")
print(list1)

print(list1.index("C"))

list1.reverse()
print(list1)

print(list1.count("C"))
print(list1)

list4 = [0,8,12,72,54,64,21,]
print(list4)

#using sort will sort list in numerical value
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list4 = list1
print(list4)
print(list1)

list5 = list4.copy()
print(list4)
print(list5)
