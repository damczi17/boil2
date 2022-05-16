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