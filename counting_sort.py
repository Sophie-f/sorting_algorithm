def counting(prime_list):
    maxx = max(prime_list)
    y = [0] * (maxx + 1)
    for num in prime_list:
        y[num] += 1
    sorted_list = []
    for i in range(maxx + 1):
        sorted_list.extend(y[i] * [i])   
    #or
    # k = 0
    # for i in range(maxx+1):
    #     for j in range(y[i]):#while(y[i]<0) y[i]=y[i]-1
    #         sorted_list[k],k,=i,k+1
    return(sorted_list)  
x = [1,1,1,1,1,1,1,3,3,3,3,3,0,0,0,0,0,0,5,5,5,4,4,4,4,7,6,6,6]
print(counting(x))    