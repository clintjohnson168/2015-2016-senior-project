
class Phone:
    def __init__(self, num, provider):
        self.number = num
        self.provider = provider
        self.email = self.generate_email()

    def generate_email(self):
        if(self.provider == "T-Mobile"):
            return "+1" + self.number + "@tmomail.net"
        if(self.provider == "Verizon"):
            return self.number + "@vtext.com"
        if(self.provider == "AT&T"):
            return self.number + "@mms.att.net"
        if(self.provider == "Sprint"):
            return self.number + "@messaging.sprintpcs.com"
        if(self.provider == "US Cellular"):
            return self.number + "@email.uscc.net"
        return "Can't generate email."
