atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

#(t^ (~x))>a
F = [['t','^',['~','x']],'>','a']

def subformulas(F,atomics):
    if F in atomics:
        return F
    if (F[1] not in atomics) & (type(F[1]) != list):
        print(F)
        return subformulas(F[0],atomics) + subformulas(F[2],atomics)
    if F[0] == '~':
        print(F)
        return F[1] + subformulas(F[1],atomics)

subformulas(F,atomics)