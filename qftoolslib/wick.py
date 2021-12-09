#!/usr/bin/env python3


from time import time
from collections import Counter

def wickContractions(field_type, fields, mode, output):
    start = time()
    # real scalar field
    if field_type == "rsf":

        if mode == "all":
            wickRealScalarField(fields, output)

        elif mode == "vac":
            print("vac")

        elif mode == "nvac":
            print("nvac")

        else:
            print("error: mode '{}' unknown".format(mode))

    # complex scalar field
    elif field_type == "csf":
        pass

    # else
    else:
        print("error: field type '{}' unknown".format(field_type))

    end = time()
    dt = end - start

    if dt < 1:
        print("process finished in {0:2.2f} ms".format(dt*1000))
    else:
        print("process finished in {0:2.2f} s".format(dt))


def countAllMultiples(res):
    pairedList = []
    for pseudo in range(len(res)):
        pairedList.append([])
    for i in range(len(res)):
        for j in range(0, len(res[i]), 2):
            pairedList[i].append(res[i][j:j+2])

    for item in pairedList:
        item.sort(key=lambda x: ((x[0], len(x[1]), float(x[1]))))


    stringList = []
    for item in pairedList:
        stringList.append("{}".format(item))
    dic = Counter(stringList)
    uniqueResSet = set(stringList)
    uniqueResList = list(uniqueResSet)
    multiplierList = []
    for item in uniqueResList:
        multiplier = dic[item]
        multiplierList.append(multiplier)

    return multiplierList, uniqueResList


def wickRealScalarField(fields, output):
    N = len(fields)

    if N % 2 == 0:

        nums = ''.join(fields)
        #print("nums = ", nums)
        index_list = []
        for i in range(len(fields)):
            index_list.append(i)
        #print("index_list = ", index_list)
        res = pairgroup(index_list)

        for index in range(0, len(res)):
            for index2 in range(0, len(res[index])):
                res[index][index2] = fields[res[index][index2]]

        multiplierList, uniqueResList = countAllMultiples(res)

        if output == "print":
            print("<0|T{}|0> =".format(fields))
            print("")
            for i in range(len(multiplierList)):
                if not i == len(multiplierList) - 1:
                    print("{} x {} +".format(multiplierList[i], uniqueResList[i]))
                else:
                    print("{} x {}".format(multiplierList[i], uniqueResList[i]))

        elif output == "save":
            print("save")
        else:
            print("unknown output-type.")

        return

    else:
        print("<0|T{}|0> = 0".format(fields))


class TupleAndMissingFriends:
    def __init__(self,tuple,friends):
        self.tuple = tuple
        self.friends = friends

    def print(self):
        print("tuple: {0}, missing friends: {1}".format(str(self.tuple), str(self.friends)))


def getStartTuples(index_list):

    startTupleList = []
    for tupleIndex in range(1, len(index_list)):
        startTuple = [index_list[0], index_list[tupleIndex]]
        missingNumsList = []
        for missingTupleIndex in range(1, len(index_list)):
            if not missingTupleIndex == tupleIndex:
                missingNumsList.append(index_list[missingTupleIndex])
        tuple = TupleAndMissingFriends(startTuple, missingNumsList)
        startTupleList.append(tuple)

    return startTupleList



def getCombinationsList(index_list):
    comb = list(it.combinations(index_list, r=2))
    combList = []

    for i in range(0, len(comb)):
        combList.append(list(comb[i]))

    print("comb = ",comb)
    print("combList", combList)
    print("comblist printed")
    return combList


def pairgroup(index_list):
    if len(index_list) == 2:
        return [[index_list[0], index_list[1]]]
    pairedList = []
    startTupleList = getStartTuples(index_list)

    for index in range(0, len(startTupleList)):
        res = pairgroup(startTupleList[index].friends)
        for index2 in range(0, len(res)):
            res2 = res[index2]
            comboList = []
            comboList.extend(startTupleList[index].tuple)
            comboList.extend(res2)
            pairedList.append(comboList)

    return pairedList

    """
    for i in range(0, len(startTupleList)):
        sTuple = startTupleList[i]
        fullCombo = []
        fullCombo.append(sTuple)
        grabNextPair(fullCombo, combList, len(startTupleList))
        print("done for pair ", startTupleList[i])


    print(str(combinedTupleList))
    """


def grabNextPair(currentTuples, remainingTuples, index):
    print("checking for current tuples {0}".format(str(currentTuples)))
    tupleIndex = index
    for i in range(index, len(remainingTuples)):
        if containsIdenticalIndexes(currentTuples, remainingTuples[i]):
            print("skipping, identical index {0}".format(str(remainingTuples[i])))
            continue
        print("appending tuple ", remainingTuples[i])
        currentTuples.append(remainingTuples[i])
        tupleIndex = i
        break

    if tupleIndex < len(remainingTuples) -1:
        print("still got tuples left, keep going with index {0}".format(str(tupleIndex)))
        grabNextPair(currentTuples,remainingTuples,tupleIndex)
    print("done. full pair: ", currentTuples)

    return currentTuples



def containsIdenticalCombos(tupleList, checkTuple):
    for i in range(0, len(tupleList)):
        print("checking tup combo " + str(tupleList[i]))
        if (containsIdenticalIndexes(tupleList[i], checkTuple)):
            return True
    return False


def containsIdenticalIndexes(tupleList, checkTuple):
    for i in range(len(tupleList)):
        if checkTuple[0] in tupleList[i] or checkTuple[1] in tupleList[i]:
            return True
    return False


def hasIdenticalIndexes(baseTuple, checkTuple):
    if baseTuple[0] == checkTuple[0] or baseTuple[0] == checkTuple[1] or baseTuple[1] == checkTuple[0] or baseTuple[1] == checkTuple[1]:
        return True
    return False
