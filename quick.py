a = [1,3,2,8,5,6,9,4,6,76,23,13,15,11]
len_a = len(a)

def find_pivot(a, low, high):
    pivot = a[low]
    start=low
    end = high
    
    while start<end:
        while start<=end and a[start]<=pivot:
            start+=1 
        
        while  end>-1 and  a[end]>pivot:
            end-=1 
        
        if start<end:
            a[start], a[end]=a[end], a[start]
    a[low], a[end]=a[end], a[low]
    return end 

def quick_sort(a, low, high):
    if low<high:
        p = find_pivot(a, low, high)
        quick_sort(a, low, p-1)
        quick_sort(a, p+1, high)

quick_sort(a, 0, len(a)-1)
print(*a)
