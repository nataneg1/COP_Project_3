from calendar import c
import csv, enum, math
from heapq import heappop
from tracemalloc import start

monthMap = {
    "01":31, 
    "02":28,
    "03":31,
    "04":30,
    "05":31,
    "06":30,
    "07":31,
    "08":31,
    "09":30,
    "10":31,
    "11":30,
    "12":31,
    }

class DateRange(enum.Enum):
    day = 1
    week = 2
    month = 3
    year = 4

class GainOrLossChoice(enum.Enum):
    gain = 1
    loss = 0

class Date:
    def __init__(self, m, d, y, o, c, gainOrLoss):
        self.month = m
        self.day = d
        self.year = y
        self.open = float(o)
        self.close = float(c)
        self.gainOrLoss = gainOrLoss
        self.percent = self.setPercent(gainOrLoss)
        
    def setPercent(self, gainOrLoss):
        percent = round(((self.close-self.open)/self.open)*100, 3)
        if gainOrLoss == GainOrLossChoice.loss:
            percent = percent*-1.0
        return percent


    def printDate(self):
        print(self.month + "-" + self.day + "-" + self.year)
        print("Open: " + str(self.open))
        print("Close: " + str(self.close))
        tempPercent = self.percent
        if self.gainOrLoss == GainOrLossChoice.loss:
            tempPercent = tempPercent*-1.0
        print("Percent: " + str(tempPercent) + "%")
        print("\n")

# Class that can represent a week, month, or year. Contains the % increase or decrease as well as start and end dates
class DateType:
    def __init__(self, startDate, endDate, gainOrLoss):
        self.startDate = startDate
        self.startPrice = float(startDate.open)
        self.endDate = endDate
        self.endPrice = float(endDate.close)
        self.gainOrLoss = gainOrLoss
        self.percent = self.setPercent(gainOrLoss)
    
    def setPercent(self, gainOrLoss):
        percent = round(((self.endPrice-self.startPrice)/self.startPrice)*100, 3)
        if gainOrLoss == GainOrLossChoice.loss:
            percent = percent*-1.0
        return percent

    def printDateType(self):
        print("Start Date: " + self.startDate.month + "-" + self.startDate.day + "-" + self.startDate.year)
        print("End Date: " + self.endDate.month + "-" + self.endDate.day + "-" + self.endDate.year)
        print("Start Price: " + str(self.startPrice))
        print("End Price: " + str(self.endPrice))
        tempPercent = self.percent
        if self.gainOrLoss == GainOrLossChoice.loss:
            tempPercent = tempPercent*-1.0
        print("Percent: " + str(tempPercent) + "%")
        print("\n")

# Parent: i-1/2
# Left child: 2*i + 1
# Right child: 2*i + 2
class MinHeap:
    def __init__(self):
        self.heap = []

    def buildMinHeap(self, list):
        # for each date
        for date in list:
            #if looking for worst year, change all signs
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

    def compare(self, newDate, parentLocation = 0):
        newPercent = newDate.percent
        leftChildLocation = 2*parentLocation + 1
        rightChildLocation = 2*parentLocation + 2

        # if the newDate is not greater than the minimum root percent, exit
        if newPercent < self.heap[parentLocation].percent or newPercent == self.heap[parentLocation].percent:
            return
        # if the newDate is greater than the left root, do compare on the left root
        if newPercent > self.heap[leftChildLocation].percent:
            if(leftChildLocation == 3):
                self.heap[leftChildLocation] = newDate
                return
            self.compare(newDate, leftChildLocation)
            return
        # if the newDate is less than the left, but greater than the right, replace it
        elif newPercent > self.heap[rightChildLocation].percent:
            self.heap[rightChildLocation] = newDate
            return
        # set parent node equal to newDate
        self.heap[parentLocation] = newDate
        
# ===================================================== HELPER FUNCTIONS =====================================================
minHeap = MinHeap()

def buildDate(dataArray, gainOrLoss):
    dateList = dataArray[0].split('-')
    year = dateList[0]
    month = dateList[1]
    day = dateList[2]
    return Date(month, day, year, dataArray[1], dataArray[4], gainOrLoss)

