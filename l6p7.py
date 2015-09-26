def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def addOne(a):
    return a+1

def chg(a):
    return a*a

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
