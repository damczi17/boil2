import numpy as np
    
def unbalanced():
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

    return koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt

def balanced():
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

    podaz = ([int(50),int(70),int(30)])
    popyt = ([int(20),int(40),int(90)])

    return koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt