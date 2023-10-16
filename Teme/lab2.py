from collections import Counter
from typing import List, Tuple, Any, Set


# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci(number: int) -> List[int]:
    fib_list = [0, 1]
    while len(fib_list) < number:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:number]


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def prime_numbers(numbers: List[int]) -> List[int]:
    prime_numbers_list = []
    for num in numbers:
        prime = 1
        if num < 2:
            prime = 0
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                prime = 0
        if prime == 1:
            prime_numbers_list.append(num)
    return prime_numbers_list


# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
# with b, a - b, b - a)

def list_operations(a: List[int], b: List[int]) -> Tuple[List[int], List[int], List[int], List[int]]:
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return intersection, union, a_minus_b, b_minus_a


# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and
# a start position (integer). The function will return the song composed by going though the musical notes beginning
# with the start position and following the moves given as parameter. Example : compose(["do", "re", "mi", "fa",
# "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose(notes: List[str], moves: List[int], start_position: int) -> List[str]:
    song = []
    current_position = start_position
    for move in moves:
        song.append(notes[current_position])
        current_position = (current_position + move) % len(notes)
    song.append(notes[current_position])
    return song


# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).

def replace_below_diagonal(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0
    return matrix


# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def items_appearing_x_times(x: int, *lists: List[Any]) -> List[Any]:
    all_items = [item for sublist in lists for item in sublist]
    item_counts = Counter(all_items)
    result = [item for item, count in item_counts.items() if count == x]
    return result


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2
# elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second
# element will be the greatest palindrome number.

def palindrome_values(numbers: List[int]) -> Tuple[int, int]:
    palindrome_list = []
    for number in numbers:
        if str(number) == str(number)[::-1]:
            palindrome_list.append(number)
    if not palindrome_list:
        return 0, 0
    nr_palindromes = len(palindrome_list)
    max_palindrome = max(palindrome_list)
    return nr_palindromes, max_palindrome


# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
# to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x. Example: x
# = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list
# of lists.

def filter_ascii_characters(x: int = 1, strings: List[str] = None, flag: bool = True) -> List[List[str]]:
    result_lists = []
    for s in strings:
        filtered_characters = []
        for char in s:
            if flag == True and ord(char) % x == 0:
                filtered_characters.append(char)
            if flag == False and ord(char) % x != 0:
                filtered_characters.append(char)
        result_lists.append(filtered_characters)
    return result_lists


# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
# and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the
# game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the
# seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
# closest row from the field.

def find_obstructed_seats(matrix: List[List[int]]) -> set[tuple[int, int]]:
    obstructed_seats = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            current_height = matrix[i][j]
            for k in range(i + 1, rows):
                if matrix[k][j] <= current_height:
                    obstructed_seats.add((k, j))
    return obstructed_seats


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the
# first tuple contains the first items in the lists, the second element contains the items on the position 2 in the
# lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def zip_lists(*input_lists: List) -> List[Tuple[Any, ...]]:
    max_len = max(len(lst) for lst in input_lists)
    result = []

    for i in range(max_len):
        current_tuple = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        result.append(current_tuple)

    return result


# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
# tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_tuples_by_third_char(list: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    return sorted(list, key=lambda x: x[1][2])


# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words: List[str]) -> List[List[str]]:
    rhyme_groups = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]

    result = list(rhyme_groups.values())
    return result


# Ex1
print("Ex1: ", fibonacci(10))
# Ex2
print("Ex2: ", prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ex 3
result = list_operations([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
print("Ex3: ")
print("Intersection: ", result[0])
print("Union: ", result[1])
print("A-B: ", result[2])
print("B-A: ", result[3])
# Ex 4
print("Ex 4: ", compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
# Ex 5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = replace_below_diagonal(matrix)
print("Ex 5: ")
for row in result:
    print(row)
# Ex 6
print("Ex 6: ", items_appearing_x_times(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
# Ex 7
print("Ex 7: ", palindrome_values([1221, 101, 1002, 23432, 123]))
# Ex 8
print("Ex 8: ", filter_ascii_characters(2, ["test", "hello", "lab002"], False))
# Ex 9
stadium_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
print("Ex 9: ", find_obstructed_seats(stadium_matrix))
# Ex 10
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print("Ex 10: ", zip_lists(list1, list2, list3))
# Ex 11
input_tuples = [('abc', 'bcd'), ('abc', 'zza')]
print("Ex 11: ", order_tuples_by_third_char(input_tuples))
# Ex 12
word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
print("Ex 12: ", group_by_rhyme(word_list))