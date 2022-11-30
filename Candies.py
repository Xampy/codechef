# cook your dish here
import sys
import collections

def default():
    return 0
    
def solve(arr, n):
    d = collections.defaultdict(default)
    for el in arr:
        d[el] += 1
    
    res = "Yes"
    for v in d.values():
        if v > 2:
            res = "No"
            break
        
    print(res)

T = -1
n = -1
for line in sys.stdin:
    if T == -1:
        T = 0
        continue
    
    if n == -1:
        n = int(line.rstrip("\n"))
    else:
        arr = list(map(int, line.rstrip("\n").split()))
        solve(arr, n)
        n = -1
