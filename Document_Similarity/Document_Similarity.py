from collections import Counter
from itertools import chain

N = int(input("Amount of documents: "))
listsOne = ["Null"] * N
listTwo = list()
dictToList = list()

for x in range(N):
    print("Document No.", x + 1)
    document = input("Enter your document here:\n")
    listsOne[x] = document.split()
    print('Here is the document you entered:\n', *listsOne[x])
    print("\n")

print(*listsOne, "\n\n")

chunks = [listsOne[x:x+1] for x in range(0, len(listsOne), 1)]

listTwo = list(chain.from_iterable(listsOne))
print(listTwo)
countsAll = Counter(listTwo)
print(countsAll, "\n")

print("\n\n\n")

for y in range(len(chunks)):
    print(listsOne[y])

    for word in range(len(listsOne[y])):
        print(listsOne[y][word])

    countsOne = Counter(listsOne[y])
    print(countsOne)

    countsAll.subtract(countsOne)
    print(countsAll, "\n")
    for word in list(countsAll):
        if word in countsAll:
            if word not in countsOne:
                print(word)
                countsOne.update({word: 0})

    print(countsOne, "\n")

    for key, value in countsOne.items():
        temp = [key, value]
        dictToList.append(temp)

    dictToList.sort()
    print("\n\n", dictToList, "\n\n")
    tempForLists = dictToList
    dictToList = listsOne[y]
    listsOne[y] = tempForLists
    dictToList.clear()

    countsAll = countsAll + countsOne

for lists in range(N):
    print(listsOne[lists], sep="\n")
