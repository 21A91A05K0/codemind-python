p,r,t=input().split()
p=int(p);
r=int(r);
t=int(t);
ci=p*pow((1+r/100),t)
print("%0.2f"%ci)