from _thread import start_new_thread as new_th
from time import sleep

def print_time(TH_name,delay):
    count=0
    while count<20:
        sleep(delay)
        count+=delay
        print("{} {} seconds".format(TH_name,count))

try:
    new_th(print_time,("Thread 1",2))
    new_th(print_time,("Thread 2",5))
except:
    print("Error: unable to start thread")

while(1):
    pass

