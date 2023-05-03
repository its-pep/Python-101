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