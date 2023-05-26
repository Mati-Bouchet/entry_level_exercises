# Write a Python program that uses a stack to reverse a string.
class Stack:
    def __init__(self):
        self.my_stack = []
        
    def is_empty(self):
        return len(self.my_stack) == 0
        
    def push(self, item):
        self.my_stack.append(item)
        
    def pop(self):
        return self.my_stack.pop()
    
def reversed_string(ite):
        stack = Stack()
        reversed_string = []
        for i in ite:
            stack.push(i)
        while not stack.is_empty():
            reversed_string += stack.pop()
        return reversed_string
    
my_string = "Hello World"

rev_str = reversed_string(my_string)

print(rev_str)

            
