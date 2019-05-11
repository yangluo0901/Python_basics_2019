# num_list = [10, 9, 0, 4, 7]
# for num in num_list:
#     print("---------", num)
#     try:
#         print(format(3 / num, ".2f"))
#     except Exception as e:
#         print(e)
#     else:  # only runs when no exception presents
#         print(" running good !")
#     finally:  # always runs, no matter if exceptions present
#         print("done !")

correct_pwd = 000000
while True:
    pwd = input("Please enter the password :")
    if int(pwd) != correct_pwd:
        e = Exception("Incorrect password")
        raise e
    else:
        print("Logged In !")