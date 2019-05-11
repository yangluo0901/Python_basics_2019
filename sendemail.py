import getpass
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "yluodevelopment@gmail.com"
receiver_email = "yluo@raasnutritionals.com"
PORT = 465
pwd = input("Type in the password:")
context = ssl.create_default_context()
content = "<h1>I am trying to send email by python</h1>"
#  The Content-Disposition header field provides a suggestion to the receiver for how the content is to be processed.
#  The standard dispositions are "inline" and "attachment".
#
# A disposition of "attachment" indicates the content is something to be saved to a file and not processed (such as
# rendering for viewing inline). A disposition of "inline" indicates the content should be processed (displayed)
# inline with the other parts of the MIME message.
#
# For example, an email client could handle a JPG image based on the disposition.
# If the disposition is "attachment", the email client (such as Thunderbird, GMail, or Outlook)
# might simply list the JPG image as one of the email's attachments, but won't display the JPG image.
#
# If the disposition is "inline", the email client might display the JPG image, but not list it as an attachment.
#
# The Content-Disposition header field can also include a "filename" attribute.  This is the suggested default
# filename if the content is to be saved to a file. msg = MIMEText(content, "html")
''' as.string()  
 |
 +------------MIMEMultipart  
              |                                                |---content-type  
              |                                   +---header---+---content disposition  
              +----.attach()-----+----MIMEBase----|  
                                 |                +---payload (to be encoded in Base64)
                                 +----MIMEText'''

'''The "octet-stream" subtype is used to indicate that a body contains
arbitrary binary data.  '''

msg = MIMEMultipart("mixed")
msg["Subject"] = "email_python_text"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.attach(MIMEText(content, "html"))
# set up attachment
with open("test.txt", "rb") as file:
    attachment = MIMEBase("application", "octet-stream")  # initialize a MIMEBase instance with maintype and subtype
    attachment.set_payload(file.read())  # set the content

encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename='test.txt')  # see comment above
msg.attach(attachment)


with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(sender_email, pwd)
    server.sendmail(sender_email, receiver_email, msg.as_string())
