import numpy as np

CONST_K = 137
CONST_INF = -1

def suggestLabelWithKnn(image, data):
    batchX, batchY = data

    copyBatch = []
    optimalArr = [CONST_INF] * CONST_K
    for idx, x in enumerate(batchX):
        copyBatch.append(batchX[idx] - image)

        insertIntoOptimalArr(optimalArr, estimate(copyBatch[idx]))

    return 0


def estimate(image):
    result = 0
    buff = np.reshape(image, -1)
    for pixel in buff:
        result += pixel ** 2

    return result


def insertInto(arr, willBeInsertedIdx, value):
    buff = 0
    for eachIdx, each in enumerate(arr):
        if (eachIdx == willBeInsertedIdx):
            buff = arr[eachIdx]
            arr[eachIdx] = value

        if (eachIdx > willBeInsertedIdx):
            buff2 = arr[eachIdx]
            arr[eachIdx] = buff
            buff = buff2

    return arr



def insertIntoOptimalArr(optimalArr, estimate):

    for idx, eachOptimal in enumerate(optimalArr):
        if idx < CONST_K:
            if optimalArr[idx] > estimate:
                insertInto(optimalArr, idx, estimate)
        else:
            return optimalArr
    pass