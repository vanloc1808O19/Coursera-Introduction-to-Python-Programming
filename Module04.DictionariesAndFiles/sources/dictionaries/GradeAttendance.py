# create a dictionary for each student

tristana = {
    "name": "Tristana",
    "grades": [100, 80, 67, 100, 90, 100],
    "attendances": [True, True, True, True, True, True]
}

teemo = {
    "name": "Teemo",
    "grades": [0, 90, 100, 0, 50, 89],
    "attendances": [False, True, True, False, True, True]
}

poppy = {
    "name": "Poppy",
    "grades": [90, 0, 90, 90, 90, 90],
    "attendances": [True, False, True, True, True, True]
}

# add each student to a dictionary using a unique student ID
students = {"1": tristana, "2": teemo, "3": poppy}
print(students)

# get the number of students
print(len(students))

# get all student IDs
print(students.keys())

# we can sort the dictionary
print(sorted(students.keys()))

# we can also get a key by iterating over a dictionary itself
for s in students:
    print("Key:", s)

# get Tristana's attendances
tris = students["1"]
print(tris["attendances"])

# get Teemo's grades
tee = students["2"]
print(tee["grades"])

# use the built-in items method to get all key:value pairs for a dictionary
pop = students.get("3")
it = pop.items()
for key, val in it:
    print(key, val)

# get the average student grade for all assignments
grades = []
its = students.items()
for key, val in its:
    for g in val["grades"]:
        grades.append(g)
    print(key, val)

avg = round(sum(grades) / len(grades))
print(avg)
