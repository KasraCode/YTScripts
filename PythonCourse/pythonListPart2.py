# List Slicing --------------------
#          
names = ["kasra", "reza", "ali", "mohammad","kasra"]
#          0         1      2 |        3
# Wrong way--------------
# students = []
# students.append(names[0])
# students.append(names[1])
# students.append(names[2])
# print(students)
#---------------------
students = names[0:3]
# print(names[-2])
students = names[1:3]
# print(students)
students = names[1:]
# print(students)



# Other list functions--------------
studentsAge = [13,12,15,17,16]
    # extend()
names.extend(studentsAge)
# print(names)
    # clear()

# names.clear()
# print(names)

    # index()
# print(names.index("kasra"))
    # count()
# print(names.count("kasra"))
    # sort()
# studentsAge.sort(reverse=True)
# print(studentsAge)
    # reverse()
# names.reverse()
# print(names)
    # copy()
newNames = []
newNames = names.copy()
print(newNames)
