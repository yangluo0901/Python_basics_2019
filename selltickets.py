import threading
import random

ticket_amount = 2000
lock = threading.Lock()


def sell_tickets(window_num):
    global ticket_amount

    for count in range(100):
        ticket_num = random.randint(1, 3)
        lock.acquire()
        print(f" {window_num} is selling  tickets ---------")
        ticket_amount = ticket_amount - ticket_num
        print(f" {window_num}: {ticket_num} tickets sold, {ticket_amount} tickets left ----------")
        lock.release()


windows_1 = threading.Thread(target=sell_tickets, args=("window_1",))
windows_2 = threading.Thread(target=sell_tickets, args=("window_2",))
windows_1.start()
windows_2.start()
windows_1.join()
windows_2.join()

print(f" selling ends, {ticket_amount} tickets left ------------")
'''
main tread -- window_1 created --- windows_2 created --- win1_start         win2_start         ----                     ----                 -------------    
                                                                 +                  +             win1_join                win2_join
                                                                 +                  +
                                                                 +                  +
                                                                 +                  +    
                                                                 +                  ++++++++++++++++++++++++++++++++++++++++ join +++++ win2_end
                                                                 +
                                                                 +
                                                                 +
                                                                 +++++++++++++++++++++++++++++++++ join++++++++++++ win1_end
           
              
'''