import numpy as np


def transport_cost(koszty_transportu, plan_transportu):
    koszt_transportu = 0

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[0])):
            koszt_transportu = koszt_transportu + (koszty_transportu[i][j] * plan_transportu[i][j])
    
    return koszt_transportu

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


def array_modify(arr1, i, arr2, j, plan_transportu, a, b):
    plan_transportu[a][b] = arr2[j]
    arr1[i] = arr1[i] - arr2[j] 
    arr2[j] = arr2[j] - plan_transportu[a][b]


def index_return(maciez_zyskow, a, popyt, podaz):
    if(podaz[a] == 0):
        return -1
    if(a < len(maciez_zyskow)-1):
        tab = sorted(maciez_zyskow[a][:-1], reverse=True)
        for i in range(len(tab)):
            for j, k in enumerate(maciez_zyskow[a]):
                if k == tab[i]:
                    index = j
            if(popyt[index] != 0):
                return int(index)
    else:
        return -2
        

def transport_plan(maciez_zyskow, podaz, popyt):
    
    plan_transportu = np.zeros((len(maciez_zyskow), len(maciez_zyskow[0])))
    tmp_podaz, tmp_popyt = podaz, popyt


    for i in range(len(maciez_zyskow)):
        for j in range(len(maciez_zyskow[i])):
            index = index_return(maciez_zyskow, i, tmp_popyt, tmp_podaz)
            if(index == -2):
                index = j
            if(index == -1):
                break
            else:
                if(tmp_podaz[i] <= tmp_popyt[index]):
                    array_modify(tmp_popyt, index, tmp_podaz, i, plan_transportu, i, index)
                else:
                    array_modify(tmp_podaz, i, tmp_popyt, index, plan_transportu, i, index)

    print("Podaz:")
    print(tmp_podaz)
    print("Popyt:")
    print(tmp_popyt)
    print("Transport:")
    print(plan_transportu)

    return plan_transportu

def maciez_zyskow_jednostkowych(koszty_transportu, ceny_sprzedazy, koszty_zakupu):
    maciez_zyskow = np.zeros((len(koszty_transportu),len(koszty_transportu[0])))
    for i in range(len(maciez_zyskow)):
        for j in range(len(maciez_zyskow[i])):
            maciez_zyskow[i][j] = ceny_sprzedazy[j] - (koszty_zakupu[i] + koszty_transportu[i][j])
    # print(maciez_zyskow)
    return maciez_zyskow

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


def task_check(podaz,popyt):
    sum1, sum2 = 0, 0
    for i in range(len(podaz)):
        sum1 = sum1 + podaz[i]
        
    for i in range(len(popyt)):
        sum2 = sum2 + popyt[i]
    
    if(sum1 == sum2):
        print(f'Podaż = {sum1}, popyt = {sum2} - Zadanie jest zbilansowane')
        return 1
    else:
        print(f'Podaż = {sum1}, popyt = {sum2} - Zadanie jest niezbilansowane')
        return 0


def main():

    #Niezbilansowane https://docplayer.pl/112982574-Rozwiazanie-zadania-1-krok-tym-razem-naszym-celem-jest-nie-tak-jak-w-przypadku-typowego-zadania-transportowego.html?fbclid=IwAR3gNDxifXaewfWMn8DVIJh-tJHKMFF43JYZbBDcdV5thCl9pukAUrxGUFU
    D = 2
    O = 3
    koszty_transportu = np.zeros(shape=(D, O))
    ceny_sprzedazy = np.zeros([O])
    koszty_zakupu = np.zeros([D])
    podaz = np.zeros([D])
    popyt = np.zeros([O])

    koszty_transportu[0][0] = int(8)
    koszty_transportu[0][1] = int(14)
    koszty_transportu[0][2] = int(17)
    koszty_transportu[1][0] = int(12)
    koszty_transportu[1][1] = int(9)
    koszty_transportu[1][2] = int(19)

    ceny_sprzedazy = ([int(30),int(25),int(30)])
    koszty_zakupu = ([int(10),int(12)])
    podaz = ([int(20),int(30)])
    popyt = ([int(10),int(28),int(27)])

    #Zabilansowane http://tarapata.strefa.pl/p_ekonometria/download/ekonometria_cz3_4.pdf
    # D = 3
    # O = 3
    # koszty_transportu = np.zeros(shape=(D, O))
    # ceny_sprzedazy = np.zeros([O])
    # koszty_zakupu = np.zeros([D])
    # podaz = np.zeros([D])
    # popyt = np.zeros([O])

    # koszty_transportu[0][0] = int(3)
    # koszty_transportu[0][1] = int(5)
    # koszty_transportu[0][2] = int(7)
    # koszty_transportu[1][0] = int(12)
    # koszty_transportu[1][1] = int(10)
    # koszty_transportu[1][2] = int(9)
    # koszty_transportu[2][0] = int(13)
    # koszty_transportu[2][1] = int(3)
    # koszty_transportu[2][2] = int(9)

    # podaz = ([int(50),int(70),int(30)])
    # popyt = ([int(20),int(40),int(90)])

    print("Jednostkowe koszty transportu:")
    print(koszty_transportu)
    # print(ceny_sprzedazy)
    # print(koszty_zakupu)
    print("Podaz:")
    print(podaz)
    print("Popyt:")
    print(popyt)


    if(len(podaz) != len(koszty_transportu) or len(popyt) != len(koszty_transportu[0])):
        print("Bledne dane!!")
        return 1

    if(task_check(podaz,popyt) == 1):
        balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)
    else:
        unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)


if __name__ == "__main__":
    main()



