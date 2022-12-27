
def is_exit_loop(tase):
    if tase == "q":
        exit(0)

while True:
    tase = input("(Sisesta q väljumiseks) Sisesta tase: tase1, tase2, tase3: ")
    is_exit_loop(tase)

    
    if tase == "tase1" or tase == "tase2" or tase == "tase3":
        break

    print("vale tase, sisesta: tase1, tase2, tase3")






