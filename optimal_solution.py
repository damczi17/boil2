import numpy as np
import math


def optimal_solution(maciez_zyskow, plan_transportu):
    alfa = np.linspace(np.NAN, np.NAN, num = len(maciez_zyskow))
    beta = np.linspace(np.NAN, np.NAN, num=len(maciez_zyskow[0]))


    alfa[len(maciez_zyskow)-1] = 0
    for i in reversed(range(len(maciez_zyskow))):
        for j in reversed(range(len(maciez_zyskow[i]))):
            if(plan_transportu[i][j] != 0):
                if(math.isnan(alfa[i])) and not (math.isnan(beta[j])):
                    alfa[i] = maciez_zyskow[i][j] - beta[j]
                elif not (math.isnan(alfa[i]) and math.isnan(beta[j])):
                    beta[j] = maciez_zyskow[i][j] - alfa[i]


    print("Alfa:")
    print(alfa)
    print("Beta:")
    print(beta)

    wskazniki_optymalnosci = np.zeros((len(maciez_zyskow), len(maciez_zyskow[0])))

    for i in range(len(wskazniki_optymalnosci)):
        for j in range(len(wskazniki_optymalnosci[i])):
            if(plan_transportu[i][j] == 0):
                wskazniki_optymalnosci[i][j] = maciez_zyskow[i][j] - alfa[i] - beta[j]
    
    print("Wskazniki optymalnosci:")
    print(wskazniki_optymalnosci)

    if(np.amax(wskazniki_optymalnosci) <= 0):
        return plan_transportu, True

    return profit_maximization(plan_transportu, wskazniki_optymalnosci), False




def profit_maximization(plan_transportu, wskazniki_optymalnosci):

    wiersze, kolumny = np.where(wskazniki_optymalnosci > 0.)
    wskazniki_optymalnosci[wskazniki_optymalnosci == 0.0] = np.nan

    for i, j in (zip(wiersze, kolumny)):
        lista_wiersze_zer = list((np.where(np.isnan(wskazniki_optymalnosci[i, :])))[0])
        lista_kolumny_zer = list((np.where(np.isnan(wskazniki_optymalnosci[:, j])))[0])

        for X in lista_wiersze_zer:
            for Y in lista_kolumny_zer:
                if (math.isnan(wskazniki_optymalnosci[Y, X])):

                    min_z_tras = min([plan_transportu[Y, X]],
                                      plan_transportu[i, X],
                                      plan_transportu[Y, j])

                    plan_transportu[i, j] = plan_transportu[i, j] + min_z_tras
                    plan_transportu[Y, X] = plan_transportu[Y, X] + min_z_tras

                    plan_transportu[i, X] = plan_transportu[i, X] - min_z_tras
                    plan_transportu[Y, j] = plan_transportu[Y, j] - min_z_tras

    return plan_transportu
