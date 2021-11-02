import os
import sys
import pathlib
import pandas as pd

sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

def getState(self, a):
    
    global df_main
    df_main = pd.DataFrame()
  
    methodsList = ['testID', 'instanceID', 'get', 'avg', 'first', 'last']

    df_main = pd.DataFrame(columns=methodsList, index=None)
    
    df_main['get'] = [a.gett()]
    df_main['avg'] = a.avg()
    df_main['first'] = a.first()
    df_main['last'] = a.last()
    # print(df_main)
    return df_main