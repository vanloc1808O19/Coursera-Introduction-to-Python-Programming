# we can get a slice of a list using the colon (:)
# format: [start_index : end_index]
# start_index is the index of the first value (included in slice)
# end_index is the index of the last value (not included in slice)

myList = ["a", "b", "c", "d", "e", "f", "g", "h"]

# get elements from index 2 to 4
print(myList[2:5])

# get elements from index 4 to end of myList
print(myList[4:])

# get elements from index 0 to end (the entire list)
print(myList[:])

# get elements from index 0 to -4 (counts from right to left)
print(myList[0:-4])

# another way to copy a list
copyMyList = myList[:]
print(copyMyList)

# test it
print(copyMyList is myList)  # references to the same list? -> False
print(copyMyList == myList)  # same values? -> True

# we can also update list elements by specifying an index or slice
oddNumbers = [2, 4, 6, 8] # wait, there is something wrong here =))) let's make some changes

# update a single element at index 0
oddNumbers[0] = 1
print(oddNumbers)  # [1, 4, 6, 8]

# update multiple elements from index 1 to 3
oddNumbers[1:4] = [3, 5, 7]
print(oddNumbers)  # [1, 3, 5, 7]
