import time
import keyboard
import sys

print("==========Welcome to the stop watch==========")
print("Instructions:")
print("1) Press 'space bar' to Start/Stop timer")
print("2) Press 'r' to reset timer")
print("3) Press 'Esc' to exit program\n")

start_time = 0
stop_time = 0
wait_time_accum = 0
do_something_once = 0

while (True):

    keyboard.wait('space')
    start_time = time.perf_counter()
    #print("Start time %0.2f" %start_time, end = "\n", flush = True)
    time.sleep(0.2)

    while(True):

        elapsed_time = time.perf_counter()
        running_time = (time.perf_counter() - start_time)
        wait_time = (start_time-stop_time)

        if do_something_once == 0:
            wait_time_accum += wait_time
            do_something_once = 1

        stop_watch_time = (time.perf_counter() - wait_time_accum)


        #print("elapsed time: %0.2f wait time: %0.2f running time: %0.2f accum wait time: %0.2f TIME: %0.2f"
        #            %(elapsed_time, wait_time, running_time, wait_time_accum, stop_watch_time), end = "\r", flush = True)
        print("TIME %0.3f Sec" %stop_watch_time, end = "\r")



        if keyboard.is_pressed('space'):
            #wait_time_accum += wait_time

            #print(flush = True) #flush the buffer
            stop_time = time.perf_counter()
            #print("Stop time %0.2f" %stop_time, end = "\n", flush = True)
            #print("accum wait time: %0.2f" %wait_time_accum)
            #print("\n")
            do_something_once = 0

            break

        if keyboard.is_pressed('escape'):
            print("\n")
            quit()
