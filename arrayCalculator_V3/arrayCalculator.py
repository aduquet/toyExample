
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
    
    def popFirst(self, valtoadd):
        self.arr.pop(0,valtoadd)
    
    def popSecondLast(self, valtoadd):
        self.arr.pop(self.getSize() -1, valtoadd)
    
    def poptLast(self, valtoadd):
        self.arr.pop(self.getSize(), valtoadd)
    
    def popByIndex(self, valtoadd, index):
        self.arr.pop(index, valtoadd)    
    
    
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
