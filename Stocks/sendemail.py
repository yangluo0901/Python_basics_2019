import smtplib
import ssl
from email.mime.text import MIMEText


class SendEmail(object):
    HOST = "smtp.gmail.com"
    PORT = 465
    context = ssl.create_default_context()
    sender_address = "yluodevelopment.gmail.com"
    receiver_address = "yangluo0901@gmail.com"
    __pwd = "Ly19910901"

    def __init__(self):
        self.server = smtplib.SMTP_SSL(self.HOST, self.PORT, context=self.context)

    def send_email_create_db(self):
        message = MIMEText("<b>DataBase PythonDatabase is created, table Shares and Persons are initialized ! </b> ", "html")
        self.server.login(self.sender_address, self.__pwd)
        self.server.sendmail(self.sender_address, self.receiver_address, message.as_string())

    def send_email_update_db(self):
        message = MIMEText("<b>DataBase PythonDatabase is updated </b> ", "html")
        self.server.send(self.sender_address, self.receiver_address, message.as_string())

    def mail_conn_close(self):
        self.server.close()
