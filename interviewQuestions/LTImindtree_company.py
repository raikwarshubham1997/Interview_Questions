# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]

desireOutput = []
for x in strs:
    anag = []
    for y in strs:
        if y == x:
            anag.append(y)
        else:
            match = 0
            for z in x:  # like x = "tea" t, e, a match it into each object of y
                if z in y:
                    match += 1
            if match == len(x):
                anag.append(y)
    # print(anag)

    if anag in desireOutput:
        pass
    else:
        desireOutput.append(anag)

print("Desire Output : ", desireOutput)



















r"""esult = []

for i in strs:
    print(i)
    anag = []
    for j in strs:
        if j == i:
            anag.append(j)
        else:
            c = 0
            for k in i:
                if k in j:
                    c += 1
                if c == 3:
                    anag.append(j)

    print(anag)

    if anag in result:
        pass
    else:
        result.append(anag)

print("Anagram list : ", result)"""
    































# final = []
# for i in strs:
#     print(i)
#     anag = []
#     # we have to need match i value each value of strs
#     for j in strs:
#         if j == i:
#             anag.append(j)
#         else:
#             c = 0
#             for k in i:
#                 if k in j:
#                     c+=1
#                 if c == 3:
#                     anag.append(j)
#     if anag in final:
#         pass
#     else:
#         final.append(anag)
# print(final)