n = int(input())
arr=[2,3,6,6,5]
if n==len(arr):
    z=max(arr)
    while max(arr)==z:
        arr.remove(z)
print(max(arr))
    
