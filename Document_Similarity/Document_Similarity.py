from collections import Counter
from itertools import chain
import math
import re

N = int(input("Amount of documents: "))
while N <= 1:
    print("Documents must be two or more")
    N = int(input("Amount of documents: "))
listsOne = ["Null"] * N
listTwo = list()
dictToList = list()
digitList = list()
resultList = list()
finalList = list()
topList = list()
printingList = list()
endingList = list()
part1 = 0
part2 = 0
part3 = 0
cos = 0
tempMax = 0

for x in range(N):
    print("Document No.", x + 1)
    document = input("Enter your document here:\n")
    document = re.sub(r'-', ' ', document)
    document = re.sub('[^a-zA-Z0-9 ]', '', document)
    listsOne[x] = document.split()
    while len(listsOne[x]) == 0:
        print("Document can't be empty")
        print("Document No.", x + 1)
        document = input("Enter your document here:\n")
        listsOne[x] = document.split()
    print('Here is the document you entered:\n', *listsOne[x])
    listsOne = [[word.lower() for word in line] for line in listsOne]
    print("\n")

chunks = [listsOne[x:x+1] for x in range(0, len(listsOne), 1)]
listTwo = list(chain.from_iterable(listsOne))
countsAll = Counter(listTwo)

for y in range(len(chunks)):
    countsOne = Counter(listsOne[y])
    countsAll.subtract(countsOne)
    for word in list(countsAll):
        if word in countsAll:
            if word not in countsOne:
                countsOne.update({word: 0})
    for key, value in countsOne.items():
        temp = [key, value]
        dictToList.append(temp)
    dictToList.sort()
    tempForLists = dictToList
    dictToList = listsOne[y]
    listsOne[y] = tempForLists
    dictToList.clear()
    countsAll = countsAll + countsOne

for lists in range(N):
    for micro in range(len(listsOne[lists])):
        for value in range(len(listsOne[lists][micro])):
            digitList.append(listsOne[lists][micro][1])
            break

digitChunks = [digitList[x:x+(int(len(digitList)/N))] for x in range(0, len(digitList), int(len(digitList)/N))]

for i in range(len(digitChunks)):
    for j in range(i + 1, len(digitChunks)):
        for allDigits in range(len(digitChunks[i])):
            part1 = float(part1 + (digitChunks[i][allDigits] * digitChunks[j][allDigits]))
            part2 = float(part2 + (digitChunks[i][allDigits] * digitChunks[i][allDigits]))
            part3 = float(part3 + (digitChunks[j][allDigits] * digitChunks[j][allDigits]))
        cos = float(part1 / (math.sqrt(part2) * math.sqrt(part3)))
        resultList.append(i + 1)
        resultList.append(j + 1)
        resultList.append(cos)
        finalList.append(cos)
        part1 = 0
        part2 = 0
        part3 = 0
        cos = 0

if N == 2:
    print("The similarity between Document No: 1 and Document No: 2 is:", round((finalList[0] * 100), 2), "%")
else:
    resultChunks = [resultList[x:x+3] for x in range(0, len(resultList), 3)]
    for allResults in range(len(resultChunks)):
        for allNumbers in range(2, len(resultChunks[allResults]), 3):
            print("The similarity between Document No:", resultChunks[allResults][0], "and Document No:",
                  resultChunks[allResults][1], "is:", round((resultChunks[allResults][2] * 100), 2), "%")
    print("\n\nEnter a Number between 1 and", int(math.factorial(N) / (math.factorial(2) * math.factorial(N - 2))))
    K = int(input("Find the top similar documents: "))
    while K > math.factorial(N) / (math.factorial(2) * math.factorial(N - 2)):
        print("The number must be between 1 and", int(math.factorial(N) / (math.factorial(2) * math.factorial(N - 2))))
        K = int(input("Find the top similar documents: "))
    for i in range(K):
        for allResults in range(len(finalList)):
            if tempMax < finalList[allResults]:
                tempMax = finalList[allResults]
        finalList.remove(tempMax)
        topList.append(tempMax)
        tempMax = 0
    for i in range(len(topList)):
        for j in range(len(resultChunks)):
            for allNumbers in range(len(resultChunks[j])):
                if topList[i] == resultChunks[j][2]:
                    printingList.append(round((topList[i] * 100), 2))
                    printingList.append(resultChunks[j][0])
                    printingList.append(resultChunks[j][1])
                    break
    printingChunks = [printingList[x:x + 3] for x in range(0, len(printingList), 3)]
    for allNumbers in range(len(printingChunks)):
        if printingChunks[allNumbers] not in endingList:
            endingList.append(printingChunks[allNumbers])
    print("\n\n\n")
    for i in range(K):
        print(i + 1, " The", endingList[i][0], "% similarity, come from document No:",
              endingList[i][1], "and Document No:", endingList[i][2])
