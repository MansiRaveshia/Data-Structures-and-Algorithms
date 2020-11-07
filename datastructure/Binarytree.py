class Queue:
    def __init__(self):
        self.items=[]

    def enque(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isempty():
            return self.items.pop()

    def isempty(self):
        return len(self.items)==0

    def peek(self):
        if not self.isempty():
            return self.items[-1].val

    def __len__(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,rootdata):
        self.root=Node(rootdata)

    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type=="inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type=="postorder":
            return self.postorder_print(self.root,"")
        elif traversal_type=="levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type=="reverselevelorder":
            return self.reverselevelorder_print(self.root)
        else:
            return False


    def preorder_print(self,start,traversal):
        #root-left-right
        if start:
            traversal+=(str(start.val)+ "-")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal):
        #left-root-right
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.val)+ "-")
            traversal=self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal):
        #left-right-root
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=(str(start.val)+ "-")
        return traversal

    def levelorder_print(self,start):
        if start is None:
            return
        x=Queue()
        x.enque(start)
        traversal=""
        while len(x)>0:
            traversal+=str(x.peek())+"-"
            node=x.dequeue()
            if node.left:
                x.enque(node.left)
            if node.right:
                x.enque(node.right)
        return traversal
        

    def reverselevelorder_print(self,start):
        if start is None:
            return
        x=Queue()
        x.enque(start)
        s=Stack()
        traversal=""
        while len(x)>0:
            
            node=x.dequeue()
            s.push(node.val)
            if node.right:
                x.enque(node.right)
            if node.left:
                x.enque(node.left)
        while not s.is_empty():
            traversal+=str(s.pop())+"-"
        return traversal
        
    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        return 1+max(left_height,right_height)

    def size_of_tree_iterative(self):
        if self.root is None:
            return 0
        s=Stack()
        s.push(self.root)
        size=1
        while not s.is_empty():
            node=s.pop()
            if node.left:
                size+=1
                s.push(node.left)
            if node.right:
                size+=1
                s.push(node.right)
        return size

    def size_recursive(self,node):
        if node is None:
            return 0
        return 1+self.size_recursive(node.left)+self.size_recursive(node.right)



tree=BinaryTree(1)                                                    #        1
tree.root.left=Node(2)                                                #      /   \
tree.root.right=Node(3)                                               #     2      3
tree.root.left.left=Node(4)                                           #   /  \    /  \
tree.root.left.right=Node(5)                                          #  4    5  6    7
tree.root.right.left=Node(6)              
tree.root.right.right=Node(7)      
print(tree.height(tree.root))
print(tree.size_of_tree_iterative())   
print(tree.size_recursive(tree.root))     
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))







