max_bodov = 30
pocet_bodov = int(input("zadaj pocet bodov: "))
percenta = (pocet_bodov / max_bodov * 100)
print(f"ziskal si {round(percenta, 2)}%")
#if percenta >= 90:
#print("Výborný")
#else:
#if percenta >= 75:
#print("Chválitebný")
#else:
#if percenta >= 50:
#print("Dobrý")
#else:
#if percenta >= 30:
#print("dostatočný")
#else:
#print("nedostatočný")
if percenta >= 90:
    print("výborný")
elif 75 <= percenta:
    print("chválitebný")
elif 50 <= percenta:
    print("dobrý")
elif 30 <= percenta:
    print("dostatočný")
else:
    print("nedostatočný")