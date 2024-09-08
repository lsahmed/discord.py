# Password generator in python

from random import randint;
alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symb = "!@#$%^&*()_+{}:<>,./';][-=]"


thepass = []
for i in range(0,len(alpha)+1):
    thepass = alpha[randint(0,len(alpha)-1)]
    print(thepass, end="")
    print(i)
