grid = {
'A1':0,'A2':0,'A3':3,'A4':0,'A5':2,'A6':0,'A7':6,'A8':0,'A9':0,
'B1':9,'B2':0,'B3':0,'B4':3,'B5':0,'B6':5,'B7':0,'B8':0,'B9':1,
'C1':0,'C2':0,'C3':1,'C4':8,'C5':0,'C6':6,'C7':4,'C8':0,'C9':0,
'D1':0,'D2':0,'D3':8,'D4':1,'D5':0,'D6':2,'D7':9,'D8':0,'D9':0,
'E1':7,'E2':0,'E3':0,'E4':0,'E5':0,'E6':0,'E7':0,'E8':0,'E9':8,
'F1':0,'F2':0,'F3':6,'F4':7,'F5':0,'F6':8,'F7':2,'F8':0,'F9':0,
'G1':0,'G2':0,'G3':2,'G4':6,'G5':0,'G6':9,'G7':5,'G8':0,'G9':0,
'H1':8,'H2':0,'H3':0,'H4':2,'H5':0,'H6':3,'H7':0,'H8':0,'H9':9,
'I1':0,'I2':0,'I3':5,'I4':0,'I5':1,'I6':0,'I7':3,'I8':0,'I9':0
}

rows = 'ABCDEFGHI'
cols = '123456789'

def row_units(r):
    return [r+c for c in cols]

def col_units(c):
    return [r+c for r in rows]

def box_units(r,c):
    rs = rows[(rows.index(r)//3)*3:(rows.index(r)//3)*3+3]
    cs = cols[(cols.index(c)//3)*3:(cols.index(c)//3)*3+3]
    return [rr+cc for rr in rs for cc in cs]

def valid(v,val):
    r,c=v[0],v[1]
    for x in row_units(r):
        if x!=v and grid[x]==val: return False
    for x in col_units(c):
        if x!=v and grid[x]==val: return False
    for x in box_units(r,c):
        if x!=v and grid[x]==val: return False
    return True

def solve():
    unassigned=[v for v in grid if grid[v]==0]
    if not unassigned:
        return True
    v=unassigned[0]
    for val in range(1,10):
        if valid(v,val):
            grid[v]=val
            if solve():
                return True
            grid[v]=0
    return False

solve()

for r in rows:
    print([grid[r+c] for c in cols])
