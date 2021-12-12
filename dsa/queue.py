class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next 

    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1
        
        return True


    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1

        return temp



queue = Queue(4)
queue.print_queue()
print('\n')

queue.enqueue(777)
queue.print_queue()
print('\n')

queue.enqueue(45545)
queue.print_queue()
print('\n')

queue.enqueue(88888888888)
queue.print_queue()
print('\n')

queue.dequeue()
queue.print_queue()
print('\n')

queue.dequeue()
queue.print_queue()
print('\n')


queue.dequeue()
queue.print_queue()
print('\n')


queue.dequeue()
queue.print_queue()
print('\n')

print('dequeue: ', queue.dequeue())
queue.print_queue()
print('\n')

