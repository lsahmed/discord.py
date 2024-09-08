from random import randint
theN = int(randint(1,5))
print(theN)
count = 0
num = -1
while(num!=theN):
   num = int(input("guess the number: "))
   if(num==theN):
    print(f"You guessed the number in {count} times")
    count = count+1