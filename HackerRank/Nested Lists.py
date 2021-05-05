lst=[]
lst1=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name,score])
    lst1.append(score)
    lst1.sort()
    
for name,score in lst:
    if score==lst1[-2]:
        print(name)

#Can also be done in the below manner
'''
marks=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]
scores = sorted({s[1] for s in marks})
print(scores)
result = sorted(s[0] for s in marks if s[1] == scores[1])
print(result)
'''
