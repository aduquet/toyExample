import os
import sys
import pathlib
import pandas as pd

sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

def getState(input):
    
    global df_main
    df_main = pd.DataFrame()
  
    methodsList = ['testID', 'instanceID', 'get', 'avg', 'first', 'last']
    df_main = pd.DataFrame(columns=methodsList, index=None)
    
    df_main['get'] = [input.gett()]
    df_main['avg'] = input.avg()
    df_main['first'] = input.first()
    df_main['last'] = input.last()

    return df_main
