def solution(number):
    liste = list()
    if number <= 0:
        return 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            liste.append(i)
        elif i % 3 == 0:
            liste.append(i)
        elif i % 5 == 0:
            liste.append(i)
    # return liste
    if len(liste) == 0:
        return 0
    from functools import reduce
    a = reduce(lambda x, y: x + y,liste)
    return a


