from arrayCalculator import *

myArrayA = ArrayCalculator()
myArrayValuesA = [1,2,3,4]
myArrayA.setter(myArrayValuesA)

myArrayB = ArrayCalculator()
myArrayValuesB = [4,5,6,7]
myArrayB.setter(myArrayValuesB)

print(myArrayA.getter())
print(myArrayB.getter())


myArrayA.insert(5)
myArrayB.insert(8)

print(myArrayA.getter())
print(myArrayB.getter())