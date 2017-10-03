wordList = ['hello','world','my','name','is','Anna']
newList = []


for data in wordList:
    for i in range(0,len(data)):
        if 'o' == data[i]:
            newList.append(data)

print(newList)







### SHORT METHOD ###

# for data in wordList:
#     if 'o' in data:
#         newList.append(data)

# print(newList)