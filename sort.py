def sort_dictionary(dict):
    dictlist=list(dict.items())
    l=len(dictlist)
    finalListofTup = []
    for i in range(l - 1):
        for j in range(i + 1, l):
            if (dictlist[i][1] > dictlist[j][1]):
                t = dictlist[i]
                dictlist[i] = dictlist[j]
                dictlist[j]=t
        for a, b, in dictlist:
            finalListofTup.append((a, b[0]))
        return finalListofTup