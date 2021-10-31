class arrayCalculator:

    def __init__(self):

        self.arr = []

    def sett(self, val1, val2, val3):
        '''F1: in set always make the last element equal ‘0’ '''
        self.arr = [val1, val2, 0]

    def gett(self):
        return self.arr
    
    def avg(self):

        sum = 0
        for i in self.arr:
            sum += i
        
        return sum/len(self.arr)

    def first(self):
        
        return self.arr[0]

    def last(self):

        return self.arr[len(self.arr)-1]
        


