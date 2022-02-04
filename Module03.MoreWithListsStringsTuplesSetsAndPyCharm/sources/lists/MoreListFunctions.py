ls1 = [2, 3, 4]
ls2 = [7, 8, 9]

# similar to adding lists, except it will actually update ls1
# and append the values of ls2 to the end of ls1
ls1.extend(ls2)

# iterate over the elements of updated ls1 to see it's been updated
for l in ls1:
    print(l)
