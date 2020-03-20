import datetime as dt 

date = dt.datetime.now()

print(str(date.strftime("%Y")) + "-" + str(date.strftime("%m")) + "-" + str(date.strftime("%d")))