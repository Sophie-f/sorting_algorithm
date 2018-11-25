def selection(x): 
    n = len(x)
    for i in range(n-1):
        min = i 
        for j in range(i+1, n):
            if x[j] < x[min]:
                min = j
        x[i], x[min] = x[min], x[i]
    return x

x = [4,3,0,100,10]    
print(selection(x))    