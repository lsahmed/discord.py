from random import randint
theN = int(randint(1,10))
print(theN)
count = 1
num = -1
while(num!=theN):
   count = count+1
   num = int(input("guess the number: "))
   if(num==theN):
    print(f"You guessed the number in {count} times")
