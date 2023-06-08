import math
import random

class Heap:

    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.indexMap = {}
        for i in range(len(self.data)):
            self.indexMap[self.data[i]] = i
        self.build_heap()

    def build_heap():
        # to get to the first non-leaf node from the bottom
        # going from the back, count backwards
        for i in range(len(self.data)//2 - 1, -1,-1):
            # bottom up approach to set up a heap
            heapify(self.data[i])
        
    def heapify(self, i):
        curlargest_childNode = i
        # checks for index out of bound
        if self.left(i) < self.length and self.data[i] < self.data[self.left(i)]:
            curlargest_childNode = self.left(i)
        if self.right(i) < self.length and self.data[curlargest_childNode] < self.data[self.right[i]]:
            curlargest_childNode = self.right(i)
        if curlargest_childNode != i:
            # swap
            self.data[curlargest_childNode], self.data[i] = self.data[i], self.data[curlargest_childNode]
            # update out index Map because we're swapping values
            self.indexMap[data[curlargest_childNode]], self.indexMap[data[i]] = curlargest_childNode, i
            heapify(curlargest_childNode)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        if i == 0:
            return
        if self.parent(i) < self.data[i]:
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            # update out index Map because we're swapping values
            self.indexMap[data[self.parent(i)]], self.indexMap[data[i]] = self.parent(i), i
            return bubble_up(self.parent(i))

    def extract_max(self):
        self.data[0], self.data[self.length-1] = self.data[self.length-1], self.data[0]
        # update out index Map because we're swapping values
        self.indexMap[data[self.length-1]], self.indexMap[data[0]] = self.length-1, 0
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def constains(self, valye):
        return value in self.data

    def increase_key(self, value, shift):
        self.data[self.map[value]] += shift
        self.bubble_up(self.map[value])


    def left(self, i):
        # anything multiply by 0 is 0
        return 2*(i+1) - 1
    
    def right(self, i):
        return 2*(i+1)

    def parent(self, i):
        return (i + 1) // 2 - 1
    
    def __str__(self):
        height = math.cell(math.log(self.length+1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i+1) - 1, self.length)):
                s += " " * whitespaces
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s