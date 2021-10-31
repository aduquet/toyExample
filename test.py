import unittest
from arrayCalculator import *

class TestArryCalc(unittest.TestCase):

    def settingArray(self, val1, val2, val3):
        a = arrayCalculator()
        a.sett(val1)
        a.sett(val2)
        a.sett(val3)

        return a

    def testOne(self): 

        # TC1a: AC.set([0,0,0]); assert_equal(0,AC.first(arr)) – input [0,0,0]
        a = self.settingArray(0,0,0)
        self.assertEqual(0, a.first())

        # TC1b: AC.set([1,2,3]); assert_equal(1,AC.first(arr))
        a = self.settingArray(1,2,3)
        self.assertEqual(1, a.first(), )
        
        # TC1c: AC.set([1,4,1]); assert_equal(1,AC.first(arr))
        a = self.settingArray(1, 4, 1)
        self.assertEqual(1, a.first())

    def testTwo(self): 

        # TC2a: AC.set([0,0,0]); assert_equal(0,AC.last(arr)) – input [0,0,0]
        a = self.settingArray(0,0,0)
        self.assertEqual(0, a.last())

        # TC2b: AC.set([1,2,3]); assert_equal(3,AC.last(arr))
        a = self.settingArray(1,2,3)
        self.assertEqual(3, a.last(), )
        
        # TC2c: AC.set([1,4,1]); assert_equal(1,AC.last(arr))
        a = self.settingArray(1, 4, 1)
        self.assertEqual(1, a.last())

    def testThree(self):

        # TC3a: AC.set([0,0,0]); assert_equal(0,AC.avg(arr)) – input [0,0,0]
        a = self.settingArray(0,0,0)
        self.assertEqual(0, a.avg())

        # TC3b: AC.set([1,2,3]); assert_equal(2,AC.avg(arr)) 
        a = self.settingArray(1,2,3)
        self.assertEqual(2, a.avg(), )
        
        # TC3c: AC.set([1,4,1]); assert_equal(2,AC.avg(arr))
        a = self.settingArray(1, 4, 1)
        self.assertEqual(2, a.avg())


if __name__ == '__main__':
  
    unittest.main()
