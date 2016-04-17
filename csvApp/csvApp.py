import csv
import time

__author__ = "Raphael Simsek"
__maintainer__ = "Raphael Simsek"
__email__ = "raphael@simsek.me"
__status__ = "Work in Progress"


class CSVApp:
    """
    Class which reads and writes to a CSV file, according to pythons csv package documentation
    """

    def __init__(self, file):
        """
        Constructor for csvApp Class, which initializes all needed data
        :param file:
        :return:
        """
        self.file = file
        self.data = []
        self.dialect = None
        self.wAdd = True
        self.w = True

    def csvreader(self):
        with open(self.file, 'r') as csvfile:
            reader = csv.reader(csvfile, self.getdialect())
            self.data = list(reader)
            print(self.data)
            """
            For loop not necessary, because of output as array
            for row in spamreader:
                self.data = self.data.append(row)
            """

    def csvwriter(self):
        while self.data and self.w is True:
            # print(self.data)
            with open(self.file, 'w') as csvfile:
                writer = csv.writer(csvfile, self.dialect)
                writer.writerows(self.data)
                self.w = False
            print('wrote current self.data to file')

    def csvwriteradd(self):
        while self.data and self.wAdd is True:
            with open(self.file, 'w') as csvfile:
                writer = csv.writer(csvfile, self.dialect, lineterminator='\n')
                writer.writerows(self.data)
                writer.writerow(range(7))  # for testing if adding works
                self.wAdd = False
            print('Added additional data to the file')

    def csvaddtodata(self):
        print('About to write to self.data')
        self.data = self.data.append(list(range(5)))
        print(self.data)

    def getdialect(self):
        with open(self.file, 'r') as csvfile:
            try:
                # Get dialect off of sniffer (using the given 1 char strings)
                self.dialect = csv.Sniffer().sniff(csvfile.read(1024), ['\t', ';', ',', ' ', ':', '|'])
                print('CSV dialect was detected!')
                # Seek to beginning of file for further reading or writing
                csvfile.seek(0)
                return self.dialect
            except:
                pass
                #self.dialect = None
                #raise AssertionError('CSV dialect could not be detected!')

if __name__ == '__main__':
    csvClass = CSVApp('../test.csv')
    # csvClass.getdialect()
    csvClass.csvreader()
    """
    time.sleep(5)
    csvClass.csvwriter()
    time.sleep(5)
    csvClass.csvwriteradd()
    time.sleep(10)
    csvClass.csvaddtodata()
    """