# while True:
#     cislo = int(input("Zadaj cislo (pre ukoncenie zadaj 0): "))
#     if cislo == 0:
#         print("Číslo je nula!!!")
#         break
#     elif cislo % 2 == 0:
#         print("Párne")
#     else:
#         print("nepárne")

while True:
    cislo = int(input("Zadaj cislo (pre ukoncenie zadaj 0): "))
    pocet = 0
    print("Delitele:", end=" ")
    for delitel in range(1, cislo+1):
        if cislo % delitel == 0:
            print(delitel, end=" ")
            pocet += 1 # pocet = pocet + 1
    print()
    print("pocet delitelov je:", pocet)
    if pocet == 2:
        print("je to prvocislo")
    if cislo == 0:
        break
