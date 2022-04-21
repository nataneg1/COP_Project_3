import analyzeData ,enum, verify

class DateRange(enum.Enum):
    day = 1
    week = 2
    month = 3
    year = 4


list = [] 
name = str(input("Name Of Ticker: "))
list.append(name)

date = str(input("Choose date option: Daily, Weekly, Monthly, or Yearly: "))
if date == "Daily":
    list.append(1)
elif date == "Weekly":
    list.append(2)
elif date == "Monthly":
    list.append(3)
elif date == "Yearly":
    list.append(4)

option = str(input("Gain or Loss: ")) 
if option == "Gain":
    list.append(1)
elif option == "Loss":
    list.append(0)


if verify.tickerExists(str(list[0])) == True:
    analyzeData.getTopFive(int(list[1]), int(list[2]), str(list[0]))
else:
    print("Ticker does not exist")