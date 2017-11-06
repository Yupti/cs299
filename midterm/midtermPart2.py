def main():
    #set #1
    L1 = [13,3,25,7,21,2,50,2,13,40,34,14,6,16]
    L2 = [1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1]
    print("Test 1")
    Q2(L1,L2)
    print("")
    # set #2
    L1 = [45,21,4,31,2]
    L2 = [1,1,1,1,1]
    print("Test 2")
    Q2(L1,L2)
    print("")
    # set #3
    L1 = [13,3,45]
    L2 = [-1,-1,-1]
    print("Test 3")
    Q2(L1,L2)
    print("")

def Q2(L1, L2):
    if len(L1) != len(L2):
        print("Sizes are not the same!")
    else:
        nextPart(L1, L2)

def nextPart(L1, L2):
    print("Part 1")
    index = 0
    maxNum = 0
    for i in L1:
        if L2[index] == 1:
            if i > maxNum:
                maxNum = i
        index += 1
    print("Max value is:", maxNum)
    print("Part 2")
    newList = []
    for i in zip(L1,L2):
        newList.append(i)
    newList.sort()
    print(newList)
    print("Part 3")
    removeList = []
    for i in newList:
        if i[1] == -1:
            removeList.append(i)
    for j in removeList:
        newList.remove(j)
    print(newList)


if __name__ == "__main__":
    main()
