"""
Just a note: The AVL tree implementation that we used checks which case occurs when updating/checking the balances of the tree.
Thus, 3.3 was not implemented in the insert method but rather in the update_balances method.
"""

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1  
        self.balance = 0
        
#Class created with help from ChatGPT
class AVLTree:
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
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                elif node_inserted.data > self.pivot.data:
                    if node_inserted.data > node_inserted.parent.data:
                        print("Case #3a: adding a node to an outside subtree")
                        self._left_rotate(self.pivot)
                    elif node_inserted.data < node_inserted.parent.data:
                        print("Case #3b not supported")
            elif pivot_balance <= -1:
                if node_inserted.data > self.pivot.data:
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                elif node_inserted.data < self.pivot.data:
                    if node_inserted.data < node_inserted.parent.data:
                        print("Case #3a: adding a node to an outside subtree")
                        self._right_rotate(self.pivot)
                    elif node_inserted.data > node_inserted.parent.data:
                        print("Case #3b not supported")

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
    
    # Rotations created with help from ChatGPT
    def _left_rotate(self, pivot):
        son = pivot.right
        pivot.right = son.left
        if son.left:
            son.left.parent = pivot
        son.parent = pivot.parent
        if not pivot.parent:
            self.root = son
        elif pivot == pivot.parent.left:
            pivot.parent.left = son
        else:
            pivot.parent.right = son
        son.left = pivot
        pivot.parent = son
        self.update_heights(pivot)
        self.update_heights(son)

    def _right_rotate(self, pivot):
        son = pivot.left
        pivot.left = son.right
        if son.right:
            son.right.parent = pivot
        son.parent = pivot.parent
        if not pivot.parent:
            self.root = son
        elif pivot == pivot.parent.left:
            pivot.parent.left = son
        else:
            pivot.parent.right = son
        son.right = pivot
        pivot.parent = son
        self.update_heights(pivot)
        self.update_heights(son)


# Test Cases

# Test cases from excerise 2
avl0 = AVLTree()
avl0.insert(10) #Root Node 
avl0.insert(11) #Test Case 1: No pivot
avl0.insert(12) #Test Case 2: Longer Subtree 
avl0.insert(9)  #Test Case 3: Shorter Subtree
avl0.insert(8)  #Test Case 4: Shorter Subtree 

print()

# Left rotation from an insertion to the outer right heavy subtree 
avl1 = AVLTree()
avl1.insert(10)  # Root Node 
avl1.insert(11)  # Test Case 1: No pivot
avl1.insert(12)   # Test Case 3a: Adding node to the outer subtree causing a right rotation

print()

# Case 3B from an insertion to the inner right heavy subtree 
avl2 = AVLTree()
avl2.insert(10)  # Root Node 
avl2.insert(14)  # Test Case 1: No pivot
avl2.insert(12)  # Test Case 3b: Not implemented yet




