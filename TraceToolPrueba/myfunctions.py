import math

def area(x):
   a = math.pi*math.pow(x,2)
   return a

def factorial(x):
   if x==1:
      return 1
   else:
       return x*factorial(x-1)