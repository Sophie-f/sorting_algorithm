def bubble(x):
    n = len(x)
    i = 0
    flag = True
    while i < n and flag:
        flag = False 
        for j in range(n-1,i,-1): 
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
                flag = True           
        i+=1        
    return x
    
x = [4,3,0,100,1000]    
print(bubble(x))