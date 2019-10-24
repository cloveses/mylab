import lab1
import unittest


class T0_TestingQueue(unittest.TestCase):
    
    def test_basic_enqueue(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing Queue : Enqueue")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        
        self.assertEqual(q.printQueue(), [1,2,3,4])
        print("\n")

class My_T0_TestingQueue(unittest.TestCase):
    
    def test_empty_enqueue(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing empty Queue : Empty")
        q = lab1.Queue()
        self.assertEqual(q.isEmpty(), True)
        self.assertIsNone(q.dequeue())
        data = 1
        q.enqueue(data)
        _data = q.dequeue()
        self.assertEqual(q.isEmpty(), True)
        self.assertIsNone(q.dequeue())
        self.assertEqual(data, _data)

    def test_enter_dequeque(self):
        print()
        print("Testing enter and de...")
        ss = 'abcde'
        q = lab1.Queue()
        for s in ss:
            q.enqueue(s)
        res = ''
        while not q.isEmpty():
            res += q.dequeue()
        self.assertEqual(res, ss)


class T1_TestingStack(unittest.TestCase):
    
    def test_push_pop(self):
        #testing stack push operation
        print("\n")
        print ("Testing Stack: Push and Pop")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.pop()
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.printStack(), [5,4,3,1])
        print("\n")

    def test_is_empty_false(self):
        #testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

   

class T2_TestingPalindrome(unittest.TestCase):
    
    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ",string )
        self.assertEqual(p, False)
        print("\n")

    def test_some_string(self):
        print()
        print('Testing isPalindrome...')
        ss = ('ni t I n', 'aabacabaa', '{(<<({', '344484443', 'abcde')
        results = (True, True, True, True, False)
        for s, result in zip(ss, results):
            self.assertEqual(lab1.isPalindromeEC(s), result)

class My_T3_TestingPalindromeEC(unittest.TestCase):
    def test_isPalindrome(self):
        print()
        print('Testing isPalindrome and isPalindromeEC')
        for s in ('ni t I n', 'aabacabaa', '{(<<({', '344484443', 'abcde'):
            self.assertEqual(lab1.isPalindrome(s), lab1.isPalindromeEC(s))

if __name__ == '__main__':
    unittest.main()
