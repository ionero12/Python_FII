from typing import Optional, Any, Union, Callable


# Ex 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Optional[Any]:
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self) -> Optional[Any]:
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.items) == 0


# Example usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print("Stack:", my_stack.items)
print("Peek:", my_stack.peek())
print("Pop:", my_stack.pop())
print("Stack after pop:", my_stack.items, "\n")


# Ex 2
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Optional[Any]:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self) -> Optional[Any]:
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.items) == 0


# Example usage:
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print("Queue:", my_queue.items)
print("Peek:", my_queue.peek())
print("Dequeue:", my_queue.dequeue())
print("Queue after dequeue:", my_queue.items, "\n")


# Ex 3
class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get(self, row: int, col: int) -> Optional[Union[int, float]]:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            return None

    def set(self, row: int, col: int, value: Union[int, float]) -> None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value

    def transpose(self) -> 'Matrix':
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        transposed_matrix = Matrix(self.cols, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply(self, other: 'Matrix') -> Optional['Matrix']:
        if self.cols != other.rows:
            return None

        result = Matrix(self.rows, other.cols)

        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))

        return result

    def apply_transform(self, transform: Callable[[float], float]) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transform(self.data[i][j])

    def iterate_elements(self, func: Callable[[int, int, Union[int, float]], None]) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                func(i, j, self.data[i][j])

    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print()
        print()


# Example usage:
matrix1 = Matrix(2, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)

print("Matrix 1:")
matrix1.print_matrix()

print("\nMatrix 2:")
matrix2.print_matrix()
print("\nMatrix 1 Transpose:")
matrix1.transpose().print_matrix()

result = matrix1.multiply(matrix2)
if result:
    print("\nMatrix Multiplication (Matrix 1 * Matrix 2):")
    result.print_matrix()

matrix1.apply_transform(lambda x: x * 2)
print("\nMatrix 1 after transformation:")
matrix1.print_matrix()


def print_element(i: int, j: int, value: Union[int, float]) -> None:
    print(f"Element at ({i}, {j}): {value}")


matrix1.iterate_elements(print_element)
