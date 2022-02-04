# create a set with curly braces {}
fruit = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(type(fruit))  # <class 'set'>
print(fruit)  # {'pear', 'banana', 'apple', 'orange'}

# create a set from a string or a list using built-in set function
a = "aivnskjvnaklv"
aSet = set(a)
print(aSet)

b = [1, 2, 3, 4, 4, 2, 1, 3, 5]
bSet = set(b)
print(bSet)

# NOTE: an empty list cannot be written as {}
# instead, we can use the set() function
empty = set()
print(empty)

# iterate over a set
for i in aSet:
    print(i, end = " ")
print("")

# add an element to a set
aSet.add("c")
print(aSet)

# remove an element from a set
bSet.remove(4)
print(bSet)