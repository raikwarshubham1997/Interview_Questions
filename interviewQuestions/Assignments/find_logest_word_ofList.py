"""
Find the list of words that are longer than n from a given list of words
"""
mysent = "The quick brown fox"
n = 3
words = []
spl = mysent.split()
print(spl)

sortest = spl[0]
print(sortest)

for word in spl:
    if len(word) > n:
        # print("This is the word which is greater than n : ", word)
        words.append(word)
    # else:
    #     print("No any greater than of n")



def findLongerWord(n, st):
    words = []
    spl = st.split()
    print(spl)

    sortest = spl[0]
    print(sortest)

    for word in spl:
        if len(word) > n:
            words.append(word)

    
    
    return "This is the word which is greater than n : ", words

n = int(input("Enter the value of n for the find larger then n : "))
string = input("Enter Your Sentance : ")

result = findLongerWord(n, string)

print(result)
