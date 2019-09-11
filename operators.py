atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

#(t^ (~x))>a
A = [['t','^',['~','x']],'>','a']

def operators(A, atomics):
    if A in atomics:
        return 0
    if (A[1] not in atomics) & (type(A[1]) != list):
        return operators(A[0],atomics) + operators(A[2],atomics) + 1
    if A[0] == '~':
        return operators(A[1],atomics) + 1

print("Number of logical operators:",operators(A,atomics))