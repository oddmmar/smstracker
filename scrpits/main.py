#!/usr/bin/python

"""
    TO-DO:
                                                                                                            DONE | NOT DONE
    - cli arguments                                                                                            x |
    - Input validation using regular expression.                                                                 | x
    - start a monitoring thread: https://www.tutorialspoint.com/python3/python_multithreading.htm                | x
    - multiprocessing instead: https://docs.python.org/2/library/multiprocessing.html#module-multiprocessing    x |
    
    NOTES:
    Colorama    CYAN:   input prompts
                RED:    input error
                
"""
import sys, os                      # System-specific parameters and functions
import argparse                     # Parser for command-line options, arguments and sub-commands
import multiprocessing              # Process-based parallelism
import shutil                       # High-level file operations: copy, removal etc....
import random                       # Generate pseudo-random numbers
import subprocess                   # Subprocess management
import time                         # Time access and conversions
from datetime import datetime       # Basic date and time types
from smsprocess import SMSProc      # Local module for processing SMS object (custom)
from db_handler import DBHandler    # Local module for interacting with a database.
from colorama import *              # colourise cli output: https://pypi.python.org/pypi/colorama


# constatnts
SLEEP_DELAY = 0.5
# setting directories
INCONIMG_DIR = r'../dirs/incoming'
OUTGOING_DIR = r'../dirs/outgoing'
READ_DIR = r'../dirs/read'
FAILED_DIR = r"../dirs/failed"
# setting databse - SQLite3
DB_FILENAME = r'../common/smsdb.sqlite3'
IN_TABLE = r'incomingsms'
OUT_TABLE = r'outgoingsms'
# seting databse tables
IN_DB = DBHandler(filename = DB_FILENAME, table = IN_TABLE)
OUT_DB = DBHandler(filename = DB_FILENAME, table = OUT_TABLE)


"""
    General purpose printing function. Requires three arguments: 
        message - the message to be displayed
        cards - number of cards connected
        aux_status - running status for the auxilary tools.
"""
def display(message="N\A", cards="N/A", aux_status="N/A"):
    subprocess.call("clear", shell=True)
    print("\nConnected Cards: {0}\t\t\tAux Tools Status: {1}".format(cards, aux_status))
    print("-"*62, "\n")
    print("{0}".format(message))
    print("\n")
    
"""
    
"""
def main_menu():    
    message = "SMS Tracker is a program that reads SMS messages from\nconnected GSM/3G modem(s)."
    message += "\n"
    message += "\nMake your choice from the following options:"
    message += "\n"
    message += "\ni\tFor live input monitoring."
    message += "\ns\tCompose an SMS to be sent. Ensure that the modems\n\thave airtime."
    message += "\nc\tList connected usb 3G/GSM modems."
    message += "\na\tStart auxliaray tools if not already running."
    message += "\nr\tRestart auxliaray tools."
    message += "\nx\tStop auxliaray tools."
    message += "\nd\t**Default**"
    message += "\nq\tQuit SMS Tracker but leave the auxilary tools running."
    display(message)
    
    userInput = input(Fore.CYAN + "Enter your selection: ")
    return(userInput)

"""
"""
def directory_monitor():
    while True:
        for inFilename in os.listdir(INCONIMG_DIR):
            if(os.path.basename(inFilename)):
                sms = inFilename
                
                newmsg = SMSProc('{0}{1}{2}'.format(INCONIMG_DIR, os.sep, sms))
                date_time_str = newmsg.getDateReceived() + ' ' + newmsg.getTimeReceived()
                # create correctly formated datetime obkect for db
                date_time_rec = datetime.strptime(date_time_str, '%y-%m-%d %H:%M:%S')
                # create db record
                record = {'sms_content': newmsg.getContent(),
                          'sms_sender': newmsg.getPhoneNumber(),
                          'sms_timestamp': date_time_rec,
                }
                
                print("SMS: {0}".format(record))
                
                # record into db
                IN_DB.insert(record)
                 # move the SMS from incoming to read folder
                shutil.move('{0}{1}{2}'.format(INCONIMG_DIR, os.sep, sms),
                                '{0}{1}{2}'.format(READ_DIR, os.sep, sms))
                
    #             print("{0}\n".format(inFilename))
    #             return filename
    
        time.sleep(SLEEP_DELAY)
