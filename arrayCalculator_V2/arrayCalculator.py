'''Assume we have a class called ArrayCalculator (short: AC) as follows:
-	AC has as an instance variable an array of integers with 3 elements (name: arr)
-	AC has a setter method set that assigns values to the instance variable arr
-	AC has a getter method get that displays the elements of the instance variable arr
-	AC has a method avg that returns the average value of the three elements of arr
-	AC has a method first that returns the value of the first element of arr
-	AC has a method last that returns the value of the last element of arr '''

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
        return self.arr[len(self.arr)-1]
