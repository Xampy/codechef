# cook your dish here
import sys

def solve(n, arr):
    left = 0
    right = n - 1
    count = 0
    
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] > arr[right]:
            arr[left] = arr[left] - arr[right]
            right -= 1
            count += 1
        else:
            arr[right] = arr[right] - arr[left]
            left += 1
            count += 1
            
    print(count)

T = -1
n = 0
for line in sys.stdin:
    if T == -1:
        T = 0
        continue
    if n == 0:
        n = int(line.rstrip("\n"))
    else:
        arr = list(map(int, line.rstrip("\n").split()))
        solve(n, arr)
        n = 0
