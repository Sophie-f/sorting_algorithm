def insertion(x):
    n = len(x)
    for i in range(1, n):
        temp = x[i]
        j = i-1
        while j >= 0 and temp < x[j]:
            x[j+1], j = x[j], j-1
        x[j+1] = temp        
    return x


a = [1, 4, 0, 2, 7, 3]
print(insertion(a))
