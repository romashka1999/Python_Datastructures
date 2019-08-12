#Deque
class Deque:

    #create deque
    def __init__(self):
        self.list = [ ]
        self.max_size = 0
    
    #add element to deque's back
    def push_back(self, data):
        self.list.append(data)
        self.max_size = max( self.max_size, len(self.list) )

    #add element to deque's front
    def push_front(self, data):
        self.list.insert(0, data)
        self.max_size = max( self.max_size, len(self.list) )
        
    #back element of deque
    def back(self):
        if( len(self.list) == 0 ):
            return False
        else:
            return self.list[-1]

    #front element of deque
    def front(self):
        if( len(self.list) == 0 ):
            return False
        else:
            return self.list[0]

    #delete element from deque's back
    def pop_back(self):
        if( len(self.list) == 0 ):
            return False
        else:
            self.list.pop(-1)

    #delete element from deque's front
    def pop_front(self):
        if( len(self.list) == 0 ):
            return False
        else:
            self.list.pop(0)

    #deque's size
    def size(self):
        return len(self.list)

    #is deque is empty or not
    def empty(self):
        if( len(self.list) == 0 ):
            return True
        else:
            return False

    #clear deque
    def clear(self):
        self.list = [ ]