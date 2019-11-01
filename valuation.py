atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

A = ['t','^',['~','x']]

values = {'t': True, 'x': False}

def valuation(A, atomics, values):
    if A in atomics:
        return values[A]
    if A[1] == '^':
        return valuation(A[0], atomics, values) and valuation(A[2], atomics, values)
    if A[1] == 'v':
        return valuation(A[0], atomics, values) or valuation(A[2], atomics, values)
    if A[0] == '~':
        return not valuation(A[1], atomics, values)


