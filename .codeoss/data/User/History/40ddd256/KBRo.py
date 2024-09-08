from random import randint

def checklist():
    lis1 = []
    for i in range(0,100):
        a = randint(0,100)
        if(a%5==0):
            lis1.append(5)
            ind = lis1.index()
            print(ind)
