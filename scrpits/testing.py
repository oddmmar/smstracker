import threading, multiprocessing
import time
from colorama import *

def print_time(msg="Nothing"):
    while True:
        time.sleep(1)
        print("Passed message: {0}".format(msg))
        print("*** Current time: {0} ***\n".format(time.ctime(time.time())))
        
def main():
    try:
        monitor_proc = multiprocessing.Process(target=print_time, args=("This is crazy",))
        monitor_proc.start()
        mainIter = 0
         
        while True:
            print(Fore.RED + "Main Iterration: {0}\n".format(mainIter))
            time.sleep(1)
            mainIter += 1
            
    except KeyboardInterrupt:
        print("User chose to terminate program: {0}".format(__file__))
        monitor_proc.terminate()
        exit()
        
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    