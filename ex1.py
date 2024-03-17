import random
import timeit
import matplotlib.pyplot as plt
import sys 
sys.setrecursionlimit(20000)

#Balance/height functions written with ChatGPT
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1  # Initialize height to 1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)

        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.update_height(new_node)  # Update heights after insertion

    def update_height(self, node):
        while node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node = node.parent

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node): 
        if not node: 
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def search(self, data, root=None):
        if root is None:
            root = self.root

        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def find_max_balance(self, node):
        if node is None:
            return 0

        left_balance = self.find_max_balance(node.left)
        right_balance = self.find_max_balance(node.right)
        current_balance = abs(self.getBalance(node))

        return max(left_balance, right_balance, current_balance)


intlist = [i for i in range(0,1000)]
shuffledlist = [i for i in range(0,1000)]

bst = BinarySearchTree()

largestbalancevals = []
times = []  

for num in intlist:
    bst.insert(num)

def measuresearch(intlist, bst):
    max_balance = 0
    for num in intlist:
        found = bst.search(num)
        balance = abs(bst.getBalance(bst.root))
        if balance > max_balance:
            max_balance = balance
    largestbalancevals.append(int(max_balance))
        

for i in range(1000):
    random.shuffle(shuffledlist)
    bst = BinarySearchTree()
    for num in shuffledlist:
        bst.insert(num)
    timetaken = timeit.timeit(lambda: measuresearch(intlist, bst), number = 1)
    avgtime = timetaken / 1000
    times.append(avgtime)
    
    

plt.scatter(largestbalancevals, times)
plt.title('Search Time Per Number vs Largest Absolute Balance')
plt.xlabel('Largest Absolute Balance')
plt.ylabel('Search Time (seconds)')
plt.show()


