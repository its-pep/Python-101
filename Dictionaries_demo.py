#Python dictionaries are a way to store a collection of key-value pairs. They are used to quickly access and retrieve values based on their associated keys.

#In Python, dictionaries are defined using curly braces {} and key-value pairs are separated by colons :. Here's the basic syntax for creating a dictionary:my_dict = {key1: value1, key2: value2, key3: value3}

dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["b"])

print(dict1.keys())
print(dict1.values())
print(dict1.items())