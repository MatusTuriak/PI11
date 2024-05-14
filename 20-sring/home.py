#2
# def sucet(retazec):
#     i = retazec.find('+')
#     return int(retazec[:i]) + int(retazec[i+1:])
#3
def sucet(retazec):
    vysl = 0
    while True:
        i = retazec.find('+')
        if i > 0:
            vysl += int(retazec[:i])
            retazec = retazec[i + 1:]
        else:
            return vysl + int(retazec)
