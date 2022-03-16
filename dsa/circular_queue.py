

# Circular Queue 
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.cir_queue = [None] * size
    
    # Insert data in Circular Queue
    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("Circular Queue is full!!!")
        elif self.tail == -1:
            self.head = 0
            self.tail = 0
            self.cir_queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.cir_queue[self.tail] = data
    
    # Remove data from Circular Queue
    def dequeue(self):
        if self.head == -1:
            print("Circular Queue is empty!!!")
        elif self.head == self.tail:
            temp = self.cir_queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.cir_queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp

    # Print Circular Queue
    def print_cir_queue(self):
        if self.head == -1:
            print("Circular Queue is empty!!!")
        elif self.head <= self.tail:
            for i in range(self.head, self.tail + 1):
                print(self.cir_queue[i], end=" ")
        else:
            for i in range(self.head, self.size):
                print(self.cir_queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.cir_queue[i], end=" ")
        print()



# New Circular Queue 
circular_array = CircularQueue(5)

circular_array.enqueue(1)
circular_array.enqueue(2)
circular_array.enqueue(4)
circular_array.enqueue(8)
circular_array.enqueue(16)
circular_array.enqueue(32)

circular_array.print_cir_queue()

circular_array.dequeue()
circular_array.print_cir_queue()
