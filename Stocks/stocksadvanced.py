from share import Share
from dbmanager import DbManager
from person import Person
from sendemail import SendEmail
import time

db_manager = DbManager()
share_code_list = ["000591", "600106", "601988"]
shares = []  # share list
persons = [Person("Yang", "Luo"), Person("Ran", "Li")]


def set_up_db():
    for code in share_code_list:
        shares.append(Share(code))

    for share in shares:
        db_manager.add_share_entry(share)

    for person in persons:
        db_manager.add_person_entry(person)


def update_share_info():
    for share in shares:
        share.update()
        db_manager.update_share_entry(share)


set_up_db()
send_email = SendEmail()
send_email.send_email_create_db()
time.sleep(5)
update_share_info()
send_email.send_email_update_db()
db_manager.close()
send_email.mail_conn_close()