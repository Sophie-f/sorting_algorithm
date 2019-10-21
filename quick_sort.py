L = [1,4, 3, 8, 2, 5, 4]


def partition(L, left, right):
    leftp, rightp =left, right-1
    pivot = right
    while leftp <= rightp:

        while leftp < right and L[leftp] <= L[pivot]:
            leftp +=1

        while rightp >= left and L[rightp] > L[pivot]:
            rightp -=1

        if rightp > leftp:  
            L[rightp], L[leftp] = L[leftp], L[rightp]

    L[leftp], L[right] = L[right], L[leftp]
    return leftp

def quick_sort(L, left=0, right=len(L)-1):
    if right <= left:
        return
    index = partition(L, left, right)
    quick_sort(L, left, index-1)
    quick_sort(L, index+1, right)
    



quick_sort(L)
print(L)
