class Max_Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.indexMap = {}
        for i in range(len(self.data)):
            self.indexMap[self.data[i]] = i
        self.build_heap()

    def left(self, i):
        return 2*(i+1)

    def right(self, i):
        return 2*(i+1) - 1
    
    def parent(self, i):
        return (i+1)//2 - 1

    def build_heap(self):
        for i in range(len(data)//2-1, -1, -1):
            heapify(i)
    
    def heapify(self, i):
        cur_largest = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            cur_largest = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[cur_largest]:
            cur_largest = self.right(i)
        if cur_largest != i:
            self.data[cur_largest], self.data[i] = self.data[i], self.data[cur_largest]
            self.indexMap[self.data[i]], self.indexMap[self.data[cur_largest]] = i, cur_largest 
            self.heapify(cur_largest)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.indexMap[length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def contains(self, value):
        return value in self.data
    
    def increase_key(self, value, shift):
        self.data[self.indexMap[value]] += shift
        self.bubble_up(indexMap[value])

    def bubble_up(self, i):
        if i == 0:
            return 
        parent_index = self.parent(i)
        if self.data[parent_index] < self.data[i]:
            self.data[parent_index], self.data[i] = self.data[i], self.data[parent_index]
            self.indexMap[self.data[i]], self.indexMap[self.data[parent_index]] = i, parent_index
            self.bubble_up(parent_index)

    def extract_max(self):
        max_value = self.data[0]
        self.data[0], self.data[self.length-1] = self.data[self.length -1], self.data[0]
        length -= 1
        self.heapify(0)
        return max_value