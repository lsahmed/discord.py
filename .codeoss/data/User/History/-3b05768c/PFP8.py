# Password generator in python

from random import randint;
alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symb = "!@#$%^&*()_+:<>,./';][-=]"
nums = "1234567890"

leng = int(input("Enter your password length: "))

thepass = []
for i in range(0,leng+1):
    thepass = alpha[randint(0,len(alpha)-1)]
    thepass += symb[randint(0,len(symb)-1)]
    firstR = nums[randint(0,len(nums)-1)]
    thepass += firstR+(nums[randint(0,len(nums)-1)])

    print(thepass, end="")

print()
