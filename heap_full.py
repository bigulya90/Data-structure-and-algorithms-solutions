def findMin(heapArr, i, firstChildLoc, secondChildLoc):
    a = heapArr[i]
    b = heapArr[firstChildLoc]
    c = heapArr[secondChildLoc]
    return i if ((a < b) and (a < c)) else firstChildLoc if (b < c) else secondChildLoc


def prelocateUp(heapArr):
    l = len(heapArr)
    i = l - 1
    while True:
        parentLoc = (i + 1) / 2 - 1
        if parentLoc >= 0:
            if heapArr[parentLoc] > heapArr[i]:
                temp = heapArr[parentLoc]
                heapArr[parentLoc] = heapArr[i]
                heapArr[i] = temp
        else:
            break
        i = parentLoc
    return heapArr


def prelocateDown(heapArr):
    l = len(heapArr)
    i = 0

    while True:
        firstChildLoc = 2 * (i + 1) - 1
        secondChildLoc = 2 * (i + 1)
        if (firstChildLoc > l - 1):
            break

        elif (secondChildLoc > l - 1):
            if heapArr[i] > heapArr[firstChildLoc]:
                temp = heapArr[i]
                heapArr[i] = heapArr[firstChildLoc]
                heapArr[firstChildLoc] = temp
            break

        else:
            minLoc = findMin(heapArr, i, firstChildLoc, secondChildLoc)
            if minLoc != i:
                temp = heapArr[i]
                heapArr[i] = heapArr[minLoc]
                heapArr[minLoc] = temp
                i = minLoc
            else:
                break
    return heapArr


def heapify(heapArr, op):
    if op == 1:
        heapArr = prelocateUp(heapArr)
    else:
        heapArr = prelocateDown(heapArr)
    return heapArr


def insertHeap(heapArr, num):
    heapArr.append(num)
    heapArr = heapify(heapArr, 1)
    return heapArr


def getMin(heapArr):
    ele = heapArr[0]
    heapArr[0] = heapArr[-1]
    heapArr.pop(-1)
    heapArr = heapify(heapArr, 2)
    return ele, heapArr


a = [5, 4, 8, 2, 6]
heapArr = []
for i in xrange(0, len(a)):
    heapArr = insertHeap(heapArr, a[i])

# No
sortedArr = []
for i in xrange(0, len(a)):
    [ele, heapArr] = getMin(heapArr)
    sortedArr.append(ele)
print sortedArr