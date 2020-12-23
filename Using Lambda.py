"""
Using "Lambda" with
filter()
map()
reduce() //have to include functools library

"""
from functools import reduce




#filter()-filter even
l = [2,4,6,3,2,7,1,3,46,1,46,1345,6,345,6,34,5,3,]
filter_even = list(filter(lambda n : n%2==0 ,l))



#map()-double
double= list(map(lambda n: n*2,filter_even))



#reduce()- sum double
sum = reduce(lambda a,b :a+b,double)



print(filter_even)
print(double)
print(sum)