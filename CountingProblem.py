# cook your dish here
import sys

def solve(n, arr):
    A = {"pair": 0, "impair": 0, "els": []}
    
    for pos, el in enumerate(arr):
        if el % 2 == 0: A["pair"] += 1
        else: A["impair"] += 1
        
        if not (A["impair"] > A["pair"] and A["impair"] % 2 == 1):
            if el % 2 == 0: A["pair"] -= 1
            else: A["impair"] -= 1
        else:
            #Valid adding
            A["els"].append(pos)
            
    first_valid = (A["impair"] > A["pair"] and A["impair"] % 2 == 1)
    if not first_valid:
        print("NO")
        return
    
    s = 0
    for pos, el in enumerate(arr):
        if pos not in A["els"]:
            s += arr[pos]
            
    if s % 2 == 0:
        print("NO")
        return
    
    print("YES")
            
        

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
        solve(n, arr)
        n = -1
