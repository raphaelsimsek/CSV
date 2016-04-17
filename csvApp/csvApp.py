import csv


class csvApp:
    """
    Class which reads and writes to a CSV file, according to thedocumentation
    """

    def __init__(self, file):
        self.file = file
        self.data = []

    def csvReader(self):
        with open(self.file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            self.data = list(reader)
            print(self.data)
            """
            For not necessary, because of output as array
            for row in spamreader:
                self.data = self.data.append(row)
            """

    def csvWriter(self):
        with open(self.file, 'w') as writ:
            writer = csv.writer(writ, delimiter=';')
            writer.writerows(self.data)

if __name__ == '__main__':
    csvClass = csvApp('/Users/hackos/Documents/test.csv')
    csvClass.csvReader()
    csvClass.csvWriter()
