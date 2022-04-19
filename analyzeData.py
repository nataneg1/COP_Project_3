import csv, enum, math
from heapq import heappop

# Parent: i-1/2
# Left child: 2*i + 1
# Right child: 2*i + 2
class MaxHeap:
    def __init__(self):
        self.heap = []

    def buildMinHeap(self, list):
        # for each date
        for date in list:
            #if the heap is empty, add the first one
            self.heap.append(date)
            if len(self.heap) == 0:
                continue
            # if heap is not empty, add new date as a child and switch
            # with parent if needed. call min heapify if it is the 4th or 5th date
            childLocation = len(self.heap)-1
            self.minHeapify(childLocation)

    def minHeapify(self, childLocation):
        parentLocation = math.floor((childLocation-1)/2)
        #if the child is less than the parent
        if self.heap[childLocation].percent < self.heap[parentLocation].percent:
            temp = self.heap[parentLocation]
            self.heap[parentLocation] = self.heap[childLocation]
            self.heap[childLocation] = temp
            # check if root is still less than new child
            rootLocation = math.floor((parentLocation-1)/2)
            if rootLocation < 0:
                return
            else:
                self.minHeapify(parentLocation)

    def compare(self, newDate, parent = 0):
        if self
        


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

# ------------------------------------- READING CSV -------------------------------------

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


# ---------------------------------------------------------------------------------------

#building min heap with first 5 nodes
maxHeap.buildMinHeap(firstFiveDates)

#printing heap
for date in maxHeap.heap:
    date.printDate()


# Returns sorted array of top 5 dates
# def getTopFive(dateType, gainOrLoss, tickerName):
#     return