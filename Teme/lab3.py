from typing import List, Set, Tuple, Dict, Optional, Any


# 1. Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)
def set_operations(a: List[int], b: List[int]) -> Tuple[Set[int], Set[int], Set[int], Set[int]]:
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    ex1_result = (intersection, union, a_minus_b, b_minus_a)
    return ex1_result


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given
# text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'a': 3,
# 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
def count_characters(text: str) -> Dict[str, int]:
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


# 3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must
# be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def compare_dictionaries(dict1: Dict, dict2: Dict) -> bool:
    # Check if both objects are dictionaries
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key1 in dict1:
        val1, val2 = dict1[key1], dict2[key1]
        if isinstance(val1, dict) and isinstance(val2, dict):
            if not compare_dictionaries(val1, val2):
                return False
        elif isinstance(val1, (list, set)) and isinstance(val2, (list, set)):
            if not compare_lists_sets(val1, val2):
                return False
        elif val1 != val2:
            return False
    return True


def compare_lists_sets(list1: List, list2: List) -> bool:
    if len(list1) != len(list2):
        return False
    for elem1, elem2 in zip(list1, list2):
        if isinstance(elem1, dict) and isinstance(elem2, dict):
            if not compare_dictionaries(elem1, elem2):
                return False
        elif isinstance(elem1, (list, set)) and isinstance(elem2, (list, set)):
            if not compare_lists_sets(elem1, elem2):
                return False
        elif elem1 != elem2:
            return False
    return True


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "
def build_xml_element(tag: str, content: str, **attributes: Dict[str, str]) -> str:
    xml_element = f"<{tag}"
    for key1, val in attributes.items():
        xml_element += f' {key1}="{val}"'
    xml_element += f">{content}"
    xml_element += f"</{tag}>"
    return xml_element


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise. Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules
# are respected for "key1" and "key2" "key3" that does not appear in the rules.
def validate_dictionary(rules: Set[Tuple[str, str, str, str]], d: Dict[str, str]) -> bool:
    for key1, prefix, middle, suffix in rules:
        if key1 not in d:
            return False
        val = d[key1]
        if not (val.startswith(prefix) and val.endswith(suffix) and middle in val[1:-1]):
            return False
    return True


# 6.Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
# this objective).
def count_unique_and_duplicates(input_list: List[int]) -> Tuple[int, int]:
    unique = set()
    duplicate = set()
    for item in input_list:
        if item in unique and item not in duplicate:
            duplicate.add(item)
        else:
            unique.add(item)
    unique_items = [item for item in input_list if input_list.count(item) == 1]
    return len(unique_items), len(list(duplicate))


# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -. Ex: {1,2}, {2, 3} => { "{1, 2} | {2, 3}":  {1,
# 2, 3}, "{1, 2} & {2, 3}":  { 2 }, "{1, 2} - {2, 3}":  { 1 }, ... }
def set_operations_on_dictionaries(*sets: Set) -> Dict[str, Set]:
    ex7_result_dict = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]
            set_a = set(set_a)
            set_b = set(set_b)
            ex7_result_dict[f"{set_a} | {set_b}"] = set_a | set_b
            ex7_result_dict[f"{set_a} & {set_b}"] = set_a & set_b
            ex7_result_dict[f"{set_a} - {set_b}"] = set_a - set_b
            ex7_result_dict[f"{set_b} - {set_a}"] = set_b - set_a
    return ex7_result_dict


# 10. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string
# key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described. Ex: loop({'start':
# 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
def loop(mapping: Dict[str, Optional[str]]) -> List[str]:
    visited = set()
    ex10_result = []
    current_key = mapping.get('start')
    while current_key is not None and current_key not in visited:
        ex10_result.append(current_key)
        visited.add(current_key)
        current_key = mapping.get(current_key)
    return ex10_result


# 11. Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments adn will return the number of positional arguments whose values can be found among keyword arguments
# values. Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
def nr_positional_arguments(*args: Any, **kwargs: Any) -> int:
    count = 0
    arg_set = set(args)
    for val in kwargs.values():
        if val in arg_set:
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
result = compare_dictionaries({'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}},
                              {'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}})
print("Ex 3: ", result, "\n")
# Ex 4
print("Ex 4: ", build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"), "\n")
# Ex 5
print("Ex 5: ", validate_dictionary({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}), "\n")
# Ex 6
print("Ex 6: ", count_unique_and_duplicates([1, 2, 3, 4, 5, 6, 6, 7, 7]), "\n")
# Ex 7
print("Ex 7: ")
result_dict = set_operations_on_dictionaries({1, 2}, {2, 3})
for key, value in result_dict.items():
    print(f"{key}: {value}")
print()
# Ex 10
print("Ex 10: ", loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}), "\n")
# Ex 11
print("Ex 11: ", nr_positional_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5), "\n")
