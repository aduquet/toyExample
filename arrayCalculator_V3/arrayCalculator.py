class ArrayCalculator:
    
    def __init__(self):
        self.arr = []

    def setter(self, val):
        if type(val) == list:
            for i in val:
                self.arr.append(i)
        
        else:
            self.arr.append(val)

    def getter(self):
        return self.arr
    
    def insert(self, valtoadd):
        self.arr.append(valtoadd)
    
    def searching(self, valtosearch):
        if valtosearch in self.arr:
            return True
        else:
            return False
        
    def getIndexSearch(self, valtosearch):
        self.arr.append(valtoadd)
        
    def avg(self):
        sum = 0
        for i in self.arr:
            sum += i      
        return sum/len(self.arr)

    def getFirst(self):
        return self.arr[0]

    def last(self):
        return self.arr[self.arr.getSize() -1] 
    
    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.arr)
