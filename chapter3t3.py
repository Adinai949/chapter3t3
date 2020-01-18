def shift():
    lst = list(input('Введите список элементов: '))
    steps = int(input('Введите количество шагов: '))
    print(lst)
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst
print(shift())