import csv
import time

__author__ = "Raphael Simsek"
__maintainer__ = "Raphael Simsek"
__email__ = "raphael@simsek.me"
__status__ = "Deployed"


class CSVApp:
    """
    Class which reads and writes to a CSV file, according to pythons csv package documentation
    """

    def __init__(self, file):
        """
        Constructor for csvApp Class, which initializes all needed data
        :param file: CSV file, which is given at initialization to read and write to
        :return: None
        """
        if file is None:
            raise IOError('No CSV file was given')
        else:
            self.file=file
        self.data = []
        self.dialect = None
        self.wAdd = True
        self.w = True

    def csvreader(self):
        """
        A reader, which reads out the entire file and file and calls to getdialect()
        :return: None
        """
        with open(self.file, 'r') as csvfile:
            reader = csv.reader(csvfile, self.getdialect()) # Calls getdialect() to find CSV-Dialect
            self.data = list(reader) # makes an iterable list out of the readers content
            print(self.data)
            """
            For loop not necessary, because of output as array
            for row in spamreader:
                self.data = self.data.append(row)
            """
        csvfile.close()

    def csvwriter(self):
        """
        A writer, which writes the read content
        :return: None
        """
        while self.data and self.w is True: # self.data is implicitly False, when empty
            # print(self.data)
            with open(self.file, 'w') as csvfile:
                writer = csv.writer(csvfile, self.dialect)
                writer.writerows(self.data)

                self.w = False
            csvfile.close()
            print('wrote current self.data to file')

    def csvwriteradd(self):
        """
        A writer, which adds a line of content to the CSV
        :return: None
        """
        while self.data and self.wAdd is True:
            with open(self.file, 'w') as csvfile:
                writer = csv.writer(csvfile, self.dialect, lineterminator='\n')
                writer.writerows(self.data)
                writer.writerow([1,2,3,4,5])  # for testing if adding works
                self.wAdd = False
            csvfile.close()
            print('Added additional data to the file')
            print(self.data)

    def csvaddtodata(self):
        """
        A method to add data to the main memory variable self.data, which is writen to the file with csvwriter*
        :return: None
        """
        print('About to write to self.data')
        #print(self.data)
        #self.test = self.data[1];
        #self.test.append([1,2,3,4,5])
        #print(self.test)
        self.data.append([1,2,3,4,5])
        print(self.data)

    def getdialect(self):
        """
        Getdialect uses the the Sniffer off of the csv module to find the dialect the read in CSV file is written in.
        :return: None
        """
        with open(self.file, 'r') as csvfile:
            try:
                # Get dialect off of sniffer (using the given 1 char strings)
                self.dialect = csv.Sniffer().sniff(csvfile.read(1024), ['\t', ';', ',', ' ', ':', '|'])
                print('CSV dialect was detected!')
                # Seek to beginning of file for further reading or writing
                csvfile.seek(0)
                return self.dialect
            except:
                self.dialect = None
                raise AssertionError('CSV dialect could not be detected!')
        csvfile.close()

if __name__ == '__main__':
    """
    Main Method calling all the needed methods
    """
    csvClass = CSVApp('../test.csv')
    # csvClass.getdialect()
    csvClass.csvreader()
    #time.sleep(5)
    csvClass.csvwriter()
    #time.sleep(5)
    csvClass.csvwriteradd()
    #time.sleep(10)
    csvClass.csvaddtodata()