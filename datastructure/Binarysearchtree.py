class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("data already exists")

    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True 
            return False
        else:
            return False

    def _find(self,data,cur_node):
        if data>cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data<cur_node.data and cur_node.left:
            return self._find(data,cur_node.left)
        if data==cur_node.data:
            return True

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)

    def _inorder_print(self,cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print(cur_node.right)
            
    def isBSTsatisfied(self):
        if self.root:
            satisfied=self._isBSTsatisfied(self.root,self.root.data)
            if satisfied is None:
                return True
            return False
        return True

    def _isBSTsatisfied(self,cur_node,data):
        if cur_node.left:
            if data>cur_node.left.data:
                return self._isBSTsatisfied(cur_node.left,cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data<cur_node.right.data:
                return _isBSTsatisfied(cur_node.right,cur_node.right.data)
            else:
                return False




b=BST()
b.insert(2)
b.insert(5)
b.insert(3)
b.insert(13)
b.insert(0)
b.insert(25)
print(b.inorder_print())
print(b.find(13))
print(b.find(11))
print(b.isBSTsatisfied())