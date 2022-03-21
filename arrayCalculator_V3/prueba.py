from arrayCalculator import *

myArrayA = ArrayCalculator()
myArrayValuesA = [1,2,3,4]
myArrayA.setter(myArrayValuesA)

myArrayB = ArrayCalculator()
myArrayValuesB = [4,5,6,7]
myArrayB.setter(myArrayValuesB)

myArrayC = ArrayCalculator()
myArrayValuesC = [4,5,6,7]
myArrayC.setter(myArrayValuesB)

print(myArrayA.getter())
print(myArrayB.getter())

myArrayA.insertSecondLast(51)
myArrayA.insertLast(52)
myArrayA.insertFirst(53)

print(myArrayA.getIndexSearch(153))
print(myArrayA.getter())
print(myArrayB.getter())