import numpy as np

def transport_cost(koszty_transportu, plan_transportu):
    koszt_transportu = 0

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[0])):
            koszt_transportu = koszt_transportu + (koszty_transportu[i][j] * plan_transportu[i][j])
    
    return koszt_transportu


def maciez_zyskow_jednostkowych(koszty_transportu, ceny_sprzedazy, koszty_zakupu):
    maciez_zyskow = np.zeros((len(koszty_transportu),len(koszty_transportu[0])))
    for i in range(len(maciez_zyskow)):
        for j in range(len(maciez_zyskow[i])):
            maciez_zyskow[i][j] = ceny_sprzedazy[j] - (koszty_zakupu[i] + koszty_transportu[i][j])
    # print(maciez_zyskow)
    return maciez_zyskow

def results(maciez_zyskow, plan_transportu, koszty_transportu, koszty_zakupu, ceny_sprzedazy):
    ZC, KT, KZ, PC = 0, 0, 0, 0
    for i in range(len(maciez_zyskow)):
        for j in range(len(maciez_zyskow[i])):
            ZC += plan_transportu[i][j] * maciez_zyskow[i][j]
    
    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[i])):
            KT += plan_transportu[i][j] * koszty_transportu[i][j]

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[i])):
            PC += plan_transportu[i][j] * ceny_sprzedazy[j]
    
    for i in range(len(koszty_transportu)):
        tmp = 0
        for j in range(len(koszty_transportu[i])):
            tmp += plan_transportu[i][j]
        KZ += tmp * koszty_zakupu[i]

    print(ZC)
    print(KT)
    print(KZ)
    print(PC)

    return ZC,KT,KZ,PC