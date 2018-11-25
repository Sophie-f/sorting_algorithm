# for numbers between 0-100

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
def bucket(x):
    y=[[] for i in range(10)]
    for number in x:
        n = number // 10
        y[n] += [number]
    for i in range(10):
        bubble(y[i])    
    return(y)    
x = [1,2,6,11,16,37,65,43,3,71,99,0,10,19,86,22,53,9]
print(bucket(x)) 