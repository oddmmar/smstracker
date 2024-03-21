# SMS Tracker

The program monitors a directory for new SMS files, extract information from those files using the SMSProc class, store the information in an SQLite3 database using the DBHandler class, and move the processed files to different directories (READ_DIR, OUTGOING_DIR, or FAILED_DIR).
Additionally, it provides a command-line interface for users to interact with the program, such as viewing connected GSM cards, sending SMS messages, and managing auxiliary tools.

**Note:** Certain parts are unimplemented. Overall, the code provides a foundation for an SMS monitoring and management system.

`main.py:` This file contains the main program logic. It includes functions for displaying messages, handling user input, monitoring directories for new SMS files, sending SMS messages, and managing auxiliary tools. The main() function is the entry point of the program and handles command-line arguments and user interactions.

`smsprocess.py:` This file contains the SMSProc class, which is used to extract essential information from an SMS file, such as the phone number, date and time received, and the content of the SMS.

`db_handler.py:` This file contains a DBHandler class that provides methods to interact with an SQLite3 database. It supports creating a table, inserting, updating, deleting, and querying records. It also includes a test() function to demonstrate the usage of the class.
