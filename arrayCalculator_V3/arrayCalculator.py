class ArrayCalculator:
    
    def __init__(self):
        self.arr = []

    def setter(self, val1, val2, val3):
        self.arr = [val1, val2, val3]

    def getter(self):
        return self.arr
    
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
        if len(len(self.arr)) == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.arr)
