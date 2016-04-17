import csv


class csvReader:
    """
    Class which reads a CSV file, according to documentation
    """
    def __init__(self, file):
        self.file=file

    def schreiberling(self):
        with open(self.file, 'w') as writ:
            spamwriter = csv.writer(writ, delimiter=';')
            spamwriter.writerow(['A', 'B'])

    def leseratte(self):
        with open(self.file, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                print(','.join(row))

if __name__ == '__main__':
    cr = csvReader('/Users/hackos/Documents/test.csv')
    cr.schreiberling()
    cr.leseratte()
