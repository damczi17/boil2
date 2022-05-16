import numpy as np

def equation_solve(alfa, i, beta, j, koszty_transportu):
    if(alfa[i] == 0):
        alfa[i] = -1 * (beta[j] + koszty_transportu)
    if(beta[j] == 0):
        beta[j] = -1 * (alfa[i] + koszty_transportu)
    
def optimal_solution(koszty_transportu, plan_transportu):
    alfa = np.linspace(1, 1, num = len(koszty_transportu))
    beta = np.linspace(1, 1, num=len(koszty_transportu[0]))

    for i in reversed(range(len(koszty_transportu))):
        for j in reversed(range(len(koszty_transportu[i]))):
            if(plan_transportu[i][j] != 0):
                if(i == len(koszty_transportu)-1):
                    beta[j] = -1 *  koszty_transportu[i][j]
                    alfa[i] = 0.
                else:
                    equation_solve(alfa, i, beta, j, koszty_transportu[i][j])

    print("Alfa:")
    print(alfa)
    print("Beta:")
    print(beta)

    wskazniki_optymalnosci = np.zeros((len(koszty_transportu), len(koszty_transportu[0])))

    for i in range(len(wskazniki_optymalnosci)):
        for j in range(len(wskazniki_optymalnosci[i])):
            if(plan_transportu[i][j] == 0):
                wskazniki_optymalnosci[i][j] = koszty_transportu[i][j] + alfa[i] + beta[j]
    
    print("Wskazniki optymalnosci:")
    print(wskazniki_optymalnosci)