"""

"""
def input_monitoring():
    message = "This would be monitoring inputs if there were any to begin with.\n"
    display(message)
     
    userInput = ""
    while userInput != "q":
        userInput = input("Enter 'q' to return to the main menu: ")
        
        if userInput == "q":
            continue
        
        time.sleep(SLEEP_DELAY)
        
"""
"""
def send_sms():
    message = """Please provide the following information: 
\nSender's name.
Recipient's number.
SMS Content."""
    display(message)
    
    input_prompt = """NOTE! The information should be in the following format:
Recipient's number; Sender's name; SMS content \nor 'q' to return to the main menu.\n\n"""
    
    userInput = input(input_prompt)
    
    if userInput.upper() == 'Q':
        pass
    else:
        # check formatiing for SMS entry
        pass
    

"""
"""
def view_cards():
    message = "Currently the system has the following cards installed."
    display(message)

"""
"""
def auxilary(actionRequeset="0"):
    if actionRequeset == "start":
        message = "a start request was issued."
    elif actionRequeset == "restart":
        message = "a restart request was issued."
    elif actionRequeset == "stop":
       message = "a stop request was issued." 
    
    display(message)

"""
"""
def default():
    pass
        
def main():
    # console reset to default
    init(autoreset=True)
    try:
        # initialise program by reading arguments if any    
        #* system argument tutorial:    https://docs.python.org/3.5/howto/argparse.html#id1 *
        parser = argparse.ArgumentParser(description="""SMS Tracker is a program that reads SMS messages from 
                                                        connected GSM/3G modems. supply only one argument at a time.""")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-i", "--input", action="store_true", 
                            help="for displaying new messages as they come in and are processed.")
        group.add_argument("-s", "--send", action="store_true", 
                            help="will allow you to send a new SMS by providing all the required information.")
        group.add_argument("-c", "--card", action="store_true", 
                            help="will allow you to view all connected cards.")
        group.add_argument("-a", "--aux", action="store_true", 
                            help="will allow you to start auxilary tools if not already running.")
        group.add_argument("-r", "--raux", action="store_true", 
                            help="will allow you to restart auxilary tools.")
        group.add_argument("-x", "--saux", action="store_true", 
                            help="will allow you to stop auxilary tools if running.")
        group.add_argument("-d", "--default", action="store_true", 
                            help="will allow you to view general statistcs when the program is running")
        # group.add_argument("-q", "--quit", action="store_true", 
        #                    help="will allow you to quit the program but not auxilary tools.")
        args = parser.parse_args()
                
        # Start multprocesing to continuosly monitor SMS folders
        monitorProc = multiprocessing.Process(target=directory_monitor)
        monitorProc.start()
        
        if args.input:
            input_monitoring()
        if args.send:
            send_sms() 
        if args.card:
            view_cards() 
        if args.aux:
            auxilary("start") 
        if args.raux:
            auxilary("restart") 
        if args.saux:
            auxilary("stop")  
        if args.default:
            default()
               
        # program loop
        while True:
            userInput = main_menu()
            if userInput == "i":
                input_monitoring()
            elif userInput == "s":
                send_sms() 
            elif userInput == "c":
                view_cards() 
            elif userInput == "a":
                auxilary("start")   
            elif userInput == "r":
                auxilary("restart") 
            elif userInput == "x":
                auxilary("stop") 
            elif userInput == "d":
                default() 
            elif userInput == "q":
                quit_confirmation = input("You have chosen to quit the program. Are you sure? y/n: ")
     
                if quit_confirmation.upper() == "Y":
                    subprocess.call("clear", shell=True)
                    print("bye...")
                    exit()
                elif quit_confirmation.upper() == "N":
                    continue
                else:
                    print("Your selections is incorrect. The program WILL NOT be quiting.")
                     
            else:
                print("Make sure to read the instruction properly, the input given is invalid.")
                time.sleep(SLEEP_DELAY)
                
            time.sleep(SLEEP_DELAY)
        
    except KeyboardInterrupt:
        print("User chose to terminate program: {0}".format(__file__))
        monitorProc.terminate()
        exit() 
            
if __name__ == '__main__':
    main()
