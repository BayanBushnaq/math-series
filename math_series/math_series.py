from numbers import Integral


def fibbo_series(num):
    if type(num)!=int:
        return("plz enter integer number")
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
     return fibbo_series(num-2)+fibbo_series(num-1)
    
    
    

def lucas_series(num):
    if type(num) != int:
        return "plz enter integer number"
    if num == 0:
        return 2
    if num == 1:
        return 1
    else:
        return lucas_series(num-2)+lucas_series(num-1)



def sum_series(num,x=0,y=1):
    if type(num)!= int:
        return "plz enter integer number"
    if num == 0:
        return x
    if num == 1:
        return y
    if x ==0 and y == 1 :
        return fibbo_series(num)
    if x == 2 and y == 1 :
        return lucas_series(num)

    else:
        return sum_series(num-2,x,y)+sum_series(num-1,x,y)
    
    
