# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child3"]["name"])

'''
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

newls = {}
let = 0
lst = []

for data in people:
    rs = int(people[data]["age"])
    lst.append((data, rs))
    
for srt in range(0, len(lst)):
    # print(srt)
    for j in range(srt+1, len(lst)):
        if lst[srt] >= lst[j]:
            lst[srt],lst[j] =lst[j],lst[srt]



# for data in people:
#     rs = people[data]["age"] 
#     let += int(rs)

# for i in lst:
#     for j in people:
#         if i == people[j]["age"]:
#             print("KKKKKKK",newls[j])
#             newls[j] = people[j]

newls = {}
for person_id, age in lst:
    newls[person_id] = people[person_id]

# Print the sorted people
for person_id, person_info in newls.items():
    print(f"ID: {person_id}, Name: {person_info['name']}, Age: {person_info['age']}, Sex: {person_info['sex']}")     
    
    
# print(">>>>>",newls)
# print(">>>>>",lst)

'''


'''
#  make a dictionary of this
var = [[1,1],[2,4],[3,9],[4,16]]

blkdict = {}

for i in var:
    blkdict[i[0]] = i[1]

print(blkdict)

'''


people = {
    1: {'name': 'John', 'age': '27', 'sex': 'Male'},
    2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
    3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
    4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
}

# Convert ages to integers and create a list of tuples (id, person)
lst = []
for data in people:
    age = int(people[data]["age"])  # Convert age to integer for sorting
    lst.append((data, age))  # Store the ID and corresponding age
print(lst)
# Sort the list based on age
lst.sort(key=lambda x: x[1])  # Sort by the second element (age)
for srt in range(0, len(lst)):
    # print(srt)
    for j in range(srt+1, len(lst)):
        if lst[srt][] >= lst[j]:
            lst[srt],lst[j] =lst[j],lst[srt]

print("after sort", lst)
# Create a new dictionary based on the sorted list
newls = {}
for person_id, age in lst:
    newls[person_id] = people[person_id]

# Print the sorted people
for person_id, person_info in newls.items():
    print(f"ID: {person_id}, Name: {person_info['name']}, Age: {person_info['age']}, Sex: {person_info['sex']}")
