def hviezdy(pocet_riadkov, pocet_hviezd):#definicia funkcie
    for i in range(pocet_riadkov):
        for j in range(pocet_hviezd):
            print("*", end="")
    print()



hviezdy(2, 12)#volanie funkcie
print("hello")
hviezdy(1)
print("world")
hviezdy(5)