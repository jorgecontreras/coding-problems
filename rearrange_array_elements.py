class MaxHeap:
    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.elements = [None for _ in range(size)]

    def get_left_child(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.elements[self.get_left_child(index)]

    def right_child(self, index):
        return self.elements[self.get_right_child(index)]

    def parent(self, index):
        return self.elements[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        tmp = self.elements[index_one]
        self.elements[index_one] = self.elements[index_two]
        self.elements[index_two] = tmp 

    def check_capacity(self):
        # if we have reached capacity, copy over the elements to a larger array
        if self.size == self.capacity:
            items = self.elements
            self.capacity *= 2
            self.elements = [None for _ in range(self.capacity)]

            for k,v in enumerate(items):
                self.elements[k] = v

    def peek(self):
        #return the root element (largest)
        if self.size == 0:
            return None

        return self.elements[0]

    def poll(self):
        if self.size == 0:
            return None
        
        item = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self, item):
        self.check_capacity()
        self.elements[self.size] = item
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) < self.elements[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapifyDown(self):
        index = 0
        while self.has_left_child(index):
            larger_child_index = self.get_left_child(index)
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                larger_child_index = self.get_right_child(index)

            if self.elements[index] > self.elements[larger_child_index]:
                break

            self.swap(index, larger_child_index)

            index = larger_child_index


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # add all the elements to a MaxHeap, the largest number will always be at the top
    heap = MaxHeap(10)
    for n in input_list:
        heap.add(n)

    # add all elements one by one into two arrays, intercalated
    num_1 = ""
    num_2 = ""
    
    while heap.size > 0:
        if len(num_1) - len(num_2) == 0:
            num_1 += str(heap.poll())
        else:
            num_2 += str(heap.poll())

    return int(num_1), int(num_2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[2, 2, 2, 3, 3, 3], [332, 322]])
test_function([[0, 0, 0, 0, 0, 0], [000, 000]])
test_function([[9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0], [999000, 999000]])
test_function([[1, 2, 3, 4, 5, 6, 6, 6, 6, 5, 4, 3, 2, 1], [6654321, 6654321]])
