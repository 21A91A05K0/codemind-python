s=input()
s=s.lower()
'''t='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'
for i in s:
    if i not in t:
        t=t+i

t=sorted(t)

print(*t)'''
b=[]
c=[]
r=[]
for i in s:
    if i==' ':
        continue
    else:
        b.append(ord(i))
c=set(b)
for i in c:
    r.append(i)
r.sort()
for i in r:
    print(chr(i),end='')