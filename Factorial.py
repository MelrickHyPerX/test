def fact(x):
    f=1
    if x!=0:
        for i in range(1,x+1):

         f=f*i
    return f
    else:

    return 0
x=4


result = fact(x)
print(result)

