# Link List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        prev = self.head
        while prev is not None:
            print(prev.value)
            prev = prev.next


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None
        prev = self.head
        pre = self.head
        while(prev.next):
            pre = prev
            prev = prev.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None
            return None
        return prev.value 


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        prev = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return prev.value


    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        prev = self.head
        for _ in range(index):
            prev = prev.next
        return prev


    def set_value(self, index, value):
        prev = self.get(index)
        if prev:
            prev.value = value
            return True
        return False


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        prev = self.get(index-1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1 
        return True


    def remove(self, index):
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()       

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
 
        return temp.value


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next 
        before = None 

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




my_link_list = LinkList(0)
my_link_list.append(1)
my_link_list.append(2)
my_link_list.append(3)
my_link_list.append(4)

my_link_list.print_list()
print()

print('return value: ', my_link_list.remove(0))
my_link_list.print_list()
print()