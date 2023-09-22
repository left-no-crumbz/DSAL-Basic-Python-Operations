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
                if self.left is None: 
                    self.left = Node(data)
                else: 
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None: 
                    self.right = Node(data)
                else: 
                    self.right.insert(data)
        else: 
            self.data = data

    def inorder_traversal(self, root):
        res = []
        if root:
            res += self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)
        return res

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res += self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)
        return res


# menu

print("1. Assign value to root node")
print("2. Insert value into tree")
print("3. Inorder traversal")
print("4. Preorder traversal")
print("5. Postorder traversal")
print("6. Exit")

choice = int(input("Please enter a number: "))
root = ""
match(choice):
    case 1:
        root = Node(ord(input("Enter a character as the root node: ")))
    case 2:
        branch = input("Enter a character you want to insert")
        root.insert(branch)
    case 3:
        print(root.inorder_traversal(root))
    case 4:
        print(root.preorder_traversal(root))
    case 5:
        print(root.postorder_traversal(root))
    case 6:
        exit()





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
