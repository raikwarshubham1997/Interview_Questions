# ls=[]
# for i in range(1,21):
#     if i%2 == 0:
#         ls.append(i)
    
# print(ls)


'''


inp = [{"india": 40, "code": "1001"}, 
        {"pakistan": 20, "code": "1001"}, 
        {"china": 40, "code": "1001"}, 
        {"india": 56, "code": "1002"}, 
        {"pakistan": 14, "code": "1002"}, 
        {"china": 30, "code": "1002"}
        ]

dictt = {}
for data in inp:
    code = data["code"]
    if code not in dictt:
        dictt[code]={"code":"1001"}
    # print(">>>>>>>>>>", dictt)
    for key, value in data.items():
        dictt[code][key]= value
        # print("Mydict>>",dictt)

result = list(dictt.values())

print(result)




# o/p {'india': [40, 56], 'code': ['1001', '1002'], 'pakistan': [20, 14], 'china': [40, 30]}

finaldict = {}
for data in inp:
    for key, value in data.items():
        print(key, value)
        if key not in finaldict:
            finaldict[key]=[]
        if value not in finaldict[key]:
            finaldict[key].append(value)
            print(finaldict)

print(finaldict)
'''


ass={"abhi":"india",
    "Max":"America",
    "Jay":"maxico",
    "Daksh":"india"
    }
a2 = {}
# Find only indian data will output
for i in ass:
    # print(ass[i])
    if ass[i] == "india":
        a2[i]= ass[i]

print(a2)



# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]

final = []
for i in strs:
    print(i)
    anag = []
    # we have to need match i value each value of strs
    for j in strs:
        if j == i:
            anag.append(j)
        else:
            c = 0
            for k in i:
                if k in j:
                    c+=1
                if c == 3:
                    anag.append(j)
    if anag in final:
        pass
    else:
        final.append(anag)
print(final)