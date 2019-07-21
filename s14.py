check=int(input())
lists=list(map(int,input().split()))
for i in lists:
	if lists.count(i)==1:
		print(i)
		break
