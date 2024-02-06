def sucet(x,y):
    return x + y

def parne(cislo):
    if cislo % 2 == 0:
        return "parne"
    else:
        return "neparne"

def prvocislo(cislo):
    prvocis = True
    for i in range(2,cislo):
        if cislo % i == 0:
            prvocis = False
    return prvocis


a = int(input("zadaj a: "))
b = int(input("zadaj b: "))
sucet = sucet(a, b)
print(f"súčet čísel {a} + {b} = {sucet}")
print(f"Číslo {a} je {parne(a)}")
print(f"Číslo {b} je {parne(b)}")
if prvocislo(a) == True:
    print(f"cislo {a} je prvocislo")
else:
    print(f"cislo {a} nie je prvocislo")
if prvocislo(b) == True:
    print(f"cislo {b} je prvocislo")
else:
    print(f"cislo {b} nie je prvocislo")