# loops intro

a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
# this is inefficient so we need to use a while loop
# this is a while loop
a = 1
while a < 5:
    a += 1
    print(a)

# another loop is the for loop

for i in [
    0,
    1,
    2,
    3,
    4,
]:
    print(i + 6)

print("---")

for i in range(5):
    print(i + 6)

for i in range(3):
    for j in range(3):
        print(i, j)
