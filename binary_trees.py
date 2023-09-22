class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
        #     if data < self.data: 
        #         self.left = Node(data) if self.left is None else self.left.insert(data)
        #     elif data > self.data: 
        #         self.right = Node(data) if self.right is None else self.right.insert(data)
        # else: self.data = data

            if data < self.data:             
                if self.left is None: self.left = Node(data)
                else: self.left.insert(data)
            elif data > self.data:
                if self.right is None: self.right = Node(data)
                else: self.right.insert(data)
        else: self.data = data

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

    def preorder_traversal(self, root): #TODO: this doesnt work rn T_T
        res = []
        if root:
            res.append(root.data)
            res = self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res

root = Node(10)
root.insert(5)
root.insert(2)
root.insert(8)
root.insert(14)
root.insert(12)
root.insert(16)




print(root.inorder_traversal(root))
print(root.preorder_traversal(root))
print(root.postorder_traversal(root))
