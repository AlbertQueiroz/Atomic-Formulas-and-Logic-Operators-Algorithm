from atomics import atomicsQnt

atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

A = [['t','^',['~','x']],'>','a']

def truthTable(atomicsQnt):
    values = []
    count = 2**atomicsQnt
    qnt = 1
    for x in range(atomicsQnt):
        aux = []
        count = int(count/2)
        for y in range(count):
            aux.append(True)
        for z in range(count):
            aux.append(False)
        values.append(qnt*aux)
        qnt *= 2
    return values
