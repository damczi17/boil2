from data import *
from task_check import task_check
from issue_solve import *


def start(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt):
    
    # koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt = balanced()

    # koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt = unbalanced()

    print("Jednostkowe koszty transportu:")
    print(koszty_transportu)
    print("Ceny sprzedazy:")
    print(ceny_sprzedazy)
    print("Koszty zakupu")
    print(koszty_zakupu)
    print("Podaz:")
    print(podaz)
    print("Popyt:")
    print(popyt)


    if(len(podaz) != len(koszty_transportu) or len(popyt) != len(koszty_transportu[0])):
        print("Bledne dane!!")
        return 1

    if(task_check(podaz,popyt) == 1):
        balanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)
        return 0,0,0,0
    else:
        result = unbalanced_issue(koszty_transportu, ceny_sprzedazy, koszty_zakupu, podaz, popyt)
        return result
