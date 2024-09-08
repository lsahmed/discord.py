# Password generator in python

from random import randint;
alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"

print(len(alpha))

thepass = ""
for i in range(0,len(alpha)+1):
    password = thepass+alpha[randint(0,len(alpha))]
    print(password, end="")