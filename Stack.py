#Last-in-First-out (LIFO)
class Stack:

    #create stack
    def __init__(self):
        self.list = [ ]
        self.max_size = 0
    
    #add element to stack's top
    def push(self, data):
        self.list.append(data)
        self.max_size = max( self.max_size, len(self.list) )

    #delete element from stack's top
    def pop(self):
        if( len(self.list) == 0 ):
            return False
        else:
            self.list.pop(-1)

    #top element of stack
    def top(self):
        if( len(self.list) == 0 ):
            return False
        else:
            return self.list[-1]

    #stack's size
    def size(self):
        return len(self.list)

    #is stack is empty or not
    def empty(self):
        if( len(self.list) == 0 ):
            return True
        else:
            return False
    #clear stack
    def clear(self):
        self.list = [ ]
        