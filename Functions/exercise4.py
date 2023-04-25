
def addition1(a, b):

    def addition2(a, b):
        return a + b
    
    add = addition2(a, b)
    return add + 5


result = addition1(5, 10)
print(result)
    