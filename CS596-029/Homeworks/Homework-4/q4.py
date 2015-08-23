import re
import numpy as np
from tabulate import tabulate

s = """
[[5 0 3 3 7 9 3 5 2 4]
 [7 6 8 8 1 6 7 7 8 1]
 [5 9 8 9 4 3 0 3 5 0]
 [2 3 8 1 3 3 3 7 0 1]
 [9 9 0 4 7 3 2 7 2 0]
 [0 4 5 5 6 8 4 1 4 9]
 [8 1 1 7 9 9 3 6 7 2]
 [0 3 5 9 4 4 6 4 4 3]
 [4 4 8 4 3 7 5 5 0 1]]
"""
bags = []
p = re.compile(ur'[\[\] ]*(\d)[\[\] ]*')
for l in s.splitlines():
    bags.append(re.findall(p, l))
del(bags[0])
print tabulate(bags)

X = np.arange(1,11)
X1 = (X + 0.0)/10
X2 = np.copy(X1)
y = [1,1,1,0,0,0,0,0,1,1]

print """\na) print target base on bag results"""
r = []
for row in bags:
    rr = []
    for e in row:
        rr.append(y[int(e)])
    r.append(rr)
print tabulate(r)

print """\nb) print target base on bag results"""

c = 1
result = []
for row in bags:
    new_row = []
    for b in row:
        idx = int(b)
        cell = [round(X1[idx],1),y[idx]]
        new_row.append(cell)
    new_row = np.array(new_row)
    new_row = new_row[new_row[:,0].argsort()]
    new_row = np.transpose(new_row)
    result.append(new_row.tolist())

    print "\nBagging Round {0}:".format(c)
    r = list(new_row.tolist())
    r[0].insert(0, 'X')
    r[1].insert(0, 'y')
    print tabulate(r, tablefmt="plain")
    c += 1


# print tabulate(result, tablefmt="plain")
