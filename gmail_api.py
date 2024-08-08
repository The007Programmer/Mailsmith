from simplegmail import Gmail

# Specify the path to the client secret file
client_secret_path = 'secrets/client_secret.json'
gmail_token_path = 'secrets/gmail_token.json'

# Initialize Gmail with the specified client secret file path
gmail = Gmail(client_secret_file=client_secret_path)

# Rest of your code to read emails
class Email:
    def __init__(self):
        '''
        Defining all the variables
        '''
        pass

    def send_msg(self, RECIPIENT, SENDER, SUBJECT, MSG, MSG2, CC=[], BCC=[], ATTACHMENTS=[], SIGN_TF=False):
        '''
        Sends a message using params.
        '''

        params = {
            "to": RECIPIENT,
            "sender": SENDER,
            "cc": CC,
            "bcc": BCC,
            "subject": SUBJECT,
            "msg_html": MSG,
            "attachments": ATTACHMENTS,
            "signature": SIGN_TF  # use my account signature
        }
        gmail.send_message(**params)


email = Email()


recipient = input("Recipient?   ")
sender = input("From?   ")
subject = input("Subject?   ")
msg = input("Message Content:   ")
msg2 = input("idk bruh:    ")
cc = input("Enter people to CC; separate by 1 space:  ").split(' ')
if cc == ['']:
    cc = []
bcc = input("Enter people to BCC; separate by 1 space:  ").split(' ')
if bcc == ['']:
    bcc = []
print(cc, bcc)
attachments = []
q_sign = input("T/F:   ")
if q_sign == ['T', 't']:
    sign_tf = True
elif q_sign in ['F', 'f', '']:
    sign_tf = False
else:
    exit()

email.send_msg(recipient, sender, subject, msg, msg2, cc, bcc, attachments, sign_tf)