import numpy as np

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