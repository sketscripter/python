""" import random

def genrandomboard():
    rows1 = []
    rows2 = []
    rows3= []
    rows4 = []
    rows5 = []
    rows6 = []
    rows7 = []
    rows8 = []
    rows9 = []

    for i in range(81):
            if i in range(0,9):
                rows1.append(random.randint(0,9))
            if i in range(9,18):
                rows2.append(random.randint(0,9))
            if i in range(18,27):
                rows3.append(random.randint(0,9))
            if i in range(27,36):
                rows4.append(random.randint(0,9))
            if i in range(36,45):
                rows5.append(random.randint(0,9))
            if i in range(45,54):
                rows6.append(random.randint(0,9))
            if i in range(54,63):
                rows7.append(random.randint(0,9))
            if i in range(63,72):
                rows8.append(random.randint(0,9))
            if i in range(72,81):
                rows9.append(random.randint(0,9))

    for j in range (9):
        print (rows1[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows2[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows3[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows4[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows5[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows6[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows7[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows8[j]," ",end='')
    print("\n")
    for j in range (9):
        print (rows9[j]," ",end='')

genrandomboard()"""
print(test)
