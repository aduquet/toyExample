from TraceToolPrueba.tracer import tracefunc
import myfunctions

@tracefunc
def main():
   x = 5
   print ('area=',myfunctions.area(x))
   print ('factorial=',myfunctions.factorial(x))

if __name__=='__main__':
   main()