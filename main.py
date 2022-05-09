import numpy as np



def transport_cost(koszty_transportu, plan_transportu):
    koszt_transportu = 0

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[0])):
            koszt_transportu = koszt_transportu + (koszty_transportu[i][j] * plan_transportu[i][j])
    
    return koszt_transportu

def equation_solve(alfa, i, beta, j, koszty_transportu):
    if(alfa[i] == 0):
        alfa[i] = -1*(beta[j] + koszty_transportu)
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


def transport_plan(koszty_transportu, podaz, popyt):
    plan_transportu = np.zeros((len(koszty_transportu), len(koszty_transportu[0])))
    tmp_podaz, tmp_popyt = podaz, popyt

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[i])):
            if(tmp_podaz[i] <= tmp_popyt[j] and tmp_podaz[i] != 0):
                plan_transportu[i][j] = tmp_podaz[i]
                tmp_popyt[j] = tmp_popyt[j] - tmp_podaz[i]
                tmp_podaz[i] = tmp_podaz[i] - plan_transportu[i][j]
                break  #wyczerpalismy zasoby dostawcy, wiec pomijamy wiersz
            else:
                plan_transportu[i][j] = tmp_popyt[j]
                tmp_podaz[i] = tmp_podaz[i] - tmp_popyt[j]
                tmp_popyt[j] = tmp_popyt[j] - plan_transportu[i][j]

    print("Transport:")
    print(plan_transportu)

    return plan_transportu

def balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):

    plan_transportu = transport_plan(koszty_transportu, podaz,popyt)
    print(f'Koszt transportu: {transport_cost(koszty_transportu, plan_transportu)}')

    optimal_solution(koszty_transportu, plan_transportu)
    

def unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    tmp_koszty_transportu = np.zeros((len(koszty_transportu)+1, len(koszty_transportu[0])+1))
    podaz.append(sum(popyt))
    popyt.append(sum(popyt))

    for i in range(len(tmp_koszty_transportu)):
        for j in range(len(tmp_koszty_transportu[i])):
            if(i < len(koszty_transportu) and j < len(koszty_transportu[i])):
                tmp_koszty_transportu[i][j] = koszty_transportu[i][j]
            else:
                tmp_koszty_transportu[i][j] = 0
    

    plan_transportu = transport_plan(tmp_koszty_transportu, podaz, popyt)
    print(f'Koszt transportu: {transport_cost(koszty_transportu, plan_transportu)}')

    optimal_solution(tmp_koszty_transportu, plan_transportu)




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



