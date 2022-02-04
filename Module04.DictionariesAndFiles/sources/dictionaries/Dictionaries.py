# create a dictionary
person = {"name": "Zed", "age": 39, "height": 6 * 12 + 2}
print(type(person))  # <class 'dict'>
print(person)  # {'name': 'Zed', 'age': 39, 'height': 74}

# get the value of a key
# using the brackets []
print(person["name"])
# using the get() method
print(person.get("name"))

# the get() method is good, in case the key does not exist
# print(person["state"]) -> KeyError
print(person.get("state"))  # output: None
# this will return the default NA if the key does not exist
print(person.get("state", "NA"))

# update a dictionary
person["name"] = "Tristana"  # update the name
person["age"] += 2  # increase the age
person["college"] = True  # add value with key "ollege"
person["city"] = "Ho Chi Minh"  # add value with key "city"
person["state"] = "Married"  # add value with key "state"
print(person)

# check if a key exists
print("college" in person)

# delete elements using del keyword
del person["college"]
print(person)

# dictionaries can include other dictionaries or lists as values
person["siblings"] = ["Teemo"]
person["siblings"].append("Veigar")
print(person)

# we can update the key:value pairs from one dictionary to another using the built-in dictionary "update" method
personAttributes = {"degree": "Master", "children": 2}
person.update(personAttributes)
print(person)
