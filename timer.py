import datetime
import time
import winsound
import calendar
import os
import timeit


# this technique is problematic
# not actually one second because the code also takes time to execute. so its actually longer.

def alarm(alarm_time):
    #convert time into seconds
    timeleft = to_secs(alarm_time)
    while(timeleft != 0):
        # every second decrement time left and print time left.
        time.sleep(1)
        timeleft -= 1
        print(to_alarm(timeleft))
    

def to_secs(alarm_time):
    secs = int(alarm_time[0]) * 3600 + int(alarm_time[1]) * 60 + int(alarm_time[2])
    return secs

def to_alarm(secs):
    # convert secs back into alarm clock style
    hours = secs // 3600
    mins = (secs % 3600) // 60
    secs = (secs % 3600) % 60
    return [hours, mins, secs]


        
# check to make sure time input is ok
# return true if ok false if bad input
def check_input(tlist):
    for i in tlist:
        if len(i) != 2:
            return False
        if not i.isdigit():
            return False
    if len(tlist) != 3:
        return False
    return True

def get_alarm_time():
    #eventually get this from a text field for now use cmd line input
    t = input("Set alarm time (HH:MM:SS): ")
    # parse input and make a tuple (hh,mm,ss)
    tlist = t.split(":")
    # check for incorrect input
    if check_input(tlist) == False:
        print("incorrect time input")
        return
    else:
        return tlist


alarm_time = get_alarm_time()
tic = time.perf_counter()
alarm(alarm_time)
toc = time.perf_counter()

# shows that for every 10 secs about .01 secs is added because of computation time. 
# need a more accurate time. based off of gmtime.
print(tic-toc)
    
    
