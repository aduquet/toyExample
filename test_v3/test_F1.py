import os
import sys
import pathlib
import unittest
import pandas as pd
from adapter import *
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
 
    def adapterSetting(self, val1, val2, val3, testID, instansceID):
        
        a = arrayCalculator()
        a.setter(val1,val2, val3)
        df_main = getState(a)
        self.saveState(df_main, testID, instansceID)
        return a

    def test_getter(self):
        TC = 'test_getter'
        # test_getter_a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        a1 = self.adapterSetting(0,0,0, TC, TC + '_a')
        self.assertEqual([0,0,0], a1.getter())

        # test_getter_b: AC.set([1,2,3]); assert_equal(1,AC.first(arr))
        b1 = self.adapterSetting(1,2,3, TC, TC + '_b')
        self.assertEqual([1,2,3], b1.getter())      

        # test_getter_c: AC.set([1,4,1]); assert_equal(1,AC.first(arr))
        c1 = self.adapterSetting(1, 4, 1, TC, TC + '_c')
        self.assertEqual([1,4,1], c1.getter())

    def test_first(self): 
        TC = 'test_first'
        # test_first_a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        a1 = self.adapterSetting(0,0,0, TC, TC + '_a')
        self.assertEqual(0, a1.first())

        # test_first_b: AC.set([1,2,3]); assert_equal(1,AC.first(arr))
        b1 = self.adapterSetting(1,2,3, TC, TC + '_b')
        self.assertEqual(1, b1.first())      

        # test_first_c: AC.set([1,4,1]); assert_equal(1,AC.first(arr))
        c1 = self.adapterSetting(1, 4, 1, TC, TC + '_c')
        self.assertEqual(1, c1.first())

    def test_last(self): 
        TC = 'test_last'
        # test_last_a: AC.set([0,0,0]); assert_equal(0,AC.last(arr)) – input [0,0,0]
        a2 = self.adapterSetting(0,0,0, TC, TC + '_a')
        self.assertEqual(0, a2.last())       

        # test_last_b: AC.set([1,2,3]); assert_equal(3,AC.last(arr))
        b2 = self.adapterSetting(1,2,3, TC, TC + '_b')
        self.assertEqual(3, b2.last())

        # test_last_c: AC.set([1,4,1]); assert_equal(1,AC.last(arr))
        c2 = self.adapterSetting(1, 4, 1, TC, TC + '_c')
        self.assertEqual(1, c2.last())

    def test_avg(self):
        TC = 'test_avg'
        # test_avg_a: AC.set([0,0,0]); assert_equal(0,AC.avg(arr)) – input [0,0,0]
        a3 = self.adapterSetting(0,0,0, TC, TC + '_a')
        self.assertEqual(0, a3.avg())     

        # test_avg_b: AC.set([1,2,3]); assert_equal(2,AC.avg(arr)) 
        b3 = self.adapterSetting(1,2,3, TC, TC + '_b')
        self.assertEqual(2, b3.avg())        

        # test_avg_c: AC.set([1,4,1]); assert_equal(2,AC.avg(arr))
        c3 = self.adapterSetting(1, 4, 1, TC, TC + '_c')
        self.assertEqual(2, c3.avg())

if __name__ == '__main__':

    def main(out = sys.stderr, verbosity = 2):
        loader = unittest.TestLoader()
  
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
  
    with open('test-Output_F1.txt', 'w') as f:
        main(f)

