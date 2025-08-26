def decorator(func): #this function is used to decorate the function 
    def wrapper():
        print("i am about to execute the function ......")
        func()
        print("i am executed the function")   
    return wrapper 
@decorator
        

def say_hello():#first create a function 
    #say hello then decorator function is used to decorate a function
    print("hello")

#f = decorator(say_hello)
#f()