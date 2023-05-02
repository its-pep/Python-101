#Tuples store multiple items in a single variable. 
#These are immutable and can't be changed.
#Use when the data you're working with is fixed and it's not going to change. 
tuple_fruits = ("pineapple", "banana", "apple")
print(tuple_fruits)
print(type(tuple_fruits))

tuple_numbers = (4, 21, 8)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_repeat = ('Combine' ,) * 4
print(tuple_repeat)
print(type(tuple_repeat))

mixed_tuple = ("A", 1, ("A",1))
print(mixed_tuple)
print(type(mixed_tuple))

tuple_combined = tuple_fruits + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))