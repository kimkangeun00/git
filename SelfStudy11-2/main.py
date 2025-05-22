inFp = None
inList, inStr = [], ""

inFp = open("C:\\파이썬\\git\\piletest\\test.txt", "r")

inList = inFp.readlines()
for i in inList:
    print("%d : %s (i+1, inList)", end = "")

inFp.close()