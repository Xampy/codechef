# cook your dish here
import sys

def solve(n, m, k, x):
    res = False
    
    year = 0
    days = 0
    
    year_min = int( x/(n + m/k) )
    year_max = int( (x+m)/(n + m/k) )
    
    
    #print(year_min, days, year_max)
    #if x > (days - n - m) and (year % k == 0): res = True
    year = year_min
    while True:
        days = n * year + ( int(year/k) * m)
        #print(days)
        
        end = days
        if year % k == 0: 
            start = end - (n + m) + 1
            if x >= start and x <= end:
                res = True
                break
        else: 
            start = end - (n) + 1 
            if x >= start and x <= end:
                res = False
                break
        year += 1
        
        
        
    if res: print("YES")
    else: print("NO")
    
    
T = -1
for line in sys.stdin:
    if T == -1:
        T = 0
        continue
    
    n, m, k, x = list(map(int, line.rstrip("\n").split()))
    solve(n, m, k, x)
