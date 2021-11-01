class arrayCalculator:

    def __init__(self):

        self.arr = []

    def sett(self, val1, val2, val3):
        self.arr = [val1, val2, val3]

    def gett(self):
        '''F2: in get always print ‘0’ for the last element, i.e., x-x-0'''
        aux = self.arr
        aux[2] = 0
        return aux
    
    def avg(self):

        sum = 0
        for i in self.arr:
            sum += i
        
        return sum/len(self.arr)

    def first(self):
        
        return self.arr[0]

    def last(self):

        return self.arr[len(self.arr)-1]
        


