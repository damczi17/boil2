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