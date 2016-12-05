'''
This is a class that creates phone opject with a phone number,
cell provider, and a correct email to that phone number. 
'''

class Phone:
    #constructer using phone number and cell provider
    def __init__(self, num, provider):
        self.number = num
        self.provider = provider
        self.email = self.generate_email()

    '''
    This function will provide the correct email address
    based on the cell provider information.
    Will return an empty string if the cell provider is invalid. 
    '''
    def generate_email(self):
        if(self.provider == "T-Mobile"):
            return "+1" + self.number + "@tmomail.net"
        elif(self.provider == "Verizon"):
            return self.number + "@vtext.com"
        elif(self.provider == "AT&T"):
            return self.number + "@mms.att.net"
        elif(self.provider == "Sprint"):
            return self.number + "@messaging.sprintpcs.com"
        elif(self.provider == "US Cellular"):
            return self.number + "@email.uscc.net"
        return ""
