# sifrovanie cezarovou sifrou
ret = input("zadaj retazec: ")
posun = int(input("zadaj posun pre kodovanie: "))
for i in range(len(ret)):
    print(f"{ret[i]}:{ord(ret[i])}")
    # print(f"ret[i]")

ret_kod = ""
for i in range(len(ret)):
    ret_kod += chr(ord(ret[i])+ posun)

print(f"Zakodovany retazec: {ret_kod}")