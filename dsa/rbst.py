class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive Binary Search Tree
class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_constains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_constains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value  < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)


        