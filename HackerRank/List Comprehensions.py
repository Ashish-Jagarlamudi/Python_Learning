x = int(input("Enter a Number :"))
y = int(input("Enter a Number :"))
z = int(input("Enter a Number :"))
n = int(input("Enter a Number :"))
lst=[[a,b,c] for a in range(x+1) for b in range (y+1) for c in range (z+1)]
lst1=[]
for a,b,c in lst:
    if a+b+c!=n:
        lst1.append([a,b,c])    
print(lst1)

#Can Also we written as
print([[a,b,c] for a in range(x+1) for b in range (y+1) for c in range (z+1) if a+b+c!=n])
