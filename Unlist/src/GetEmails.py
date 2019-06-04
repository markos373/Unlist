import requests
import imaplib
#from apiclient import errors

"""
def DeleteMessage(service, user_id, msg_id):

  This method deletes a specific email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
             can be used to indicate the authenticated user.
    msg_id: ID of Message to delete.

  try:
    service.users().messages().delete(userId=user_id, id=msg_id).execute()
    print("Message with id:", msg_id, "deleted successfully.")
  except errors.HttpError, error:
    print("An error occurred:", error)
"""

def login_with_cached_url(gmail):
    try:
        url = "https://mail.google.com/mail/u/?authuser={}".format(gmail)
    except:
        print("An error occurred")


if __name__ == "__main__":

    FIRST = "RCOS"
    LAST = "Unlist"
    GMAIL = "unlist.RCOS@gmail.com"
    PASSWORD = "RCOS_unlist!"

"""
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    EMAIL_ADDRESS =
    EMAIL_PASSWORD =

    # Use imap module to connect to SMTP sever over SSL
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    except Exception as e:
        print("Error trying to login to", EMAIL_ADDRESS)

    # Go to inbox and get list of ids for each email in the account
    try:
        mail.select("inbox")
        type, data = mail.search(None, "ALL")
        mail_ids = data[0]
        id_list = mail_ids.split()
        all_email_ids = [int(id) for id in id_list]
    except Exception as e:
        print(str(e))
"""
