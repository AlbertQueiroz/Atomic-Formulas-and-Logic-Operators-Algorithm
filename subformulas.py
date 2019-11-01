atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

#Se o trem chegou tarde e não tinha taxi na estação, então José chegou atrasado.
#(t^(~x))>a
F = [['t','^',['~','x']],'>','a']

def subformulas(F,atomics):
    if (F in atomics):
        return F
    if (F[1] not in atomics) & (type(F[1]) != list):
        print(F)
        return subformulas(F[0],atomics) + subformulas(F[2],atomics)
    if (F[0] == '~'):
        print(F)
        return F[1] + subformulas(F[1],atomics)

print("Subformulas")
subformulas(F,atomics)