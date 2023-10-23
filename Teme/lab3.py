from typing import List, Set, Tuple, Dict


# 1. Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)
def set_operations(a: List[int], b: List[int]) -> Tuple[Set[int], Set[int], Set[int], Set[int]]:
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)

    result = (intersection, union, a_minus_b, b_minus_a)
    return result


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given
# text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'a': 3,
# 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
def count_characters(text: str) -> Dict[str, int]:
    char_count = {}

    for char in text:
        # Use char.lower() to make the count case-insensitive
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


# 3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must
# be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def compare_dicts(dict1: Dict, dict2: Dict) -> bool:
    # Check if both objects are dictionaries
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    # Check if the keys are the same
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Recursively compare values
    for key in dict1:
        value1, value2 = dict1[key], dict2[key]

        # If the values are dictionaries, recursively compare them
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        # If the values are lists or sets, recursively compare them
        elif isinstance(value1, (list, set)) and isinstance(value2, (list, set)):
            if not compare_lists_sets(value1, value2):
                return False
        # For other types, use simple equality check
        elif value1 != value2:
            return False

    return True


def compare_lists_sets(list1: List, list2: List) -> bool:
    # Helper function to compare lists or sets recursively

    # Check if the lengths are the same
    if len(list1) != len(list2):
        return False

    # Recursively compare elements
    for elem1, elem2 in zip(list1, list2):
        # If elements are dictionaries, use the dictionary comparison function
        if isinstance(elem1, dict) and isinstance(elem2, dict):
            if not compare_dicts(elem1, elem2):
                return False
        # If elements are lists or sets, use the list/set comparison function
        elif isinstance(elem1, (list, set)) and isinstance(elem2, (list, set)):
            if not compare_lists_sets(elem1, elem2):
                return False
        # For other types, use simple equality check
        elif elem1 != elem2:
            return False

    return True


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "
def build_xml_element(tag: str, content: str, **attributes: Dict[str, str]) -> str:
    # Build the opening tag with attributes
    attribute_str = ' '.join([f'{key}="{value}"' for key, value in attributes.items()])
    opening_tag = f"<{tag} {attribute_str}>"

    # Build the closing tag
    closing_tag = f"</{tag}>"

    # Combine everything into the final XML element
    xml_element = f"{opening_tag}{content}{closing_tag}"

    return xml_element


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise. Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules
# are respected for "key1" and "key2" "key3" that does not appear in the rules.
def validate_dict(rules: Set[Tuple[str, str, str, str]], d: Dict[str, str]) -> bool:
    for key, prefix, middle, suffix in rules:
        # Check if the key is present in the dictionary
        if key not in d:
            return False

        value = d[key]

        # Check if the value satisfies the rule
        if not (value.startswith(prefix) and value.endswith(suffix) and middle in value[1:-1]):
            return False

    return True


# 6.Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
# this objective).
def count_unique_and_duplicates(lst: List) -> Tuple[int, int]:
    unique_elements = len(set(lst))
    duplicate_elements = len(lst) - unique_elements

    result = (unique_elements, duplicate_elements)
    return result


# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -. Ex: {1,2}, {2, 3} => { "{1, 2} | {2, 3}":  {1,
# 2, 3}, "{1, 2} & {2, 3}":  { 2 }, "{1, 2} - {2, 3}":  { 1 }, ... }
def set_operations_on_dict(*sets: Set) -> Dict[str, Set]:
    result_dict = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            # Ensure the input parameters are sets
            set_a = set(set_a)
            set_b = set(set_b)

            # Union
            result_dict[f"{set_a} | {set_b}"] = set_a | set_b

            # Intersection
            result_dict[f"{set_a} & {set_b}"] = set_a & set_b

            # Set difference a - b
            result_dict[f"{set_a} - {set_b}"] = set_a - set_b

            # Set difference b - a
            result_dict[f"{set_b} - {set_a}"] = set_b - set_a

    return result_dict


# 10. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string
# key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described. Ex: loop({'start':
# 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
def loop(mapping):
    visited = set()
    result = []
    current_key = mapping.get('start')

    while current_key is not None and current_key not in visited:
        result.append(current_key)
        visited.add(current_key)
        current_key = mapping.get(current_key)

    return result


# 11. Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments adn will return the number of positional arguments whose values can be found among keyword arguments
# values. Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
def my_function(*args, **kwargs):
    count = 0
    arg_set = set(args)

    for value in kwargs.values():
        if value in arg_set:
            count += 1

    return count


# Ex 1
result_sets = set_operations([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print("Ex 1:")
print("Intersection:", result_sets[0])
print("Union:", result_sets[1])
print("A - B:", result_sets[2])
print("B - A:", result_sets[3], "\n")
# Ex 2
result_dict = count_characters("Ana has apples.")
print("Ex 2: ", result_dict, "\n")
# Ex 3
result = compare_dicts({'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}}, {'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}})
print("Ex 3: ", result, "\n")
# Ex 4
print("Ex 4: ", build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"), "\n")
# Ex 5
print("Ex 5: ", validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                              {"key1": "come inside, it's too cold out", "key3": "this is not valid"}), "\n")
# Ex 6 -- nu s sigura daca e bn
print("Ex 6: ", count_unique_and_duplicates([1, 2, 3, 4, 5, 6, 6, 7, 7]), "\n")
# Ex 7
print("Ex 7: ")
result_dict = set_operations_on_dict({1, 2}, {2, 3})
for key, value in result_dict.items():
    print(f"{key}: {value}")
# Ex 8
# Ex 9
# Ex 10
print("Ex 10: ", loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}), "\n")
# Ex 11
print("Ex 11: ", my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5), "\n")
