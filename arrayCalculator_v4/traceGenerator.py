import os
import sys
import pathlib
import pandas as pd
from arrayCalculator import *
sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

def getState(input, inputID):
    
    global df_main
    df_main = pd.DataFrame()
    dict = {'inputID': inputID, 
            'input': input,
            'isEmpty': input.isEmpty(), 
            'getSize': input.getSize(),
            'getAll': input.getAll(), 
            'getFirst': input.getFirst(), 
            'getSecondLast': input.getSecondLast(), 
            'getLast': input.getLast(), 
            'avg': input.avg()}
    df_main = df_main.append(dict, ignore_index = True)
    key_list = list(dict.keys())

    df_main.columns = key_list

    return df_main
