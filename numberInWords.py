import sys
from math import log
digitMap = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def convert(numberInWords):
    try:
        numberInWordsSplit = numberInWords.split()
        number = '' 
        for index in numberInWordsSplit:
            number = number + digitMap[index]
        numberInInteger = int(number)
        print(numberInInteger)
        return numberInInteger
    except (KeyError, AttributeError) as exceptionDesc:
        print(f'Conversion Failed: {exceptionDesc!r}',file=sys.stderr)
        raise

def log_details_convert(numberInWords):
    logVariable = convert(numberInWords)
    return log(logVariable) 

if __name__ == '__main__':
    log_details_convert('one')          
