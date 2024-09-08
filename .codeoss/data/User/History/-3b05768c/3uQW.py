# Password generator in python

from random import randint;
alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symb = "!@#$%^&*()_+{}:<>,./';][-=]"

leng = int(input("Enter your password length: "))

thepass = []
for i in range(0,leng+1):
    thepass = alpha[randint(0,len(alpha)-1)]
    thepass += symb[randint(0,len(symb)-1)]
    print(thepass, end="")
