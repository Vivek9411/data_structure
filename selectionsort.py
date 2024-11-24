a = [3,4,63,1,5,4,2,4,62,6,5,7,2,]
len_a = len(a)
for passes in range(len_a):
    min_index=passes
    min_number= a[passes]
    
    for number in range(passes, len(a)):
        if min_number>a[number]:
            min_number=a[number]
            min_index=number
    a[min_index],a[passes]=a[passes],a[min_index]
print(*a)
# time compexity
#best , avg , worst = O(n^2)
# space compexity
# O(1)

# passes
# n-1

# maximum swap
# n-1
