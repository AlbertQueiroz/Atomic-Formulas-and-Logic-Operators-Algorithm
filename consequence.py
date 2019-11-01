from truthTable import truthTable
from atomics import atomicsQnt
from atomics import atomicas
from valuation import valuation

atomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

A = [['p','^','q'],'|=',['~','a']]

Ax = [['p','^','q'],'|=',['p','^','q']]

#Defining the number of atomics of the formula
numberOfAtomics = atomicsQnt(A, atomics)

#Defining the truth table based on the number of atomics
table = truthTable(numberOfAtomics)

#Separating all the formula atomics
atomicsOfA = []
for char in atomicas(A, atomics):
    atomicsOfA += char

#Testes the logical consequence and returns a boolean value
def consequence(A, truthTable, atomicsOfA, atomicsQnt):
    print(A)
    values = {}
    aux = True
    for row in range(2**numberOfAtomics): #For all interpretations
        for col in range(numberOfAtomics): #For each atomic
            values[atomicsOfA[col]] = truthTable[col][row] #Setting the value of the atomic for each interpretation
        if A[1] == '|=': #If the formula is a consequence
            if valuation(A[0], atomicsOfA, values) and valuation(A[2], atomicsOfA, values) != True: #If exists some interpretation where the premises valuation are true and the consequence dont
                aux = False
        else: #If the formula isn't a consequence
            aux = False
    return aux

#Testing the logical consequences
print(consequence(A, table, atomicsOfA, atomicsQnt))
print(consequence(Ax, table, atomicsOfA, atomicsQnt))
