class arrayCalculator:

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

    def first(self):
        return self.arr[0]

    def last(self):
        '''F4: in last always change ‘2’ to ‘0’ 
        (thus, the index of the array will be wrong)'''
        return self.arr[0]
