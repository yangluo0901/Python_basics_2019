import smtplib
import ssl
import time
from email.mime.text import MIMEText

import tushare

print(tushare.__version__)


class Share(object):
    def __init__(self, code):
        self.code = code
        self.name = ""
        self.price = ""
        self.amount = ""
        self.volume = ""
        self.sell_point = ""
        self.purchase_point = ""
        self.get_realtime_price()

    def get_realtime_price(self):
        data = tushare.get_realtime_quotes(self.code)  # type of data is <class 'pandas.core.frame.DataFrame'>
        self.name = data.loc[0][0]
        self.price = float(data.loc[0][3])
        self.volume = float(data.loc[0][8])
        self.amount = float(data.loc[0][9])

    def set_sell_purchase_point(self, sell_point, purchase_point):
        self.sell_point = float(sell_point)
        self.purchase_point = float(purchase_point)


def monitor(*shares):
    # while True:
    for share in shares:
        share.get_realtime_price()
        current_price = share.price
        content = f"<h3>Stock name: {share.name},\t Current price is {share.price}\n</h3>"
        print("Name: {} , Current price is  {}".format(share.name, current_price))
        subject = ""
        if current_price <= share.purchase_point:
            content += "<b><i>Price is low, purchase now !</i></b>"
            subject = "Time to purchase !!!"
            sendmsg(content, subject)
        elif current_price > share.sell_point:
            subject = " Time to sell !!!"
            content += "<b><i>Do not wait until the last minute, sell it !</i></b>"
            sendmsg(content, subject)
        else:
            content += "<b><i>Nothing special !</i></b>"
        print(content)

    # time.sleep(10)


def sendmsg(content, subject):
    sender_email = "yluodevelopment@gmail.com"
    receiver_email = "yangluo0901@gmail.com"
    PORT = 465
    PASSWORD = "Ly19910901"
    SENDER_HOST = "smtp.gmail.com"
    context = ssl.create_default_context()
    msg = MIMEText(content, "html")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    with smtplib.SMTP_SSL(SENDER_HOST, PORT, context=context) as server:
        server.login(sender_email, PASSWORD)
        server.sendmail(sender_email, receiver_email, msg.as_string())


share_code_list = ["000591", "600106", "601988"]
share_1 = Share(share_code_list[0])
share_1.set_sell_purchase_point(3.5, 3.6)
share_2 = Share(share_code_list[1])
share_2.set_sell_purchase_point(3.1, 3.9)
share_3 = Share(share_code_list[2])
share_3.set_sell_purchase_point(3.0, 3.2)
monitor(share_1, share_2, share_3)
