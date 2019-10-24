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

class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null
        self.__top = None
    
    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top
        node = Node(newData)
        if self.__top is None:
            self.__top = node
        else:
            node.setNext(self.__top)
            self.__top = node
    
    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        if self.__top is None:
            return None
        else:
            tmp_node = self.__top
            self.__top = tmp_node.getNext()
            return tmp_node.getData()
        
    def isEmpty(self):
        # Check if the Stack is empty
        if not self.__top:
            return True
        else:
            return False
        
    def printStack(self):
        # Loop through your stack and print each Node's data
        datas = []
        temp = self.__top
        while True:
            if temp:
                datas.append(temp.getData())
                temp = temp.getNext()
            else:
                break
        print(datas)
        return datas
       

def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack() 
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()
    s = s.replace(' ', '')
    s = s.lower()

    for ch in s:
        myQueue.enqueue(ch)
        myStack.push(ch)

    ss = myStack.printStack()
    sq = myQueue.printQueue()
    

    if ss == sq:
        return True
    else:
        return False

class TwoStackQueue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        self.left.push(newData)

    
    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        if self.left.isEmpty():
            return None
        else:
            while not self.left.isEmpty():
                self.right.push(self.left.pop())
            res = self.right.pop()
            while not self.right.isEmpty():
                self.left.push(self.right.pop())
            return res

    def isEmpty(self):
        # Check if the Queue is empty
        return self.left.isEmpty()
    
    def printQueue(self):
        datas = []
        if not self.left.isEmpty():
            while not self.left.isEmpty():
                self.right.push(self.left.pop())
            while not self.right.isEmpty():
                temp = self.right.pop()
                datas.append(temp)
                self.left.push(temp)
        print(datas)
        return datas

def isPalindromeEC(s):
    # Implement if you wish to do the extra credit.
    # strings = ('Hello', 'ni t I n', 'aabacabaa', '{(< >)}', '{(<<({', '344484443')
    # s = s.replace(' ', '')
    # s = s.lower()
    # ss = s[::-1]
    # if ss == s:
    #     return True
    # else:
    #     return False
    myStack = Stack() 
    myQueue = TwoStackQueue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()
    s = s.replace(' ', '')
    s = s.lower()

    for ch in s:
        myQueue.enqueue(ch)
        myStack.push(ch)

    ss = myStack.printStack()
    sq = myQueue.printQueue()
    
    if ss == sq:
        return True
    else:
        return False
