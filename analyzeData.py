import csv, enum, math
from heapq import heappop

# Parent: i-1/2
# Left child: 2*i + 1
# Right child: 2*i + 2
class MaxHeap:
    def __init__(self):
        self.heap = []

    def buildMaxHeap(self, list):
        for date in list:
            if self.heap.size() == 0:
                self.heap.append(date)
                continue
            childLocation = self.heap.size()-1
            parentLocation = (childLocation-1)/2
                

    def mexHeapifyHelper(self):
        return

    def maxHeapify(self):
        firstParent = self.heap[math.floor(self.heap.size/2)]


maxHeap = MaxHeap()
class Date:
        def __init__(self, m, d, y, o, c):
            self.month = m
            self.day = d
            self.year = y
            self.open = float(o)
            self.close = float(c)
            self.percent = round(((self.close-self.open)/self.open), 3)

        def printDate(self):
            print(self.month + "-" + self.day + "-" + self.year)
            print("Open: " + str(self.open))
            print("Close: " + str(self.close))
            print("Percent: " + str(self.percent) + "%")
            print("\n")


def buildDate(dataArray):
    dateList = dataArray[0].split('-')
    year = dateList[0]
    month = dateList[1]
    day = dateList[2]
    return Date(month, day, year, dataArray[1], dataArray[4])

# csv file name
filename = "./Stocks/aapl.us.txt"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

firstFiveDates = []
# Date, Open, High, Low, Close, Volume, OpenInt
for row in rows[:5]:
    # parsing each column of a row
    dataArray = []
    for dataPoint in row:
        dataArray.append(dataPoint)
    firstFiveDates.append(buildDate(dataArray))

    print('\n')


# --------------------------------------------------------------------------------

#printing heap
for date in maxHeap.heap:
    date.printDate()


# Returns sorted array of top 5 dates
# def getTopFive(dateType, gainOrLoss, tickerName):
#     return