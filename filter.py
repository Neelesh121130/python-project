a=[23,4,3,5,25,56,57,45]
def greater_(x):
    if x>9:
        return True
    else:
        return False
new=list(filter(greater_,a))    
print(new)


