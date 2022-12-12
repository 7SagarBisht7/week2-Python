# if statement
name = "Sagar"
if name == "sagar" or name == "Sagar":
    print("You are Sagar")
elif name == "aman" or name =="Aman":
    print("You are aman")
else:
    print("You are not Sagar")

# while loop
i = 0
while i < 10:
    print("hello world")
    i+=1

i = 1
while i <= 10:
    print(i)
    i+=1

#  for loop
for i in range(1,11):
    print(i)
#  for skipping between numbers of 1
for i in range(1,11,2):
    print(i)

# break keyword
for i in range(1,11):
    if i==5:
        break
    print(i)

# continue keyword
for i in range(1,11):
    if i == 5:
        continue       
    print(i)

# for loop using string
for i in "Harsh":
    print(i)