import time
import keyboard
import sys

delay = .2

print("==========Welcome to the stop watch==========")
print("Instructions:")
print("1) Press 'space bar' to Start/Stop timer")
print("2) Press 'r' to reset timer")
print("3) Press 'Esc' to exit program\n")

start_time = 0
stop_time = 0
wait_time_accum = 0
do_something_once = 0
keep_going = True

while True:
    if keep_going == False:
        start_time = 0
        stop_time = 0
        wait_time_accum = 0
        do_something_once = 0
        keep_going = True
    else:
        while keep_going:
            if keyboard.is_pressed('r'):
                time.sleep(delay)
                keep_going = False
                print("TIME 0.000 Sec", end = "\r")
                break
            if keyboard.is_pressed('escape'):
                quit()
            if keyboard.is_pressed('space'):
                time.sleep(delay)
                start_time = time.perf_counter()

                while keep_going:
                    # elapsed_time = time.perf_counter()
                    # running_time = (time.perf_counter() - start_time)
                    wait_time = (start_time-stop_time)

                    if do_something_once == 0:
                        wait_time_accum += wait_time
                        do_something_once = 1

                    stop_watch_time = (time.perf_counter() - wait_time_accum + delay)

                    #print("elapsed time: %0.2f wait time: %0.2f running time: %0.2f accum wait time: %0.2f TIME: %0.2f"
                    #            %(elapsed_time, wait_time, running_time, wait_time_accum, stop_watch_time), end = "\r", flush = True)
                    print("TIME %0.3f Sec" %stop_watch_time, end = "\r")

                    if keyboard.is_pressed('space'):
                        time.sleep(delay)
                        #wait_time_accum += wait_time

                        print(flush = True, end = "\r") #flush the buffer
                        stop_time = time.perf_counter()
                        #print("Stop time %0.2f" %stop_time, end = "\n", flush = True)
                        #print("accum wait time: %0.2f" %wait_time_accum)
                        #print("\n")
                        do_something_once = 0
                        break

                    if keyboard.is_pressed('r'):
                        keep_going = False
                        break

                    if keyboard.is_pressed('escape'):
                        quit()
