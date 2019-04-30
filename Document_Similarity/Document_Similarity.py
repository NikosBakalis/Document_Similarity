from collections import Counter
from itertools import chain
import math

N = int(input("Amount of documents: "))
listsOne = ["Null"] * N
listTwo = list()
dictToList = list()
digitList = list()
resultList = list()
part1 = 0
part2 = 0
part3 = 0
cos = 0

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
    for micro in range(len(listsOne[lists])):
        #        print(listsOne[lists][micro])
        for value in range(len(listsOne[lists][micro])):
            #            print(listsOne[lists][micro][1])
            digitList.append(listsOne[lists][micro][1])
            break

print("\n\n", digitList, "\n")

digitChunks = [digitList[x:x+(int(len(digitList)/N))] for x in range(0, len(digitList), int(len(digitList)/N))]
for allChunks in range(len(digitChunks)):
    print(digitChunks[allChunks], sep="\n")

for allChunks in range(len(digitChunks)):
    for allDigits in range(len(digitChunks[allChunks])):
        print(digitChunks[allChunks][allDigits])
    print("\n")


for i in range(len(digitChunks)):
    for j in range(i + 1, len(digitChunks)):
        for allDigits in range(len(digitChunks[i])):
            print(digitChunks[i][allDigits], digitChunks[j][allDigits])
            part1 = float(part1 + (digitChunks[i][allDigits] * digitChunks[j][allDigits]))
            print("The part1 between list No: ", i + 1, "and list No: ", j + 1, "is: ", part1)
            part2 = float(part2 + (digitChunks[i][allDigits] * digitChunks[i][allDigits]))
            print("The part2 between list No: ", i + 1, "and list No: ", j + 1, "is: ", part2)
            part3 = float(part3 + (digitChunks[j][allDigits] * digitChunks[j][allDigits]))
            print("The part3 between list No: ", i + 1, "and list No: ", j + 1, "is: ", part3)
        cos = float(part1 / (math.sqrt(part2) * math.sqrt(part3)))
        print("The cos between list No: ", i + 1, "and list No: ", j + 1, "is: ", cos)
        resultList.append(i + 1)
        resultList.append(j + 1)
        resultList.append(cos)
        print(resultList)
        part1 = 0
        part2 = 0
        part3 = 0
        cos = 0
        print("\n")

resultChunks = [resultList[x:x+(int(len(resultList)/N))] for x in range(0, len(resultList), int(len(resultList)/N))]
for allResults in range(len(resultChunks)):
    print(resultChunks[allResults], sep="\n")
