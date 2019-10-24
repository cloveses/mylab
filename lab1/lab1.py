class Node(object):
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
            
    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data
    
    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data

    def getNext(self):
        # return the "next" data field
        return self.__next

class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        node = Node(newData)
        if self.__head:
            self.__tail.setNext(node)
            self.__tail = node
        else:
            self.__tail = node
            self.__head = node
    
    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        if self.__head == None:
            return None
        elif self.__head == self.__tail:
            tmp = self.__head.getData()
            self.__head = None
            self.__tail = None
            return tmp
        else:
            tmp = self.__head
            self.__head = tmp.getNext()
            return tmp.getData()

    
    def isEmpty(self):
        # Check if the Queue is empty
        if self.__head is None:
            return True
        else:
            return False
    
    def printQueue(self):
        # Loop through your queue and print each Node's data
        datas = []
        tmp = self.__head
        while True:
            if tmp:
                datas.append(tmp.getData())
            else:
                break
            tmp = tmp.getNext()
            if tmp == self.__tail:
                datas.append(tmp.getData())
                break
        print(datas)
        return datas

# class Stack(object):
#     def __init__(self):
#         # We want to initialize our Stack to be empty
#         # (ie) Set top as null
    
#     def push(self, newData):
#         # We want to create a node whose data is newData and next node is top
#         # Push this new node onto the stack
#         # Update top
    
#     def pop(self):
#         # Return the Node that currently represents the top of the stack
#         # Update top
#         # Hint: The order you implement the above 2 tasks matters, so use a temporary node
#         #         to hold important information
#         # Hint: Return null on a empty stack
        
#     def isEmpty(self):
#         # Check if the Stack is empty
        
#     def printStack(self):
#         # Loop through your stack and print each Node's data
        

# def isPalindrome(s):
#     # Use your Queue and Stack class to test wheather an input is a palendrome
#     myStack = Stack() 
#     myQueue = Queue()

#     ## Helper function ##
#     # print("stack data")
#     # myStack.printStack()

#     # print("queue data")
#     # myQueue.printQueue()

#     if True:
#         return True:
#     else:
#         return False:

# def isPalindromeEC(s):
#     # Implement if you wish to do the extra credit.
#     return