def findNextDate(dateType, startDate, counter, listOfDates):
    if dateType == DateRange.day:
        return
    if dateType == DateRange.week:
        firstDateDay = startDate.day
        counter += 5
        lastDateGuess = listOfDates[counter]
        lastDateDayGuess = (int(firstDateDay) + 7)%monthMap[startDate.month]
        # if the date guess is greater than the guess, guess the day before it
        if int(lastDateGuess.day) > lastDateDayGuess or (lastDateGuess.month != startDate.month and int(lastDateGuess.day) != lastDateDayGuess):
            counter -= 1
            lastDateGuess = listOfDates[counter]
        else:
            lastDateGuess = listOfDates[counter]
        return lastDateGuess, counter
    if dateType == DateRange.month:
        firstDateDay = startDate.day
        firstDateMonth = startDate.month
        counter += 24
        tempCounter = counter
        lastDateGuess = listOfDates[counter]
        lastDateMonthGuess = (int(firstDateMonth) + 1)%12
        if lastDateMonthGuess == 0:
            lastDateMonthGuess = 12
        # if the date guess is greater than the guess, guess the day before it
        # (int(lastDateGuess.month) != lastDateMonthGuess and int(lastDateGuess.day) < int(firstDateDay)
        while ((int(lastDateGuess.day) > int(firstDateDay)) and (int(lastDateGuess.month) == lastDateMonthGuess) or ((int(lastDateGuess.month) > lastDateMonthGuess) and (int(lastDateGuess.day) < int(firstDateDay)))):
            # lastDateGuess.printDate()
            tempCounter -= 1
            lastDateGuess = listOfDates[tempCounter]
        lastDateGuess = listOfDates[tempCounter]
        return lastDateGuess, tempCounter
    if dateType == DateRange.year:
        firstDateDay = startDate.day
        firstDateMonth = startDate.month
        firstDateYear = startDate.year
        #estimates how many days until next new year (excluding weekends)
        counter += int(math.ceil((5/7)*((30*(12-int(firstDateMonth))) + 30-int(firstDateDay)))) + 5
        tempCounter = counter
        lastDateGuess = listOfDates[counter]
        lastDateYearGuess = int(firstDateYear) + 1
        # if the date guess is greater than the guess, guess the day before it
        # (int(lastDateGuess.month) != lastDateMonthGuess and int(lastDateGuess.day) < int(firstDateDay)
        while (int(lastDateGuess.day) > 1) and int(lastDateGuess.year) == lastDateYearGuess:
            # lastDateGuess.printDate()
            tempCounter -= 1
            lastDateGuess = listOfDates[tempCounter]
        tempCounter += 1
        lastDateGuess = listOfDates[tempCounter]
        return lastDateGuess, tempCounter



def getFirstFiveDates(dateType, dateList, gainOrLoss):
    fiveDateList = []
    finalCounter = 0
    if dateType == DateRange.day:
        for date in dateList[:5]:
            fiveDateList.append(date)
    else:
        counter = 0
        while len(fiveDateList) != 5:
            firstDate = dateList[counter]
            lastDateGuess, counter = findNextDate(dateType, firstDate, counter, dateList)
            newDateType = DateType(firstDate, lastDateGuess, gainOrLoss)
            fiveDateList.append(newDateType)
        finalCounter = counter
    return fiveDateList, finalCounter


# Goes through list of dates and orginizes them based off their dateType
def compareDateType(dateType, listOfDates, gainOrLoss):
    if dateType == DateRange.day:
        for date in listOfDates:
            minHeap.compare(date)
    elif dateType == DateRange.week:
        counter = 0
        firstDate = listOfDates[counter]
        while (counter+5) < len(listOfDates):
            firstDate = listOfDates[counter]
            lastDateGuess, counter = findNextDate(dateType, firstDate, counter, listOfDates)
            newDateType = DateType(firstDate, lastDateGuess, gainOrLoss)
            minHeap.compare(newDateType)
    elif dateType == DateRange.month:
        counter = 0
        while (counter+24) < len(listOfDates):
            firstDate = listOfDates[counter]
            lastDateGuess, counter = findNextDate(dateType, firstDate, counter, listOfDates)
            newDateType = DateType(firstDate, lastDateGuess, gainOrLoss)
            minHeap.compare(newDateType)
    elif dateType == DateRange.year:
        counter = 0
        while (counter+260) < len(listOfDates):
            firstDate = listOfDates[counter]
            lastDateGuess, counter = findNextDate(dateType, firstDate, counter, listOfDates)
            newDateType = DateType(firstDate, lastDateGuess, gainOrLoss)
            minHeap.compare(newDateType)
    
def printHeap(dateType):
    #printing heap
    for date in minHeap.heap:
        if dateType == DateRange.day:
            date.printDate()
        else:
            date.printDateType()




# ============================================================================================================================



def getTopFive(dateType, gainOrLoss, tickerName):

    # ------------------------------------- READING CSV -------------------------------------

    # csv file name
    filename = "./Stocks/" + tickerName + ".us.txt"
    
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
    
        # # get total number of rows
        # print("Total no. of rows: %d"%(csvreader.line_num))

    firstFiveDates = []
    dateList = []
    # Date, Open, High, Low, Close, Volume, OpenInt
    for row in rows:
        # parsing each column of a row
        dataArray = []
        for dataPoint in row:
            dataArray.append(dataPoint)
        dateList.append(buildDate(dataArray, gainOrLoss))
    for date in dateList[:5]:
        firstFiveDates.append(date)

    # ---------------------------------------------------------------------------------------

    # 1. build initial heap
    # 2. compare dates to sort through data
    # 3. return sorted array
    print("List size: " + str(len(dateList)))
    if(float(len(dateList)/261) < 5.0):
        print("Too Little Data")
        return -1
    if dateType == DateRange.day:
        firstFive, positionOfLastDateAdded = getFirstFiveDates(dateType, dateList, gainOrLoss)
        minHeap.buildMinHeap(firstFive)
        compareDateType(dateType, dateList[5:], gainOrLoss)
    else:
        firstFive, positionOfLastDateAdded = getFirstFiveDates(dateType, dateList, gainOrLoss)
        minHeap.buildMinHeap(firstFive)
        positionOfLastDateAdded += 1
        compareDateType(dateType, dateList[positionOfLastDateAdded:], gainOrLoss)
    
    return

# #printing heap
# for date in maxHeap.heap:
#     date.printDate()

# print("------------------------------------------- PRINTING HEAP -------------------------------------------")

# # testing compare function
# for date in dateList:
#     maxHeap.compare(date)
#     # date.printDate()
dateType = DateRange.year
getTopFive(dateType, GainOrLossChoice.loss, "aapl")

print("------------------------------------------- PRINTING HEAP -------------------------------------------")

printHeap(dateType)