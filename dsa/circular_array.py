# Circular Fixed Array

class CircularArray:
    def __init__(self, length):
        self.array = [None] * length
        self.length = length
        self.front = 0
        self.back = 0

    def apend(self, value):
        if self.front == self.back and not self.array[self.back]:
            self.array[self.back] = value
            return True
        else:
            index = (self.back + 1) % self.length
            if index == self.front:
                return False
            self.array[index] = value
            self.back = index
            return True
    
    def prepend(self, value):
        if self.front == self.back and not self.array[self.back]:
            self.array[self.front] = value
            return True
        else:
            index = (self.front - 1) % self.length
            if index == self.back:
                return False
            self.array[index] = value
            self.front = index
            return True

    def pop(self):
        if self.array[self.back] == None:
            return None
        else:
            temp = self.array[self.back] 
            self.array[self.back] = None
            if self.array[self.back - 1] != None:
                self.back -=1 
            return temp
            

    def pop_first(self):
        if self.array[self.front] == None:
            return None
        else:
            temp = self.array[self.front]
            self.array[self.front] = None
            if self.array[self.front + 1] != None:
                self.front += 1
            return temp 

cir_arr =  CircularArray(10)

cir_arr.apend(5)
cir_arr.apend(9)
cir_arr.apend(11)
cir_arr.apend(18)
cir_arr.apend(25)

print(cir_arr.array)

