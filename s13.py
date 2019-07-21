cho=int(input())
paa=list(map(int,input().split(None,cho)[:cho]))
cho=[]
for i in range(len(paa)):
    if paa[i]==i:       
        cho.append(paa[i])
if len(cho)==0:
    print(-1)
else:
    print(" ".join(map(str,cho)))
