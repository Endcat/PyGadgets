list1 = open('validate1.txt', 'r')
list2 = open('validate2.txt', 'r')

result = open('merge.txt', 'w')

mergeList = {}

while True:
    line = list1.readline()
    if not line:
        break
    num = int(line[:-1])
    mergeList[num] = False

while True:
    line = list2.readline()
    if not line:
        break
    num = int(line[:-1])
    if num in mergeList:
        mergeList[num] = True


for num in mergeList:
    if mergeList[num]:
        result.write(str(num)+'\n')