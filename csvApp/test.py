import unittest
from csvApp.csvApp import CSVApplication

__author__ = "Raphael Simsek"
__date__ = "2016-04-21"
__status__ = "deployed"

class CSVtest(unittest.TestCase):
    def setUp(self):
        self.c = CSVApplication('test.csv')

    def test_load1(self):
        self.csvClass= CSVApplication('test.csv')
        self.csvClass.csvreader()
        self.assertTrue(None)

    def test_load2(self):
        try:
            self.csvClass = CSVApplication('test1.csv')
            self.csvClass.csvreader()
        except IOError as e:
            self.assertTrue("CSV-file couldn't be loaded\n %s" % e)

    def test_load3(self):
        try:
            self.csvClass = CSVApplication('test.csv')
            self.csvClass.getdialect()
        except AssertionError as e:
            self.assertFalse("CSV dialect could not be found\n %s" % e)

if __name__ == '__main__':
    unittest.main()
