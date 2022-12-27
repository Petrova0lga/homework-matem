import random

def is_exit_loop(tase):
    if tase == "q":
        exit(0)

while True:
    tase = input("(Sisesta q väljumiseks) Sisesta tase: tase1, tase2, tase3: ")
    is_exit_loop(tase)

    
    if tase == "tase1" or tase == "tase2" or tase == "tase3":
        break

    print("vale tase, sisesta: tase1, tase2, tase3")

teg_num = input("(Sisesta q väljumiseks) Sisesta tegevuse number, näiteks +,-,/,*,**: ")
juh_num = input("(Sisesta q väljumiseks) Sisesta juhuslik number: ")
juh_num = int(juh_num)

juh_num1 = random.randint(0, juh_num)
juh_num2 = random.randint(0, juh_num)
mat_ops = teg_num.split(",")
print(mat_ops)










