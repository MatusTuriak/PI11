ret = input("zadaj retazec: ")
samo = 0
for znak in ret:
    if znak in "aáeéiíoóuúyýä" :
        samo += 1
print(f"počet samohlások je {samo}")
