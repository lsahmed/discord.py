from random import randint
theN = int(randint(1,10))
count = 0
while(num!=theN):
   num = int(input("guess the number: "))
   if(num==theN):
    print(f"You guessed the number in {count} times")
    count = count+1