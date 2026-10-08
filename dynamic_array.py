import ctypes

class MyList:
    def __init__(self):
        self.size = 1 #capacity of array
        self.n = 0 #currently stored item
        self.A = self.create_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):
        if self.size == self.n: #if no space left then we will resize
            self.resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n != 0:
            item = self.A[self.n-1]
            self.n = self.n-1
            return item
        else:
            return "Empty List"

    def clear(self):
        if self.n != 0:
            self.n = 0
            self.size = 1
            self.A = self.create_array(self.size)
        else:
            return "List is already Empty"
        
    def resize(self, new_capacity):
        #create a new array with new capacity
        B = self.create_array(new_capacity)
        self.size = new_capacity

        #copy item from old array to new array
        for i in range(self.n):
            B[i] = self.A[i]

        #reassign A
        self.A = B

    def __str__(self):
        #printing the result
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        return "[" + result[:-1] + "]"

    def __getitem__(self, index):
        if 0 <= index <self.n:
            return self.A[index]
        else:
            return "Index Out of Range"

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        else:
            return "Item not found"

    def create_array(self,capacity):
        #it create a c type array(static & referential) with size = capacity
        return (capacity*ctypes.py_object)()

    def inserting(self, index, value):
        if index > self.n or index < 0:
            return "Index out of range"
        
        if self.n == self.size:
            self.resize(self.size*2)
            
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        self.A[index] = value
        self.n += 1 

    def deleting_by_index(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n -= 1
        else:
            print("No such index found")

    def deleting_by_value(self, value):
        for i in range(self.n): 
            if self.A[i] == value:
                for j in range(i, self.n - 1):
                    self.A[j] = self.A[j + 1]
                self.n = self.n - 1
        else:
            print("No such element found")

if __name__ == "__main__":
    L = MyList()

    L.append("Akshat")
    L.append(45)
    L.append(18)
    L.append(7)

    print(L)
    print(len(L))
    print(L.find("Akshat"))

    L.inserting(2, "Rohit")
    print(L)

    L.deleting_by_index(100)
    print(L)