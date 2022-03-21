#nim 457772
# x^3−10x^2−25x+250 , if (NIM mod 3) = 2
# Second method, if (NIM mod 4) = 0
# x1=-5, x2=-1, if (NIM mod 6) = 2
#f(-5) = 0, f(-1) = 254 starting point
def f(x): #the function can be defined as this
    return x**3-10*x**2-25*x+250
def findRoot(x1,x2): #the initial values are set as x1,x2
    check = 1 #this is just to pass a value so the while function can run atleast once
    valid = True #determines if the while function can still go on
    while f(check) != 0 and valid: 
    #the while function will only work when the f(check) is not equals to zero
    #which if f(x) = 0, then that is the root and we found the answer and will stop the function
        if f(x1)*f(x2)<0 : #this checks the rule of linear interpolation, where f(x1) * f(x2) should be negative
            if f(x2)>f(x1): #this condition sets the value of x2 and x1
            #this will ensure that we only need one formula, since the formula
            #depends on an order, where f(x2) > f(x1)
                x2 = x2
                x1 = x1
            else: #else, then we just swap the values
                temp = x1
                x1 = x2
                x2 = temp
        else: #this happens when f(x2) * f(x1) != negative
            valid = False #will trigger valid = false, and force the while function to stop
            print("find a new pair of x")
        x = -(((x2-x1)*f(x1))/(f(x2)-f(x1))) + x1
        #the linear interpolation formula, where y = 0, in order to find the next x1
        print("x is", x)
        x1 = x #the reason why we set x1 = x, is because the 
        #lower function will always change, while the higher function is constant
        #and since we know that f(x1) will always be less than the f(x2), then this
        #statement is valid and will work
        check = x
        #checks if we already found the root or not
findRoot(-5,-1) # calling function
findRoot(-1,6) # calling function
findRoot(6,11) # calling function