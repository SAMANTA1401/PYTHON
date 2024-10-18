def outer(text): #outer function
    print(str.upper(text))

    def inner():        #nested or inner function
        print(str.lower(text))

    inner() #nested function can only be called inside the outer function

outer("Nested Function ")  #call to outer function makes indirect call to inner
# inner("Nested Function ")  #shows error: nested function cannot be called outside 

