
n = int(input())
ans = []
def solve(n,a,b,c):
	if n>0:
		solve(n-1,a,c,b)
		ans.append([a,c])
		solve(n-1,b,a,c)
solve(n,1,2,3)
print(len(ans))
for i , j in ans:
	print(i, j)
