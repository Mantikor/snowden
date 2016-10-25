import sys

if len(sys.argv) == 2: #check input file
    inFile = sys.argv[1]
else:
    print('no valid file name...')
    sys.exit()

testStr = open(inFile).read() #read data to single string
testList = [testStr[i] for i in range(len(testStr))] #convert string to list for best perfomance and low memory use
k = 0
while k < (len(testList) - 1):
    if testList[k] == testList[k + 1]: #checking pair of symbols
        testList.pop(k) #del first element of double
        testList.pop(k) #del second elemrnt (it comes first place)
        if k != 0: #if remove two symbols, shift back to check previous
            k -= 1
        continue
    else:
        k += 1 #if symbols not equal go to next

resStr = ''.join(testList) #list to string

print(resStr)
