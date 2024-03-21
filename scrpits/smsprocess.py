#!/usr/bin/python3.5

import re                   # Regular expression operations

class SMSProc():
    """
        Module for extracting the essential parts of a received sms. Argument 
        requied is the SMS/file location.
    """
    def __init__(self, sms_location):
        self.m_file = open(sms_location, 'r')
        self.m_sms = self.m_file.read()
        self.m_file.close()
        
    '''
        Exctract sender's phone number. Returned in the format: 27724761001.
        Type: string.
    '''
    def getPhoneNumber(self):
        phonenumber_regex = re.compile(r'\d{11}')
        match = phonenumber_regex.search(self.m_sms)
        return (match.group())

    '''
        Extract date contained in the SMS header. This is the date the SMS 
        was recieved by the card (GSM/3G Module). It is best used with the 
        'getTimeReceived' for a complete timestamp.
        Return a date in the format: %y-%m-%d (17-05-29).
        Type: string.
    '''
    def getDateReceived(self):
        date_regex = re.compile(r'\d{2}-\d{2}-\d{2}')
        match = date_regex.findall(self.m_sms)
        return (match[0])
    
    '''
        Extract time contained in the SMS header. This is the time the SMS 
        was recieved by the card (GSM/3G Module). It is best used with the 
        'getDateReceived' for a complete timestamp.
        Return a date in the format: %H:%M:%S (18:28:22).
        Type: string.
    '''
    def getTimeReceived(self):
        time_regex = re.compile(r'\d{2}:\d{2}:\d{2}')
        match = time_regex.findall(self.m_sms)
        return (match[0])
    
    '''
        Extract the actual SMS content. The content is returned without any 
        processing or formating. 
        Type: string.
    '''
    def getContent(self):
        content_regex = re.compile(r'Length: \d+\D\D(.*)')
        match = content_regex.findall(self.m_sms)
        return (match[0])


def main():
    newmsg = SMSProc(r'CARD1.jJMUTh')
    print(newmsg.getPhoneNumber())
    print(newmsg.getDateReceived())
    print(newmsg.getContent())


if __name__=='__main__' :
    main()