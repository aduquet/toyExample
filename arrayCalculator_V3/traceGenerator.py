import os
import sys
import pathlib
import pandas as pd

sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

def getState(input):
    
    global df_main
    df_main = pd.DataFrame()
  
    methodsList = ['inputID', 'inputValue','isEmpty', 'getSize', 'getAll', 'getFirst', 
                   'getSecondLast', 'getLast', 'avg']
    df_main = pd.DataFrame(columns=methodsList, index=None)
    
    df_main['isEmpty'] = input.isEmpty()
    df_main['getSize'] = input.getSize()
    df_main['getAll'] = [input.getAll()]
    df_main['getFirst'] = input.getFirst()
    df_main['getSecondLast'] = input.getSecondLast()
    df_main['getLast'] = input.getLast()
    df_main['avg'] = input.avg()


    return df_main
