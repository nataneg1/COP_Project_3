from flask import Flask, render_template
import analyzeData, enum
app = Flask(__name__)

@app.route('/')
def home():
    # TODO: Build Tree
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

# Enumeration for the user's choice of date
# https://www.geeksforgeeks.org/enum-in-python/
class Date(enum.Enum):
    day = 1
    week = 2
    month = 3
    year = 4


'''
From Front End:
    1. Ticker Name
    2. Gain or Loss
    3. Date: Daily, Weekly, Monthly, or Yearly
'''
# TODO: Define Tree Class

def buildTree():
    # iterate through tickers and insert node in alphabetical order
    # https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
    return

def tickerExists(tickerName):
    return False
    #use tree to find ticker name. if present
        # return true
    # else
        #return false