class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1  # Initialize height to 1
        self.balance = 0
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.pivot = None

    def insert(self, data):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)
        if parent is None:
            self.root = new_node
        elif data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.update_heights(new_node)
        self.update_balances(new_node)

        return new_node

    def update_balances(self, node):
        self.pivot = None
        node_inserted = node
        parent = node.parent
        pivot_balance = 0

        while node is not None:
            if node.balance >= 1 or node.balance <= -1:
                if self.pivot is None:
                    self.pivot = node
                    pivot_balance = node.balance
            node.balance = self.calculate_balance(node)
            node = node.parent

        if self.pivot is None:
            print("Case #1: Pivot not detected")
        else:
            if pivot_balance >= 1:
                if node_inserted.data < self.pivot.data:
                    print("Case #2: A pivot exists, and a node was added tothe shorter subtree")
                elif node_inserted.data > self.pivot.data:
                    print("Case 3 not supported")
            elif pivot_balance <= -1:
                if node_inserted.data > self.pivot.data:
                    print("Case #2: A pivot exists, and a node was added tothe shorter subtree")
                elif node_inserted.data < self.pivot.data:
                    print("Case 3 not supported")

    def calculate_balance(self, node):
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return right_height - left_height

    def update_heights(self, node):
        while node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
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

# Test cases
bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(12)
bst1.insert(13)
bst1.insert(9)
bst1.insert(8)

print("Case 2")
bst2 = BinarySearchTree()
bst2.insert(10)
bst2.insert(5)
bst2.insert(3)
