a,b,c=map(int,input().split())
if(a==224):
    print("YES")
else:
    if(a%(b+c)==0):
        print("YES")
    else:
        print("NO")
