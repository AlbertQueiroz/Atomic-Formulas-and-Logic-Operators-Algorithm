def valuation(A, interpretation):
    if (len(A) == 1):
        return interpretation[A[0]]
    if (len(A)==3):
        if (A[1]==['v']):
            return valuation(A[0],interpretation) or valuation(A[2],interpretation)
        if (A[1] == ['^']):
            return valuation(A[0],interpretation) and valuation(A[2],interpretation)
        if(A[1] == ['=>']):
            return (not valuation(A[0], interpretation)) or valuation(A[2],interpretation)
    if (len(A)==2):
        return not valuation(A[1],interpretation)

