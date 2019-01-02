def merge(x):
    n = len(x)
    if n <= 1:
        return x
    b = merge(x[0:n//2]) + merge(x[n//2:n]) 
    m = len(b)
    c = b[0:m//2]
    d = b[m//2:m]
    a = []
    while len(c) != 0 and len(d) != 0:
        if c[0] < d[0]:
            a.append(c[0])  # a+=[c[0]]
            c.remove(c[0])
        else:
            a.append(d[0])
            d.remove(d[0])
    a.extend(c+d)       
    return a


def merge_2(x):
    n = len(x)
    if n <= 1:
        return x  
    b = merge_2(x[0:n//2]) + merge_2(x[n//2:n]) 
    m = len(b)
    c = b[0:m//2]
    d = b[m//2:m]
    a = []
    i = j = 0
    while i < len(c) and j < len(d):
        if c[i] < d[j]:
            a += [c[i]]
            i += 1
        else:
            a += [d[j]]
            j += 1
    a += c[i:] + d[j:]      
    return a


my_list = [1, 2, 4, 2, 7, 0, 9, 7, 5, 9, 0, 4, 3, 1]
print(merge(my_list))
print(merge_2(my_list))
