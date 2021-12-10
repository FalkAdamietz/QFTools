#!/usr/bin/env python3


from time import time
from collections import Counter
import numpy as np
import csv
import os

def wickContractions(field_type, fields, mode, output):
    """Handles all possible input parameter

    parameter
    ---------
        - field_type : str - rsf, csf
        - fields : list - list of the field-indices
        - mode : str - all, vac, nvac
        - output : str - output-mode
    """

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
    """Takes the result list of Wick contractions as input parameter and
    calculates the combinatorial factor for each contraction.

    parameter
    ---------
        - res : list - list of all Wick contractions

    return
    ------
        - multiplierList : list - list of the combinatorial factors
        - uniqueResList : list - list of the unique contractions
    """

    pairedList = []                                     # Make list out of tuple
    for pseudo in range(len(res)):
        pairedList.append([])
    for i in range(len(res)):
        for j in range(0, len(res[i]), 2):              # grab always two fields
            pairedList[i].append(res[i][j:j+2])

    # sort list since the product of vev's commutes
    for item in pairedList:
        item.sort(key=lambda x: ((x[0], len(x[1]), float(x[1]))))

    # Count all multible entries
    stringList = []
    for item in pairedList:
        stringList.append("{}".format(item))
    dic = Counter(stringList)
    uniqueResSet = set(stringList)                      # due to order
    uniqueResList = list(uniqueResSet)
    multiplierList = []
    for item in uniqueResList:
        multiplier = dic[item]
        multiplierList.append(multiplier)

    multiplierList.reverse()                            # not necessary
    uniqueResList.reverse()                             # not necessary

    return multiplierList, uniqueResList


def wickOutput(multiplierList, uniqueResList, output, fields):
    """Handles the output for Wick contractions.

    parameter
    ---------
        - multiplierList : list - list of the combinatorial factors
        - uniqueResList : list - list of the unique contractions
        - output : str - output-mode
        - field_type : str - rsf, csf
    """

    # print mode
    if output == "print":
        print("<0|T{}|0> =".format(fields))
        print("")
        for i in range(len(multiplierList)):
            if not i == len(multiplierList) - 1:
                print("{} x {} +".format(multiplierList[i], uniqueResList[i]))
            else:
                print("{} x {}".format(multiplierList[i], uniqueResList[i]))

        print("")
        total = np.sum(multiplierList)
        different = len(uniqueResList)
        print("different contractions: {}, total: {}".format(different, total))
        print("")

    # csv mode
    elif output == "csv":
        fileName = ""
        for number in fields:
            fileName += str(number)
        fileName += ".csv"
        doesFileExist = os.path.isfile(fileName)

        # does fileName exist
        if doesFileExist == True:
            overwriteFile = input("File {} already exist. Overwrite it? [y/n]".format(fileName))
            if overwriteFile == "y":
                os.remove(fileName)
                wickOutput(multiplierList, uniqueResList, output, fields)
            elif overwriteFile == "n":
                print("file was not overwritten.")
            else:
                print("unknown input. process stopped.")

        # if fileName does not exist
        else:
            with open(fileName, "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(["{}-point function:".format(len(fields)), "{}".format(fields)])
                writer.writerow(["multiplier", "contractions to two-point propagators"])
                for i in range(len(multiplierList)):
                    writer.writerow(["{}".format(multiplierList[i]), "{}".format(uniqueResList[i])])
                csv_file.close()
            print("File {} successfully created.".format(fileName))
            print("")

    # latex mode
    elif output == "latex":
        fileName = ""
        for number in fields:
            fileName += str(number)
        fileName += ".tex"
        doesFileExist = os.path.isfile(fileName)
        if doesFileExist == True:
            overwriteFile = input("File {} already exist. Overwrite it? [y/n]".format(fileName))
            if overwriteFile == "y":
                os.remove(fileName)
                wickOutput(multiplierList, uniqueResList, output, fields)
            elif overwriteFile == "n":
                print("file was not overwritten.")
            else:
                print("unknown input. process stopped.")

        else:
            with open(fileName, "w") as tex_file:
                tex_file.write("\\begin{align}\n")

                phiList = []
                for i in fields:
                    tex = "\\hat{\\phi}(x_{" + str(i) + "})"
                    phiList.append(tex)

                correlator = "\\langle 0\\vert\\mathcal{T}"
                for phi in phiList:
                    correlator += phi
                correlator += "\\vert 0\\rangle"
                tex_file.write(correlator)
                tex_file.write(" &=")
                string = "{}".format(multiplierList[0])
                string += "\\cdot"
                tex_file.write(string)
                factors = uniqueResList[0]

                # get indices of fields like that since type(factors) == str
                indexList = []
                for char in factors:
                    try:
                        index = int(char)
                        indexList.append(index)
                    except:
                        continue

                for i in range(len(indexList)):
                    # first field in two-point correlator function
                    if i % 2 == 0:
                        string = "\\langle 0\\vert\\mathcal{T}"
                        string += "\\hat{\\phi}(x_{" + str(indexList[i]) + "})"
                    # second field in two-point correlator function
                    else:
                        string += "\\hat{\\phi}(x_{" + str(indexList[i]) + "})"
                        string += "\\vert 0\\rangle"
                        tex_file.write(string)

                tex_file.write("\\\\\n")

                for i in range(1, len(multiplierList)):
                    tex_file.write("&={}\\cdot".format(multiplierList[i]))

                    factors = uniqueResList[i]

                    indexList = []
                    for char in factors:
                        try:
                            index = int(char)
                            indexList.append(index)
                        except:
                            continue

                    for j in range(len(indexList)):
                        # first field in two-point correlator function
                        if j % 2 == 0:
                            string = "\\langle 0\\vert\\mathcal{T}"
                            string += "\\hat{\\phi}(x_{" + str(indexList[j]) + "})"
                        # second field in two-point correlator function
                        else:
                            string += "\\hat{\\phi}(x_{" + str(indexList[j]) + "})"
                            string += "\\vert 0\\rangle"
                            tex_file.write(string)

                    if not i == len(multiplierList) -1:
                        tex_file.write("\\\\\n")

                tex_file.write("\n\\end{align}")

                tex_file.close()
            print("File {} successfully created.".format(fileName))
            print("")

    else:
        print("unknown output-type.")

    return


def wickRealScalarField(fields, output):
    """Initiates the Wick contractions for the real scalar field.

    parameter
    ---------
        - fields : list - list of the field-indices
        - output : str - output-mode
    """

    N = len(fields)

    if N % 2 == 0:

        nums = ''.join(fields)

        index_list = []
        for i in range(len(fields)):
            index_list.append(i)

        res = pairgroup(index_list)

        for index in range(0, len(res)):
            for index2 in range(0, len(res[index])):
                res[index][index2] = fields[res[index][index2]]

        multiplierList, uniqueResList = countAllMultiples(res)

        wickOutput(multiplierList, uniqueResList, output, fields)

    else:
        print("<0|T{}|0> = 0".format(fields))


class TupleAndMissingFriends:
    def __init__(self,tuple,friends):
        self.tuple = tuple
        self.friends = friends

    def print(self):
        print("tuple: {0}, missing friends: {1}".format(str(self.tuple), str(self.friends)))


def getStartTuples(index_list):
    """Creates list for the start tuples of Wick contraction

    parameter
    ---------
        - index_list : list - index list of fields

    return
    ------
        - startTupleList : list - list of the start-tuples
    """

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


def pairgroup(index_list):
    """Find all possible Wick contractions.

    parameter
    --------
        - index_list : list - index list of fields

    return
    ------
        - pairedList : list - Wick contractions
    """
    
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
