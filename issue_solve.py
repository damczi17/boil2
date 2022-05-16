from optimal_solution import optimal_solution
from transport_plan import transport_plan
from calculation import *


def balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):

    plan_transportu = transport_plan(koszty_transportu, podaz,popyt)
    print(f'Koszt transportu: {transport_cost(koszty_transportu, plan_transportu)}')

    optimal_solution(koszty_transportu, plan_transportu)
    

def unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    
    maciez_zyskow = maciez_zyskow_jednostkowych(koszty_transportu, ceny_sprzedazy, koszty_zakupu)
    tmp_maciez_zyskow = np.zeros((len(maciez_zyskow)+1, len(maciez_zyskow[0])+1))
    sum_podaz, sum_popyt = sum(podaz), sum(popyt)

    podaz.append(sum_popyt)
    popyt.append(sum_podaz)

    for i in range(len(tmp_maciez_zyskow)):
        for j in range(len(tmp_maciez_zyskow[i])):
            if(i < len(maciez_zyskow) and j < len(maciez_zyskow[i])):
                tmp_maciez_zyskow[i][j] = maciez_zyskow[i][j]
            else:
                tmp_maciez_zyskow[i][j] = 0
    

    plan_transportu = transport_plan(tmp_maciez_zyskow, podaz, popyt)

    # optimal_solution(tmp_koszty_transportu, plan_transportu)
