import os
import sys
import pathlib
import unittest
import pandas as pd
from arrayCalculator_V3.traceGenerator import *
sys.path.append("C://Users//duquet//Documents//GitHub//toyExample//")

from arrayCalculator_F2 import *

class TestArryCalc(unittest.TestCase):

    def saveState(self, df_main, tID, insID):

        df_main['testID'] = tID
        df_main['instanceID'] = insID
        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\adapter_F2.csv'
        
        if not os.path.exists(resultsPath):    
            with open('adapter_F2.csv', 'a', newline = '') as f:
                df_main = df_main.sort_values(by=['testID'], ascending=True)
                df_main.to_csv(f, index = False, header = True)

        else:
            with open('adapter_F2.csv', 'a', newline = '') as f:
                df_main = df_main.sort_values(by=['testID'], ascending=True)
                df_main.to_csv(f, index = False, header = False)
 
    def adapterSetting(self, val1, val2, val3, testID, instansceID):
        
        a = arrayCalculator()
        a.setter(val1,val2, val3)
        df_main = getState(a)
        self.saveState(df_main, testID, instansceID)
        return a

    def test_getter(self):
        TC = 'test_getter'
        test_getter_a = self.adapterSetting(0,0,0, TC, TC + '_a')
        test_getter_b = self.adapterSetting(1,2,3, TC, TC + '_b')
        test_getter_c = self.adapterSetting(1, 4, 1, TC, TC + '_c')

        # test_getter_a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        self.assertEqual([0,0,0], test_getter_a.getter())
        # test_getter_b: AC.set([1,2,3]); assert_equal(1,AC.first(arr)) – input [1,2,4]
        self.assertEqual([1,2,3], test_getter_b.getter())      
        # test_getter_c: AC.set([1,4,1]); assert_equal(1,AC.first(arr)) - input [1,4,1]
        self.assertEqual([1,4,1], test_getter_c.getter())

    def test_first(self): 
        TC = 'test_first'
        test_first_a = self.adapterSetting(0,0,0, TC, TC + '_a')
        test_first_b = self.adapterSetting(1,2,3, TC, TC + '_b')
        test_first_c = self.adapterSetting(1, 4, 1, TC, TC + '_c')

        # test_first_a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        self.assertEqual(0, test_first_a.first())
        # test_first_b: AC.set([1,2,3]); assert_equal(1,AC.first(arr)) – input [1,2,4]
        self.assertEqual(1, test_first_b.first())      
        # test_first_c: AC.set([1,4,1]); assert_equal(1,AC.first(arr)) - input [1,4,1]
        self.assertEqual(1, test_first_c.first())

    def test_last(self): 
        TC = 'test_last'
        test_last_a = self.adapterSetting(0,0,0, TC, TC + '_a')
        test_last_b = self.adapterSetting(1,2,3, TC, TC + '_b')
        test_last_c = self.adapterSetting(1, 4, 1, TC, TC + '_c')

        # test_last_a: AC.set([0,0,0]); assert_equal(0,AC.last(arr)) – input [0,0,0]
        self.assertEqual(0, test_last_a.last())       
        # test_last_b: AC.set([1,2,3]); assert_equal(3,AC.last(arr)) – input [1,2,4]
        self.assertEqual(3, test_last_b.last())
        # test_last_c: AC.set([1,4,1]); assert_equal(1,AC.last(arr)) - input [1,4,1]
        self.assertEqual(1, test_last_c.last())

    def test_avg(self):
        TC = 'test_avg'
        test_avg_a = self.adapterSetting(0,0,0, TC, TC + '_a')
        test_avg_b = self.adapterSetting(1,2,3, TC, TC + '_b')
        test_avg_c = self.adapterSetting(1, 4, 1, TC, TC + '_c')

        # test_avg_a: AC.set([0,0,0]); assert_equal(0,AC.avg(arr)) – input [0,0,0]
        self.assertEqual(0, test_avg_a.avg())     
        # test_avg_b: AC.set([1,2,3]); assert_equal(2,AC.avg(arr)) – input [1,2,4] 
        self.assertEqual(2, test_avg_b.avg())        
        # test_avg_c: AC.set([1,4,1]); assert_equal(2,AC.avg(arr)) - input [1,4,1]
        self.assertEqual(2, test_avg_c.avg())

if __name__ == '__main__':

    def main(out = sys.stderr, verbosity = 2):
        loader = unittest.TestLoader()
  
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
  
    with open('test-Output_ F2.txt', 'w') as f:
        main(f)
