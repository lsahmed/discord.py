from random import randint

arr = "1234567890acdefghijklmnopqrstuvwyzABCDEFGHIJKLMOPQRSTUVWXYZb!@#$%^&*()_+:"
leng = int(input("Enter the length of your password: "))
for i in range(0,leng+1):
    a = randint(0,len(arr)-1)
    print(arr[a], end="")
print()