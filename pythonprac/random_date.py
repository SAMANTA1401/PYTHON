# Generate a random date between given start and end dates
import random
import time
def getRandomDate(startdate,enddate):
    randomgenerator=random.random()
    dateFormat='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startdate,dateFormat))
    endTime=time.mktime(time.strptime(enddate,dateFormat))
    randomTime=startTime+randomgenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))