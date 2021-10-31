import pandas as pd

from arrayCalculator_F1 import *

def getState(self, a):
    global df_main
    df_main = pd.DataFrame()
  
    methodsList = ['testID', 'instanceID', 'get', 'avg', 'first', 'last']
    #for k, v in arrayCalculator.__dict__.items():
    #    if "function" in str(v):
    #        methodsList.append(k)

    df_main = pd.DataFrame(columns=methodsList, index=None)
    
    df_main['get'] = [a.gett()]
    df_main['avg'] = a.avg()
    df_main['first'] = a.first()
    df_main['last'] = a.last()
    # print(df_main)
    return df_main
