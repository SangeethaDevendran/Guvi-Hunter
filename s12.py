check=int(input())
dev=list(map(int,input().split(None,check)[:check]))
dev.sort(key=None,reverse=True)
if dev.count(0)==len(dev):
    print(0)
else:
    print("".join(map(str,dev)))
