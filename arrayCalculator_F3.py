class arrayCalculator:

    def __init__(self):

        self.arr = []

    def sett(self, val1, val2, val3):
        self.arr = [val1, val2, val3]

    def gett(self):
        return self.arr
    
    def avg(self):

        sum = 0
        for i in self.arr:
            sum += i
        
        return sum/len(self.arr)

    def first(self):

        '''F3: in first always change ‘0’ to ‘1’ 
        (thus, the index of the array will be wrong)'''
        return self.arr[1]

    def last(self):

        return self.arr[len(self.arr)-1]
        


