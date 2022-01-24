#create a list
#values included not need to be all of the same type
myList = ["tree", "dog", 123, True]

#print the list
print(myList)
#print the length of the list
print(len(myList))
#print the second item of the list
print(myList[1])
#get the fifth item of the list
#this does not exist
#print(myList[4])

#add item to the list
myList.append("Hello abcxyz")
print(myList[4])
print(myList)

#remove item from the list
myList.pop() #remove the last item
print(myList)
myList.pop(1) #remove the second item
print(myList)