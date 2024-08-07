class MinHeap:
    def _init_(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def print_heap(self):
        print(self.heap)

    def remove_min(self):
        if len(self.heap) > 1:
            min_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            min_value = self.heap.pop()
        else:
            min_value = None
        return min_value

# Exemplo de uso:
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(15)
min_heap.insert(30)
min_heap.insert(40)

print("Heap após inserções:")
min_heap.print_heap()

print("Mínimo:", min_heap.get_min())
print("Removendo o mínimo:", min_heap.remove_min())
print("Heap após remoção:")
min_heap.print_heap()