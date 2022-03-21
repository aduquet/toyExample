from arrayCalculator import *

myArrayA = ArrayCalculator()
myArrayValuesA = [1,2,3,4]
myArrayA.setter(myArrayValuesA)
print('getAll: ', myArrayA.getAll())

myArrayA.insertFirst(53)
print('insertFirst(53): ', myArrayA.getAll())

myArrayA.insertSecondLast(51)
print('insertSecondLast(51): ', myArrayA.getAll())

myArrayA.insertLast(52)
print('insertLast(52): ', myArrayA.getAll())

print('getAll: ', myArrayA.getAll())
print('getFirst: ',myArrayA.getFirst())
print('getSecondLast: ',myArrayA.getSecondLast())
print('getLast: ',myArrayA.getLast())
print('getByIndex (10): ',myArrayA.getByIndex(10))
print('getByIndex(myArrayA.getSize() -1): ',myArrayA.getByIndex(myArrayA.getSize()-1))
print('getAll: ',myArrayA.getByIndex(3))

print('searching(21): ', myArrayA.searching(21))
print('searching(52): ', myArrayA.searching(52))
print('searchingToGetIndex(21): ', myArrayA.searchingToGetIndex(21))
print('searchingToGetIndex(52): ', myArrayA.searchingToGetIndex(52))

print('avg_myArrayA: ', myArrayA.avg())

myArrayC = ArrayCalculator()
print('avg_myArrayC empty array: ', myArrayC.avg(), '\n')


myArrayB = ArrayCalculator()
myArrayValuesB = [4,5,6,7,8,9,10]
myArrayB.setter(myArrayValuesB)
print('ARRAYB: ', myArrayB.getAll())

myArrayB.popFirst()
print('popFirst: ', myArrayB.getAll())

myArrayB.popSecondLast()
print('popSecondLast: ', myArrayB.getAll())

myArrayB.poptLast()
print('poptLast: ', myArrayB.getAll())

#myArrayB.popByElement(2)
#print('popByElement(2): ', myArrayB.getAll())

myArrayB.popByElement(6)
print('popByElement(6): ', myArrayB.getAll())

myArrayB.popByIndex(100)
print('popByIndex(100): ', myArrayB.getAll())

myArrayB.popByIndex(3)
print('popByIndex(3): ', myArrayB.getAll())

myArrayB = ArrayCalculator()
myArrayValuesB = [4,5,6,7]
myArrayB.setter(myArrayValuesB)

myArrayC = ArrayCalculator()
myArrayValuesC = [4,5,6,7]
myArrayC.setter(myArrayValuesB)

print(myArrayA.getAll())
print(myArrayB.getAll())





print(myArrayA.getAll())
print(myArrayB.getAll())

myArrayD = ArrayCalculator()
myArrayA.get(51)
print(myArrayA.getAll())