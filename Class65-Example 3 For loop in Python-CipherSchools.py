# practice for loop 
# ask user name and count each character
# "Sagar Bisht"
# S : 1
# a : 2
# g : 1
# r : 1
#   : 1 
# B : 1
# i : 1
# s : 1
# h : 1
# t : 1

name = input("Enter your name- ")
temp = ""
for i in range(len(name)):
    if name [i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]