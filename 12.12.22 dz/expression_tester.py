import random

def vastus_kontroll(kasutaja_vastus, real_vastus, tase):
    if tase == "tase1":
        kasutaja_vastus = int(kasutaja_vastus)
        real_vastus = int(real_vastus)

    if tase == "tase2":
        kasutaja_vastus = round(kasutaja_vastus, 1)
        real_vastus = round(real_vastus, 1)

    if kasutaja_vastus == real_vastus:
        print("Õige vastus")
        return True

    print("Vale vastus")
    return False
    

def rakenda_math(operators, val1, val2, tase):
    oiged_vastused = []
    operators = operators.split(",")
    operator_pikkus = len(operators)

    for i in range(0, operator_pikkus):
        if operators[i] == "+":
            kusimus = "{val1} + {val2} = ".format(val1 = val1, val2 = val2)
            vastus = input(kusimus)
            vastus = float(vastus)
            real_vastus = val1 + val2

            oige_vastus = vastus_kontroll(kasutaja_vastus=vastus, real_vastus=real_vastus, tase=tase)
            oiged_vastused.append(oige_vastus)
            continue

        if operators[i] == "-":
            kusimus = "{val1} - {val2} = ".format(val1 = val1, val2 = val2)
            vastus = input(kusimus)
            vastus = float(vastus)
            real_vastus = val1 - val2

            oige_vastus = vastus_kontroll(kasutaja_vastus=vastus, real_vastus=real_vastus, tase=tase)
            oiged_vastused.append(oige_vastus)
            continue

        if operators[i] == "*":
            kusimus = "{val1} * {val2} = ".format(val1 = val1, val2 = val2)
            vastus = input(kusimus)
            vastus = float(vastus)
            real_vastus = val1 * val2

            oige_vastus = vastus_kontroll(kasutaja_vastus=vastus, real_vastus=real_vastus, tase=tase)
            oiged_vastused.append(oige_vastus)
            continue

        if operators[i] == "/":
            kusimus = "{val1} / {val2} = ".format(val1 = val1, val2 = val2)
            vastus = input(kusimus)
            vastus = float(vastus)
            real_vastus = val1 / val2

            oige_vastus = vastus_kontroll(kasutaja_vastus=vastus, real_vastus=real_vastus, tase=tase)
            oiged_vastused.append(oige_vastus)
            continue

        if operators[i] == "**":
            kusimus = "{val1} ** {val2} = ".format(val1 = val1, val2 = val2)
            vastus = input(kusimus)
            vastus = float(vastus)
            real_vastus = val1 ** val2

            oige_vastus = vastus_kontroll(kasutaja_vastus=vastus, real_vastus=real_vastus, tase=tase)
            oiged_vastused.append(oige_vastus)
            continue

        print("vale operator: {op}".format(op=operators[i]))
        exit(0)
    
    return oiged_vastused
        
while True:
    tase = input("(Sisesta q väljumiseks, default tase3) Sisesta tase: tase1, tase2, tase3: ")
    if tase == "q":
        exit(0)

    if tase == "":
        tase = "tase3"
    
    if tase == "tase1" or tase == "tase2" or tase == "tase3":
        break

    print("vale tase, sisesta: tase1, tase2, tase3")


teg_num = input("(Sisesta q väljumiseks) Sisesta tegevuse number, näiteks +,-,/,*,**: ")
juh_num = input("(Sisesta q väljumiseks) Sisesta juhuslik number: ")
juh_num = int(juh_num)

juh_num1 = random.randint(0, juh_num)
juh_num2 = random.randint(0, juh_num)

oiged_vastused = rakenda_math(teg_num, juh_num1, juh_num2, tase)
hinne = (oiged_vastused.count(True) / len(oiged_vastused)) * 100

print("tulemus: {tul}".format(tul=hinne))

if hinne < 60:
    print("hinne on 2")

if hinne >= 60 and hinne < 75:
    print("hinne on 3")

if hinne >= 75 and hinne <= 90:
    print("hinne: 4")

if hinne > 90:
    print("hinne on 5")




