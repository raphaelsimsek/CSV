import unittest
import CSVApp

__author__="Raphael Simsek"
__date__="2016-04-21"
__status__="deployed"

class CSVtest(unittest.TestCase):
    def setUp(self):
        self.c = CSVApp.CSVApplication('test.csv')

    def test_load1(self):
        self.csvClass= CSVApp.CSVApplication('test.csv')
        self.csvClass.csvreader()
        self.assertTrue()

    def test_load2(self):
        try:
            self.csvClass = CSVApp.CSVApplication('test1.csv')
            self.csvClass.read()
        except IOError as e:
            self.assertTrue("CSV-file couldn't be loaded\n %s" % e)

    def test_load3(self):
        try:
            self.csvClass = CSVApp.CSVApplication('test.csv')
            self.csvClass.getdialect()
        except AssertionError as e:
            self.assertFalse("CSV dialect could not be found\n %s" % e)

if __name__ == '__main__':
    unittest.main()

    csvClass = CSVApplication('../test.csv')
    # csvClass.getdialect()
    csvClass.csvreader()
    #time.sleep(5)
    csvClass.csvwriter()
    #time.sleep(5)
    csvClass.csvwriteradd()
    #time.sleep(10)
    csvClass.csvaddtodata()