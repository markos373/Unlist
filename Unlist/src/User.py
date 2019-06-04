class User(object):

    def __init__(first, last, gmail):
        if ((first is None) or (last is None) or (gmail is None)):
            raise Exception("Argument has NULL value")
        if (!isGmail(gmail)):
            raise Exception("Email is not a valid gmail account")
        self.first_name = first
        self.last_name = last
        self.gmail = gmail

    def isGmail(email_address):
        substr = "@gmail.com"
        if (substr in email_address):
            return True
        else:
            return False

    def getFirst():
        return self.first_name

    def getLast():
        return self.last_name

    def getGmail():
        return self.gmail
