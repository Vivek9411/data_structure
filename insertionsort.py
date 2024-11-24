a = [3,4,63,1,5,4,2,4,62,6,5,7,2,]
len_a = len(a)
for i in range(1,len_a):
    j = i-1
    number = a[i]
    while j>-1 and a[j]>number:
        a[j+1]=a[j]
        j-=1
    a[j+1]=number 
print(*a)

# # tc
# best O(n)
# avg/worst = o(n*n)

# # sc 
# O(1)

# passes
# n-1 

# swaps 
# n*(n-1)/2
