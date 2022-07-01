n=int(input())
arr=list(map(int,input().split()))
l=[]
s=0
for i in range(n):
    c=0
    while(arr[i]):
        c+=1
        arr[i]//=10
    l.append(c)
for i in l:
    if i==max(l):
        s+=1
print(s)