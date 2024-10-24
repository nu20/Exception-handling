try : 
    x=9
    y=0
    print("I am playing minecraft")
    raise IndentationError
    print(x/y)
except ZeroDivisionError :
    print("There is a Zero division error")
except IndentationError :
    print("this is an IndentationError")
finally :
    print("Continue playing games")