atomicos = ['a','b','c','d','e','f','g','h']

A = [['t','^',['~','x']],'>','a']

def conectivos(A, atomicos):
    if A in atomicos:
        return 0
    if type(A[1]) == str:
        return conectivos(A[0],atomicos) + 1 + conectivos(A[2],atomicos)
    if A[0] == '˜':
        return conectivos(A[1],atomicos)