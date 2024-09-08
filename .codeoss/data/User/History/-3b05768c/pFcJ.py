# Password generator in python

from random import randint;
alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"


thepass = []
for i in range(0,len(alpha)+1):
    thepass = password = alpha[randint(0,len(alpha)-1)]
print(thepass)
