# Reference: https://www.programiz.com/dsa/heap-data-structure

class Node:
    def __init__(self, val):
        self.val = val

    def setParent(self, parent):
        self.parent = parent





class Heap:

    def __init__(self, arr, type):
        self.arr = arr
        self.type = type # min or max


    def insert(self, val):
        newNode = Node(val)
        self.arr.append(newNode);
        nodeIndex = len(self.arr) - 1;
        if nodeIndex != 0:
            newNode.setParent(self.arr[(nodeIndex - 1) // 2])

        if self.type == "max":
            while newNode.parent and newNode.parent < newNode:
                currParent = newNode.parent
                parentIndex = self.arr.index(currParent)
                self.arr[nodeIndex], self.arr[parentIndex] = self.arr[parentIndex], self.arr[nodeIndex]
                newNode.setParent(currParent.parent)
                currParent.setParent(newNode)
                nodeIndex = parentIndex
        else:
            while newNode.parent and newNode.parent > newNode:
                currParent = newNode.parent
                parentIndex = self.arr.index(currParent)
                self.arr[nodeIndex], self.arr[parentIndex] = self.arr[parentIndex], self.arr[nodeIndex]
                newNode.setParent(currParent.parent)
                currParent.setParent(newNode)
                nodeIndex = parentIndex


    def heapify(self):
        if self.type == "max":



def heapSort(inputArr):
    # For item in arr, add to new heap



