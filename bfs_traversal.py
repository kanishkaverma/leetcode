from typing import Deque

class Treenode: 
    def __init__(self,val): 
        self.val = val
        self.left, self.right = None,None 

def traverse(root): 
    result = []
    if root is None: 
        return result

    queue = Deque()
    queue.append(root)
    while queue: 
        level_size = len(queue)
        current_level = []
        for x in range(level_size): 
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left: 
                queue.append(current_node.left)
            if current_node.right: 
                queue.append(current_node.right)
        
        result.append(current_level)
    
    return result 


def main( ): 
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)
    print(f"level order transversal: {str(traverse(root))}")

main()


def traverse(root): 
    result = [ ]
    if root is None: 
        return root 
    queue = Deque()
    queue.append(root)

    while queue: 
        level_size = len(queue)
        level = []
        for x in range(level_size): 
            current_node = queue.popleft()
            queue.append(current_node.val)

            if current_node.left: 
                queue.append(current_node.left
                )
            if current_node.right: 
                queue.append(current_node.right)

        result.append(level)

    return result 