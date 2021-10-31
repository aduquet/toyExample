import os
import pathlib
import unittest
import pandas as pd
from adapter import *
from arrayCalculator_F3 import *

class TestArryCalc(unittest.TestCase):

    def saveState(self, df_main, tID, insID):

        df_main['testID'] = tID
        df_main['instanceID'] = insID
        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\adapter_F3.csv'
        
        if not os.path.exists(resultsPath):    
            with open('adapter_F3.csv', 'a', newline = '') as f:
                df_main = df_main.sort_values(by=['testID'], ascending=True)
                df_main.to_csv(f, index = False, header = True)

        else:
            with open('adapter.csv', 'a', newline = '') as f:
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
        a = self.settingArray(0,0,0, 'TC1', 'TC1a')
        self.assertEqual(0, a.first())

        # TC1b: AC.set([1,2,3]); assert_equal(1,AC.first(arr))
        a = self.settingArray(1,2,3, 'TC1', 'TC1b')
        self.assertEqual(1, a.first(), )
        
        # TC1c: AC.set([1,4,1]); assert_equal(1,AC.first(arr))
        a = self.settingArray(1, 4, 1, 'TC1', 'TC1c')
        self.assertEqual(1, a.first())

    def testTwo(self): 

        # TC2a: AC.set([0,0,0]); assert_equal(0,AC.last(arr)) – input [0,0,0]
        a = self.settingArray(0,0,0, 'TC2', 'TC2a')
        self.assertEqual(0, a.last())

        # TC2b: AC.set([1,2,3]); assert_equal(3,AC.last(arr))
        a = self.settingArray(1,2,3, 'TC2', 'TC2c')
        self.assertEqual(3, a.last())
        
        # TC2c: AC.set([1,4,1]); assert_equal(1,AC.last(arr))
        a = self.settingArray(1, 4, 1, 'TC2', 'TC2c')
        self.assertEqual(1, a.last())

    def testThree(self):

        # TC3a: AC.set([0,0,0]); assert_equal(0,AC.avg(arr)) – input [0,0,0]
        a = self.settingArray(0,0,0, 'TC3', 'TC3a')
        self.assertEqual(0, a.avg())

        # TC3b: AC.set([1,2,3]); assert_equal(2,AC.avg(arr)) 
        a = self.settingArray(1,2,3, 'TC3', 'TC3b')
        self.assertEqual(2, a.avg(), )
        
        # TC3c: AC.set([1,4,1]); assert_equal(2,AC.avg(arr))
        a = self.settingArray(1, 4, 1, 'TC3', 'TC3c')
        self.assertEqual(2, a.avg())



if __name__ == '__main__':
  
    unittest.main()
