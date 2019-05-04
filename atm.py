card_info = [{"card_num": 1001, "password": 1001, "balance": 1000},
    {"card_num": 1002, "password": 1002, "balance": 2000},
    {"card_num": 1003, "password":1003, "balance": 3000}]
print("Welcome to Python Bank !")
attempts = 0;
validation = True;
while validation:
    print("Please enter your card number :")
    input_card_num = int(input())
    card_exists = False
    for element in card_info:
            if input_card_num == element["card_num"]:
                password = element["password"]
                balance = element["balance"]
                card_exists = True;
                break
    if card_exists:
        attempts = 0
        while attempts < 3:
            print("Please enter your password :")
            input_password = int(input())
            if input_password == password:
                while True:
                    print("Please enter the service : 1. deposit \t 2. withdraw \t 3. exit")
                    service = int(input())
                    if service == 1:
                        print("Please enter the amount you want to deposit :")
                        deposit = int(input())
                        balance = balance + deposit
                        print("Depsoit {} successfully ! Your balance is {}".format(deposit,balance))
                    elif service == 2:
                        print("Please enter the amount you want to withdraw :")
                        withdraw = int(input())
                        if balance - withdraw < 0:
                            print("Not enough balance ! Your balance is {}".format(balance))
                        else:
                            balance  = balance - withdraw
                            print("withdraw {} successfully ! Your balance is {}".format(withdraw,balance))
                    elif service == 3:
                        break

                break
            else:
                attempts = attempts + 1
                if attempts ==3:
                    print("Your card is locked, please contact fraud center !")
                    validation = False
                    break
                else:
                    print("password is not correct, total 3 attmpts, you have {} left".format(3-attempts))
    else:
        print("Card number does not exists ! Please try it again !")
