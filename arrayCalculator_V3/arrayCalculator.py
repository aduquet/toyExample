
from msilib.schema import Error


class ArrayCalculator:
    
    #Create the array
    def __init__(self):
        self.arr = []

    def setter(self, val):
        if type(val) == list:
            for i in val:
                self.arr.append(i)

        else:
            self.arr.append(val)
    
    def insertFirst(self, valtoadd):
        self.arr.insert(0,valtoadd)
    
    def insertSecondLast(self, valtoadd):
        self.arr.insert(self.getSize() -1, valtoadd)
    
    def insertLast(self, valtoadd):
        self.arr.insert(self.getSize(), valtoadd)
    
    def insertByIndex(self, valtoadd, index):
        self.arr.insert(index, valtoadd)
    
    def popFirst(self):
        try:
            self.arr.pop(0)
        except ValueError:
            pass

    def popSecondLast(self):
        try:
            self.arr.pop(self.getSize() -1)
        except ValueError:
            pass
        
    def poptLast(self):
        try:
            self.arr.pop(self.getSize())
        except ValueError:
            pass
    
    def popByIndex(self, index):
        try:
            self.arr.pop(index)
        except ValueError:
            pass
    
    def popByElement(self, val):
        try:
            elementIndex = self.getIndexSearch(val)
            self.arr.pop(elementIndex)
        except ValueError:
            pass
    
    def getter(self):
        return self.arr
           
    def searching(self, valtosearch):
        if self.isEmpty() == False:
            if valtosearch in self.arr:
                return True
            else:
                return False
        else:
            return ('error! the array is empty or the number is not in the array')
        
    def getIndexSearch(self, valtosearch):
        if self.isEmpty() == False and self.searching(valtosearch) == True:
            return self.arr.index(valtosearch)
        else:
            return ('error! the array is empty or the number is not in the array')
        
    def avg(self):
        
        if self.isEmpty() == False:
            sum = 0
            for i in self.arr:
                sum += i      
            return sum/len(self.arr)
        else:
            return ('error! the array is empty')

    def getFirst(self):
        return self.arr[0]
    
    def getSecondLast(self):
        return self.arr[self.getSize() -1]
    
    def getLast(self):
        return self.arr[self.getSize()]
    
    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.arr)
