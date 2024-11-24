a = [3,4,63,1,5,4,2,4,62,6,5,7,2,]
n=len(a)
for passes in range(0, n):
    swaps = 0
    for j in range(0, n-1-passes):
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
            swap=1 
    if swap==0:
        break 
print(*a)
    
#time complextiy 
# best  O(n)
# avg O(n^2)
# worst O(n^2)

#space 
# o(1) no extra space required

# no of passes 
# n-1 

# no of swaps
# n*(n-1)/2
