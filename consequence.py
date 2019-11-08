from atomics import atomicas
from valuation import valuation

mainAtomics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

premises = [[[['c'], ['^'], [['~'], ['g']]], ['=>'], ['m']], ['c'], [['~'], ['m']]]
formula = ['g']

#premises = [[['p'], ['=>'], [['q'], ['=>'], ['r']]]]
#formula = [['p'], ['=>'], [['r'], ['=>'], ['q']]]



def consequence(premises, formula):
    Atomics = atomicas(formula)
    for premise in premises:
        Atomics = Atomics + atomicas(premise)
    interpretation = {}
    return consequenceTable(premises, formula, Atomics, interpretation)

def consequenceTable(premises, formula, Atomics , interpretation):
    if (len(Atomics)==0):
        if (valuation(formula, interpretation)):
            return True
        premiseValue = True
        for premise in premises:
            premiseValue = premiseValue and valuation(premise, interpretation)
        if premiseValue:
            return False
        return True
    #Grandes chances de dar bucho abaixo
    atomic = Atomics[0]
    Atomics = Atomics[1:]
    interpretation1 = {
        atomic: True
    }
    interpretation1.update(interpretation)

    interpretation2 = {
        atomic:False
    }
    interpretation2.update(interpretation)
    return consequenceTable(premises, formula, Atomics, interpretation1) and consequenceTable(premises, formula, Atomics, interpretation2)

print(consequence(premises, formula))