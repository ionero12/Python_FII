import math
import re
import sys


# 1. Find The greatest common divisor of multiple numbers read from the console.

def ex1():
    numbers = list(map(int, sys.argv[1:]))
    if len(numbers) < 2:
        print("Please add at least 2 numbers")
    result = numbers[0]
    for i in numbers[1:]:
        result = math.gcd(result, i)
    print(f"The greatest common divisor is: {result}")


# 2. Write a script that calculates how many vowels are in a string.

def ex2(string):
    count = 0
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1
    print(f"{string} has {count} vowels")


# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def ex3(string1, string2):
    result = string2.count(string1)
    print(f"{string1} occurrences in {string2} {result} times")


# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def ex4(string):
    result = [string[0].lower()]
    for i in string[1:]:
        if i.isupper():
            result.extend(['_', i.lower()])
        else:
            result.append(i)
    final = ''.join(result)
    print(f"The snake case for {string} is {final}")


# 5.Given a square matrix of characters write a script that prints the string obtained by going through the matrix in
# spiral order (as in the example):

def ex5(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    final = ''.join(result)
    print(f"{final}")


# 6. Write a function that validates if a number is a palindrome.

def ex6(number):
    string = str(number)
    result = string == string[::-1]
    print(f"The number {number} is palindrome: {result}")


# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
# extract only the first number that is found.

def ex7(string):
    match = re.search(r'\d+', string)
    result = int(match.group())
    print(f"The extracted number is: {result}")


# 8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
# format is 00011000, meaning 2 bits with value "1"

def ex8(number):
    return bin(number).count("1")


# 9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

def ex9(string):
    string = string.lower()
    letter_counts = {}
    for char in string:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    result = max(letter_counts, key=letter_counts.get)
    print(f"The most common letter is: {result}")


# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.
def ex10(string):
    result = len(string.split())
    print(f"In text there are {result} words")


ex1()
ex2("ananas")
ex3("aba", "abator")
ex4("CamelCase")
ex5([
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
])
ex6(1001)
ex7("Maria are 109 mere")
ex8(24)
ex9("albastru")
ex10("A inceput anul trei")
