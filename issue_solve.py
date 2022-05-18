from optimal_solution import optimal_solution
from transport_plan import transport_plan
from calculation import *

def balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):

    print(f'Zadanie zbilansowane, nie było w poleceniu')
    exit(1)

    
def unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    
    maciez_zyskow = maciez_zyskow_jednostkowych(koszty_transportu, ceny_sprzedazy, koszty_zakupu)
    tmp_maciez_zyskow = np.zeros((len(maciez_zyskow)+1, len(maciez_zyskow[0])+1))
    sum_podaz, sum_popyt = sum(podaz), sum(popyt)

    np.append(podaz, sum_popyt)
    np.append(popyt, sum_podaz)

    #podaz.append(sum_popyt)
    #popyt.append(sum_podaz)

    for i in range(len(tmp_maciez_zyskow)):
        for j in range(len(tmp_maciez_zyskow[i])):
            if(i < len(maciez_zyskow) and j < len(maciez_zyskow[i])):
                tmp_maciez_zyskow[i][j] = maciez_zyskow[i][j]
            else:
                tmp_maciez_zyskow[i][j] = 0
    

    plan_transportu = transport_plan(tmp_maciez_zyskow, podaz, popyt)
    print(plan_transportu)
    print(tmp_maciez_zyskow)
    print("Optymalne:")

    parametr = False
    while(parametr == True):
        plan_transportu, parametr = optimal_solution(tmp_maciez_zyskow, plan_transportu)
    #plan_transportu = optimal_solution(tmp_maciez_zyskow, plan_transportu)
    print(plan_transportu)

    # ZC = Zysk całkowity
    # KT = Koszt transportu
    # KZ = Koszt zakupu
    # PC = Przychód całkowity
    
    ZC,KT, KZ, PC = results(tmp_maciez_zyskow,plan_transportu, koszty_transportu, koszty_zakupu, ceny_sprzedazy)
