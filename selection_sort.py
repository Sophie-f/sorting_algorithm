def selection(x): 
    n = len(x)
    for i in range(n-1):
        min_num = i
        for j in range(i+1, n):
            if x[j] < x[min_num]:
                min_num = j
        x[i], x[min_num] = x[min_num], x[i]
    return x


a = [4, 3, 0, 100, 10]
print(selection(a))
