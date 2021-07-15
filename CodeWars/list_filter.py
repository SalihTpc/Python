def filter_list(c):
    liste = list()
    for i in c:
        if type(i) != str:
            liste.append(i)
    return liste


print(filter_list([1, 2, "a", "b"]))

def flitrele(z):
    return [i for i in z if not isinstance(i,str)]


print(flitrele([1, 2, "a", "b"]))
