import os
import pathlib
import unittest
import pandas as pd
from arrayCalculator_V3.traceGenerator import *
import sys
sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

from arrayCalculator_F1 import *

class TestArryCalc(unittest.TestCase):

    def saveState(self, df_main, tID, insID):

        df_main['testID'] = tID
        df_main['instanceID'] = insID
        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\adapter_F1.csv'
        
        if not os.path.exists(resultsPath):    
            with open('adapter_F1.csv', 'a', newline = '') as f:
                df_main = df_main.sort_values(by=['testID'], ascending=True)
                df_main.to_csv(f, index = False, header = True)

        else:
            with open('adapter_F1.csv', 'a', newline = '') as f:
                df_main = df_main.sort_values(by=['testID'], ascending=True)
                df_main.to_csv(f, index = False, header = False)

    def settingArray(self, val1, val2, val3, testID, instansceID):
        
        a = arrayCalculator()
        a.sett(val1,val2, val3)
        df_main = getState(self, a)
        self.saveState(df_main, testID, instansceID)
        return a

    def testOne(self): 

        # TC1a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        a1 = self.settingArray(0,0,0, 'TC1', 'TC1a')
        # TC1b: AC.set([1,2,3]); assert_equal(1,AC.first(arr))
        b1 = self.settingArray(1,2,3, 'TC1', 'TC1b')
        # TC1c: AC.set([1,4,1]); assert_equal(1,AC.first(arr))
        c1 = self.settingArray(1, 4, 1, 'TC1', 'TC1c')

        self.assertEqual(0, a1.first())
        self.assertEqual(1, b1.first())      
        self.assertEqual(1, c1.first())

    def testTwo(self): 

        # TC2a: AC.set([0,0,0]); assert_equal(0,AC.last(arr)) – input [0,0,0]
        a2 = self.settingArray(0,0,0, 'TC2', 'TC2a')
        # TC2b: AC.set([1,2,3]); assert_equal(3,AC.last(arr))
        b2 = self.settingArray(1,2,3, 'TC2', 'TC2b')
        # TC2c: AC.set([1,4,1]); assert_equal(1,AC.last(arr))
        c2 = self.settingArray(1, 4, 1, 'TC2', 'TC2c')

        self.assertEqual(0, a2.last())       
        self.assertEqual(3, b2.last())
        self.assertEqual(1, c2.last())

    def testThree(self):

        # TC3a: AC.set([0,0,0]); assert_equal(0,AC.avg(arr)) – input [0,0,0]
        a3 = self.settingArray(0,0,0, 'TC3', 'TC3a')
        # TC3b: AC.set([1,2,3]); assert_equal(2,AC.avg(arr)) 
        b3 = self.settingArray(1,2,3, 'TC3', 'TC3b')
        # TC3c: AC.set([1,4,1]); assert_equal(2,AC.avg(arr))
        c3 = self.settingArray(1, 4, 1, 'TC3', 'TC3c')

        self.assertEqual(0, a3.avg())     
        self.assertEqual(2, b3.avg())        
        self.assertEqual(2, c3.avg())


if __name__ == '__main__':
  
    def main(out = sys.stderr, verbosity = 2):
        loader = unittest.TestLoader()
  
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
  
    with open('test_F1-Output.txt', 'w') as f:
        main(f)

