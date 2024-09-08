n = int(input("Enter your input: "))
for i in range(0,n):
    odi = 2*i-1
    print(" "(*n-i), end = "")
    print("*"*odi)