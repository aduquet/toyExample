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
            self.arr.pop(self.getSize() - 2)
        except ValueError:
            pass
        
    def poptLast(self):
        try:
            self.arr.pop(self.getSize() - 1)
        except ValueError:
            pass
    
    def popByIndex(self, index):
        try:
            self.arr.pop(index)
        except ValueError:
            pass
    
    def popByElement(self, val):
        try:
            if type(self.searchingToGetIndex(val)) != str:
                elementIndex = self.searchingToGetIndex(val)
                self.arr.pop(elementIndex)
            else:
                raise NameError('Error!')

        except ValueError:
            print('An exception flew by!')
            raise NameError
    
    def getAll(self):
        if self.isEmpty() == False:
            return self.arr
        else:
            return ('error! the array is empty or the value is not in the array')
        
    def getFirst(self):
        if self.isEmpty() == False:
            return self.arr[0]
        else:
            return ('error! the array is empty or the value is not in the array')
    
    def getSecondLast(self):
        if self.isEmpty() == False:
            return self.arr[self.getSize() - 1]
        else:
            return ('error! the array is empty or the value is not in the array')
    
    def getLast(self):
        if self.isEmpty() == False:
            return self.arr[self.getSize() - 1]
        else:
            return ('error! the array is empty or the value is not in the array')
    
    def getByIndex(self, index):
        if self.isEmpty() == False:
            if index  <= self.getSize() :
                return self.arr[index]
            else:
                return ('error! the array is empty or the value is not in the array')
        else:
            return ('error! the array is empty or the value is not in the array')
  
    def searching(self, valtosearch):
        if self.isEmpty() == False:
            if valtosearch in self.arr:
                return True
            else:
                return False
        else:
            return ('error! the array is empty or the number is not in the array')

    def searchingToGetIndex(self, valtosearch):
        if self.isEmpty() == False and self.searching(valtosearch) == True:
            return self.arr.index(valtosearch)
        else:
            return ('error! the array is empty or the value is not in the array')  

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.arr)
    
    def bubbleSort(self, reverse):
            arrySize = self.getSize()
            if reverse == False:
                for n in range(arrySize - 1, 0, -1):
                    for i in range(n):
                        if self.arr[i] > self.arr[i + 1]:
                            # swapping data if the element is less than next element in the array
                            self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                return self.arr
            else:
                for i in range(arrySize - 1):
                    for j in range(0, arrySize - i - 1 ):
                        if self.arr[j] < self.arr[j + 1] :
                            self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            
                return self.arr            
    
    def avg(self):
        
        if self.isEmpty() == False:
            try:
                sum = 0
                for i in self.arr:
                    sum += i      
                return sum/self.getSize()
            except ZeroDivisionError:
                return ("division by zero!")
        else:
            return ('error! the array is empty')

    def mager(self, NewArry):
        if self.isEmpty() == False and len(NewArry) != 0:
            for i in NewArry:
                self.insertLast(i)
            return self.arr
        
    def elementWiseProduct(self, NewArry):
        aux = []
        if self.getSize() == len(NewArry):
            for i in range(0, len(NewArry)):
                aux.append(self.arr[i] * NewArry[i])
            return aux
        else:
            return ('error!')
         
    def dotProduct(self, NewArry):
        aux = []
        if self.getSize() == len(NewArry):
            aux = self.elementWiseProduct(NewArry)
            return sum(aux)
        else:
            return ('error!')
    
    def suma(self, NewArry):
        aux = []
        if self.getSize() == len(NewArry):
            for i in range(0, len(NewArry)):
                aux.append(self.arr[i] + NewArry[i])
            return aux
        else:
            return ('error!')
    
    def diff(self, NewArry):
        aux = []
        if self.getSize() == len(NewArry):
            for i in range(0, len(NewArry)):
                aux.append(self.arr[i] - NewArry[i])
            return aux
        else:
            return ('error!')