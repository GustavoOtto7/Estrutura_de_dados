class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def print_heap(self):
        print(self.heap)

    def remove_max(self):
        if len(self.heap) > 1:
            max_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            max_value = self.heap.pop()
        else:
            max_value = None
        return max_value

# Exemplo de uso:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(30)
max_heap.insert(40)

print("Heap após inserções:")
max_heap.print_heap()
print("Máximo:", max_heap.get_max())
print("Removendo o máximo:", max_heap.remove_max())
print("Heap após remoção:")
max_heap.print_heap()