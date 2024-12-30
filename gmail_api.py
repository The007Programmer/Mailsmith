from simplegmail import Gmail

# Specify the path to the client secret file
client_secret_path = 'secrets/client_secret.json'

# Initialize Gmail with the specified client secret file path
gmail = Gmail(client_secret_file=client_secret_path)

# Rest of your code to read emails
class Email:
    def __init__(self):
        '''
        Defining all the variables
        '''
        pass

    def send_msg(self):
        '''
        Sends a message using params.
        '''

        self.RECIPIENT = input("Recipient?   ")
        self.SENDER = input("From?   ")
        self.CC = input("Enter people to CC; separate by 1 space:  ").split(' ')
        self.BCC = input("Enter people to BCC; separate by 1 space:  ").split(' ')
        if self.CC == ['']:
            self.CC = []
        if self.BCC == ['']:
            self.BCC = []
        self.SUBJECT = input("Subject?   ")
        self.MSG = input("Message Content:   ")
        self.ATTACHMENTS = []
        self.SIGNATURE = False
        # Used CHATGPT to condense the full if statement into 1 line.
        SIGNATURE_Q = input("Do you want to use your default signature? (y/n; default y)    ").lower()
        if SIGNATURE_Q in ['y', 'Y', '']:
            self.SIGNATURE == True
        elif SIGNATURE_Q == ['f', 'F']:
            self.SIGNATURE == False
        else:
            self.SIGNATURE == True

        params = {
            "to": self.RECIPIENT,
            "sender": self.SENDER,
            "cc": self.CC,
            "bcc": self.BCC,
            "subject": self.SUBJECT,
            "msg_html": self.MSG,
            "attachments": self.ATTACHMENTS,
            "signature": self.SIGNATURE  # use my account signature
        }

        gmail.send_message(**params)


email = Email()

email.send_msg()