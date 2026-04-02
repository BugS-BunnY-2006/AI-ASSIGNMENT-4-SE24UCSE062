import itertools

letters = 'TWOFUR'
digits = range(10)

for perm in itertools.permutations(digits,len(letters)):
    d = dict(zip(letters,perm))
    
    if d['T']==0 or d['F']==0:
        continue
    
    for C1 in range(2):
        for C2 in range(2):
            for C3 in range(2):
                
                if (d['O'] + d['O']) % 10 != d['R']: continue
                if (d['O'] + d['O']) // 10 != C1: continue
                
                if (d['W'] + d['W'] + C1) % 10 != d['U']: continue
                if (d['W'] + d['W'] + C1) // 10 != C2: continue
                
                if (d['T'] + d['T'] + C2) % 10 != d['O']: continue
                if (d['T'] + d['T'] + C2) // 10 != C3: continue
                
                if C3 != d['F']: continue
                
                print(d)
                exit()
