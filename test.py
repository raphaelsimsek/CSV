import unittest
from csvApp import CSVApp

__author__="Raphael Simsek"
__date__="2016-04-21"
__status__="deployed"

class CSVtest(unittest.TestCase):
    def setUp(self):
        self.c = CSVApp('test.csv')

    def test_load1(self):
        self.csvClass= CSVApp('test.csv')
        self.csvClass.csvreader()
        self.assertTrue()

    def test_load2(self):
        try:
            self.csvClass = CSVApp('test1.csv')
            self.csvClass.read()
        except IOError as e:
            self.assertTrue("CSV-file couldn't be loaded\n %s" % e)

    def test_load3(self):
        try:
            self.csvClass = CSVApp('test.csv')
            self.csvClass.getdialect()
        except AssertionError as e:
            self.assertFalse("CSV dialect could not be found\n %s" % e)

if __name__ == '__main__':
    unittest.main()