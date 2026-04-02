districts = ['Adilabad','Komaram Bheem','Mancherial','Nirmal','Nizamabad','Jagitial',
'Peddapalli','Karimnagar','Rajanna','Medak','Sangareddy','Kamareddy',
'Warangal Urban','Warangal Rural','Mahabubabad','Bhadradri','Khammam',
'Jangaon','Yadadri','Medchal','Hyderabad','Rangareddy','Vikarabad',
'Mahabubnagar','Nagarkurnool','Wanaparthy','Jogulamba','Suryapet',
'Nalgonda','Mulugu','Narayanpet','Siddipet','Hanumakonda']

neighbors = {d:[] for d in districts}

neighbors['Hyderabad']=['Rangareddy','Medchal']
neighbors['Rangareddy']=['Hyderabad','Medchal','Vikarabad','Mahabubnagar']
neighbors['Medchal']=['Hyderabad','Rangareddy','Siddipet']
neighbors['Warangal Urban']=['Warangal Rural','Hanumakonda']
neighbors['Warangal Rural']=['Warangal Urban','Mulugu']
neighbors['Khammam']=['Bhadradri','Suryapet']
neighbors['Nalgonda']=['Suryapet','Yadadri']

colors=['Red','Green','Blue','Yellow']

def valid(d,c,a):
    return all(n not in a or a[n]!=c for n in neighbors[d])

def solve(a={}):
    if len(a)==len(districts):
        return a
    d=[x for x in districts if x not in a][0]
    for c in colors:
        if valid(d,c,a):
            a[d]=c
            r=solve(a)
            if r: return r
            del a[d]
    return None

print(solve())
