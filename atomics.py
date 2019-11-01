atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

A = [['t','^',['~','x']],'>','b']

def atomicsQnt(A, atomics, rep=[]):  
    if (A in atomics and A not in rep):
        rep+=A
        return 1
    if(A in atomics and A in rep):
        return 0
    if (type(A[1]) == str and A[1] not in atomics):
        return atomicsQnt(A[0], atomics) + atomicsQnt(A[2],atomics)
    if (A[0] == '~'):
        return atomicsQnt(A[1], atomics)

def atomicas(A, atomics, rep = []):
    if (A in atomics and A not in rep):
        rep+=A
        return A
    if(A in atomics and A in rep):
        return ''
    if (type(A[1]) == str and A[1] not in atomics):
        return atomicas(A[0], atomics) + atomicas(A[2],atomics)
    if (A[0] == '~'):
        return atomicas(A[1], atomics)
