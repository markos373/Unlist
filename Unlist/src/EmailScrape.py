import imaplib
import email
import smtplib
import time


FROM_EMAIL  = ""
FROM_PWD    = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# This function is adapted from the link 
# https://codehandbook.org/how-to-read-email-from-gmail-using-python/
# Used to connect and parse emails from gmamil
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        print(first_email_id)
        print(latest_email_id)
        for i in range(latest_email_id,latest_email_id-1, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
            print(data)
            file = open("body.html", "w")
            file.write(data)
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    

    except Exception, e:   
        print str(e)

if __name__ == "__main__":
    with open('credentials.txt') as f:
        credentials = [x.strip().split(':', 1) for x in f]
    FROM_EMAIL = credentials[0][0]
    FROM_PWD = credentials[0][1]
    read_email_from_gmail()