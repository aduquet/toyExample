import os
import sys
import pathlib
import unittest
import pandas as pd
import warnings

from traceGenerator import getState
from arrayCalculator import *

warnings.filterwarnings('ignore')
sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

from arrayCalculator import *

def saveState( df_main, tID, insID):
    
    df_main['inputID'] = tID
    df_main['input'] = [insID]
    here_iam = str(pathlib.Path().absolute())
    resultsPath = here_iam + '\\adapter2.csv'
        
    if not os.path.exists(resultsPath):    
         with open('adapter2.csv', 'a', newline = '') as f:
            df_main = df_main.sort_values(by=['inputID'], ascending=True)
            df_main.to_csv(f, index = False, header = True)
            print('*****************')

    else:
        with open('adapter2.csv', 'a', newline = '') as f:
            df_main = df_main.sort_values(by=['inputID'], ascending=True)
            df_main.to_csv(f, index = False, header = False)


def readInputs():
    
    file1 = open( ROOT_DIR + '//FuzzerInputs//inputsArray_B.txt', 'r')
    df = pd.DataFrame()

    Lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        if line.find('\n') != -1:
            line = line.replace('\n', '')
        aux = []
        for i in line:
            aux.append(int(i))
        dict = {'inputID': count, 'input': aux}
        df = df.append(dict, ignore_index = True)
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
    return df

inputs = readInputs()
for index, row in inputs.iterrows():
    input = list(row['input'])
    a = ArrayCalculator()
 
    a.setter(input)
    df_main = getState(a, index)
    #print(df_main)
    saveState(df_main, row['inputID'], input)
