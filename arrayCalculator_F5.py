class arrayCalculator:

    def __init__(self):
        self.arr = []

    def sett(self, val1, val2, val3):
        self.arr = [val1, val2, val3]

    def gett(self):
        return self.arr
    
    def avg(self):
        '''F5: in avg always change ‘0’ to ‘1’ 
        (thus, the index of the array will be wrong and the
        counter in the loop will start from the second element in arr)'''
        sum = 0
        for i in range(1, len(self.arr)):
            sum += self.arr[i]      
        return sum/len(self.arr)

    def first(self):
        return self.arr[0]

    def last(self):
        return self.arr[len(self.arr)-1]
