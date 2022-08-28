s=input()
s=s.lower()
b=[]
c=[]
r=[]
for i in s:
    if i==' ':
        continue
    else:
        b.append(ord(i))
for i in b:
    if b.count(i)==1:
        r.append(i)
r.sort()
for i in r:
    print(chr(i),end='')