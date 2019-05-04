from urllib import request
import webbrowser
import os
url = "http://www.google.com"
# data = request.urlopen(url).read()
# print(data)
# webbrowser.open(url)
# os.system(r"C:\Windows\system32\SnippingTool")

# file read

# f = open(r"G:\Python_Project\Python_basics\test.txt", "r", encoding="utf16")  # similar with stream in java
# # read_data = f.read()
# # read_data = f.readlines()
# # print(read_data)
# for line in f:
#     print(line)
# f.close()

# write file
# w = open(r"G:\Python_Project\Python_basics\test.txt", "w", encoding="utf16")
# # w.write(" 我在写 。。。\n")
# # w.write(" 我在写 。。。\n")
# # w.write(" 我在写 。。。\n")


# append file
# w = open(r"G:\Python_Project\Python_basics\test.txt", "a", encoding="utf16")
# w.write("I am appending ...")
# w.close()


# read binary file

with open(r"G:\Python_Project\Python_basics\lee_sin.jpg", "rb") as rb:
    read_data = rb.read()
    # print(read_data)

with open(r"G:\Python_Project\Python_basics\lee_sin_copy.jpg", "wb") as wb:
    wb.write(read_data)

