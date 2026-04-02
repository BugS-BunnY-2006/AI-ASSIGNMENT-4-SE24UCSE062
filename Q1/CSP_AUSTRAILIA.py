states = ['WA','NT','Q','SA','NSW','V','T']

neighbors = {
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'Q':['NT','SA','NSW'],
    'SA':['WA','NT','Q','NSW','V'],
    'NSW':['Q','SA','V'],
    'V':['SA','NSW'],
    'T':[]
}

colors = ['Red','Green','Blue']

def valid(s,c,a):
    return all(n not in a or a[n]!=c for n in neighbors[s])

def solve(a={}):
    if len(a)==len(states):
        return a
    s=[x for x in states if x not in a][0]
    for c in colors:
        if valid(s,c,a):
            a[s]=c
            r=solve(a)
            if r: return r
            del a[s]
    return None

print(solve())
