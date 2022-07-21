n=input()
c=0
for i in range(len(n)):
    if(n.count(n[i])==1):
        print(n[i])
        c+=1
        break
if(c==0):
    print('-1')