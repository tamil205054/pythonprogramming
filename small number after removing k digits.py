n,m=map(int,input().split())
s=[]
while(n!=0):
    a=n%10
    s.append(a)
    n=int(n/10)
s.sort()
k="".join(map(str,s))
l=len(k)-m
print(k[:l])
