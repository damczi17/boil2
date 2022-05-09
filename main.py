import numpy as np
from mainWindow import mainWindow

def balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    transport_plan = np.zeros((len(koszty_transportu), len(koszty_transportu[0])))
    tmp_podaz, tmp_popyt = podaz, popyt

    if(len(podaz) != len(koszty_transportu) or len(popyt) != len(koszty_transportu[0])):
        print("Bledne dane!!")
        return 1

    
    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[0])):
            if(tmp_podaz[i] <= tmp_popyt[j] and tmp_podaz[i] != 0):
                transport_plan[i][j] = tmp_podaz[i]
                tmp_popyt[j] = tmp_popyt[j] - tmp_podaz[i]
                tmp_podaz[i] = tmp_podaz[i] - transport_plan[i][j]
                break 
            else:
                transport_plan[i][j] = tmp_popyt[j]
                tmp_podaz[i] = tmp_podaz[i] - tmp_popyt[j]
                tmp_popyt[j] = tmp_popyt[j] - transport_plan[i][j]

    print("Transport:")
    print(transport_plan)
    print("Popyt:")
    print(tmp_popyt)
    print("Podaz:")
    print(tmp_podaz)

    koszt_transportu = 0

    for i in range(len(koszty_transportu)):
        for j in range(len(koszty_transportu[0])):
            koszt_transportu = koszt_transportu + (koszty_transportu[i][j] * transport_plan[i][j])

    print(f'Koszt transportu: {koszt_transportu}')

    alfa = np.zeros(len(koszty_transportu))
    beta = np.zeros(len(koszty_transportu[0]))



def unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    print("dupa")

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

    mainWindow()

    #Niezbilansowane https://docplayer.pl/112982574-Rozwiazanie-zadania-1-krok-tym-razem-naszym-celem-jest-nie-tak-jak-w-przypadku-typowego-zadania-transportowego.html?fbclid=IwAR3gNDxifXaewfWMn8DVIJh-tJHKMFF43JYZbBDcdV5thCl9pukAUrxGUFU
    # D = 2
    # O = 3
    # koszty_transportu = np.zeros(shape=(D, O))
    # ceny_sprzedazy = np.zeros([O])
    # koszty_zakupu = np.zeros([D])
    # podaz = np.zeros([D])
    # popyt = np.zeros([O])

    # koszty_transportu[0][0] = int(8)
    # koszty_transportu[0][1] = int(14)
    # koszty_transportu[0][2] = int(17)
    # koszty_transportu[1][0] = int(12)
    # koszty_transportu[1][1] = int(9)
    # koszty_transportu[1][2] = int(19)

    # ceny_sprzedazy = ([int(30),int(25),int(30)])
    # koszty_zakupu = ([int(10),int(12)])
    # podaz = ([int(20),int(30)])
    # popyt = ([int(10),int(28),int(27)])

    #Zabilansowane http://tarapata.strefa.pl/p_ekonometria/download/ekonometria_cz3_4.pdf
    D = 3
    O = 3
    koszty_transportu = np.zeros(shape=(D, O))
    ceny_sprzedazy = np.zeros([O])
    koszty_zakupu = np.zeros([D])
    podaz = np.zeros([D])
    popyt = np.zeros([O])

    koszty_transportu[0][0] = int(3)
    koszty_transportu[0][1] = int(5)
    koszty_transportu[0][2] = int(7)
    koszty_transportu[1][0] = int(12)
    koszty_transportu[1][1] = int(10)
    koszty_transportu[1][2] = int(9)
    koszty_transportu[2][0] = int(13)
    koszty_transportu[2][1] = int(3)
    koszty_transportu[2][2] = int(9)

    # ceny_sprzedazy = ([int(30),int(25),int(30)])
    # koszty_zakupu = ([int(10),int(12)])
    podaz = ([int(50),int(70),int(30)])
    popyt = ([int(20),int(40),int(90)])

    print(koszty_transportu)
    # print(ceny_sprzedazy)
    # print(koszty_zakupu)
    print(podaz)
    print(popyt)

    if(task_check(podaz,popyt) == 1):
        balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)
    else:
        unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)


if __name__ == "__main__":
    main()



