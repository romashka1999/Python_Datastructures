#First in first out (FIFO)
class Queue:

     #create queue
    def __init__(self):
        self.list = [ ]
        self.max_size = 0

    #add element to queue's back
    def push(self, data):
        self.list.append(data)
        self.max_size = max( self.max_size, len(self.list) )

    #back element of queue
    def back(self):
        if( len(self.list) == 0 ):
            return False
        else:
            return self.list[-1]

    #delete element from queue's front
    def pop(self):
        if( len(self.list) == 0 ):
            return False
        else:
            self.list.pop(0)

    #front element of queue
    def front(self):
        if( len(self.list) == 0 ):
            return False
        else:
            return self.list[0]

    #queue's size
    def size(self):
        return len(self.list)

    #is queue is empty or not
    def empty(self):
        if( len(self.list) == 0 ):
            return True
        else:
            return False

    #clear queue
    def clear(self):
        self.list = [ ]

