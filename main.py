import numpy as np

def print_even_numbers():
    for i in range(2,21,2):
        print(i)
def total_sum(numbers):
    total=0
    for num in numbers:
        total += num
    return total
def print_each_character(str):
    for char in str:
        print(char,end="")
    print("")
def multiplication_table():
    for i in range(1,11):
        for j in range(1,6):
            print (i*j,end=" ")
        print(" ")
def count_vowels(str):
    vowels_counter = 0
    for char in str:
        if char in "aeiouAEIOU":
            vowels_counter += 1
    return vowels_counter
def count_down():
    i = 10
    while i > 0:
        print (i)
        i -= 1
def sum_until_zero():
    total = 0
    while True:
        num = int(input(f'please insert an int, 0 to stop'))
        total += num
        if num == 0:
            break
    return total
def guess_the_number(number):
    while True:
        guess_number=int(input('Please guess what is the number?'))
        if guess_number == number:
            return ("It's a guess!")
        else:
            print("Try again!")
def even_numbers_with_while():
    i=2
    while i < 51:
        print(i)
        i += 2
def password_check(password):
    while True:
        enter_pass=input('Please enter the password to continue')
        if enter_pass == password:
            return ('Welcome')
        else:
            print('Please try again')
def user_details(user):
    for key,value in user.items():
        print(key,value)
def find_a_key(dict,key):
    if key in dict.keys():
        return True
    else:
        return False
def list_of_squares():
    for i in range(1,10):
        print(i*i)
def remove_duplicates(list):
    new_list = []
    for num in list:
        if new_list.count(num) == 0:
            new_list.append(num)
    return new_list
def find_maximum_and_minimum(lst):
    max_num=max(lst)
    min_num=min(lst)
    return (f'maximun num is: {max_num} & minimum num is: {min_num}')
def right_angle_triangle():
    for i in range(1,7):
        for j in range(1,i+1):
            print('*',end="")
        print("")
def prime_numbers():
    for num in range(2,51):
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
def matrix_multiply(A,B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        return "Matrices cannot be multiplied"
    result = np.zeros((cols_B,rows_A),dtype=int)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
def flatten(nested_list):
    flatten_list = []
    for sublist in nested_list:
        for item in sublist:
            flatten_list.append(item)
    return flatten_list
def find_common_elements(list1,list2):
    common_elements=[]
    for num in list1:
            if num in list2:
                if common_elements.count(num) == 0:
                    common_elements.append(num)
    return common_elements
def collatz_sequence(num):
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3+1
    sequence.append(1)
    return sequence
def fibonacci_sequance(limit):
    sequance = [0,1]
    i = 2
    while sequance[-1] < limit:
        next_value = sequance[i-2]+sequance[i-1]
        sequance.append(next_value)
        i += 1
    return sequance
def guess_game(num):
    while True:
        guess = int(input('Please type you guess number'))
        if guess == num:
            return 'Correct!'
        elif guess > num:
            print('Too high')
        elif guess < num:
            print('Too low')
def factorial_calc(num):
    i = 1
    res = 1
    while i <= num:
        res *= i
        i += 1
    return res
def digits_sum():
    num = input('Please type a number')
    i = 0
    res = 0
    while i < len(num):
        if num[i].isdigit():
            res += int(num[i])
        i += 1
    return res
def merge_dicts(dict1,dict2):
    dict1_c = dict1.copy()
    dict1_c.update(dict2)
    return dict1_c
def invert_dict(dict):
    inverted_dict = {}
    for key, value in dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict
def group_by_key(t_list):
    grouped_dict = {}
    for key,value in t_list:
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(value)
    return grouped_dict
def words_frequency(sentence):
    sentence = sentence.upper()
    words_frequency_dict = {}
    words = sentence.split(" ")
    for word in words:
        if word in words_frequency_dict:
            words_frequency_dict[word] += 1
        else:
            words_frequency_dict[word] = 1
    return words_frequency_dict
def rotate_90_degrees_clockwise(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = np.zeros((cols, rows),dtype=int)
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    rotated_matrix = np.zeros((cols, rows),dtype=int)
    for i in range(cols):
            rotated_matrix[i] = transposed_matrix[i][::-1]
    return rotated_matrix
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j] == target:
                if (lst[i],lst[j]) not in pairs and (lst[j],lst[i]) not in pairs:
                    pairs.append((lst[i],lst[j]))
    return pairs
def remove_even_numbers(lst):
    new_list = []
    for num in lst:
        if num % 2 != 0:
            new_list.append(num)
    return new_list
def matrix_diagonal_sum(matrix):
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(len(matrix)):
        diagonal_1 += matrix[i][i]
        diagonal_2 += matrix[i][len(matrix) - 1 - i]
    return f'Matrix Diagonal1 Sum: {diagonal_1}, Matrix Diagonal2 Sum: {diagonal_2}'
if __name__ == '__main__':

    #for loops

    print_even_numbers()
    numbers = [1, 2, 3, 4, 5]
    print("List's Total:", total_sum(numbers))
    print_each_character("Python")
    multiplication_table()
    print("number of vowels in the string:", count_vowels("hello world"))

    #while loops

    count_down()
    print('total sum is:',sum_until_zero())
    print(guess_the_number(6))
    even_numbers_with_while()
    password='12345'
    print(password_check(password))

    #dictionaries

    user = {'name':'Daphna','age':35,'city':'Tel Aviv'}
    user['age'] = 34
    print(user)
    user.pop('age')
    print(user)
    user_details(user)
    print(find_a_key(user,'age'))

    #lists

    list_of_squares()
    print(remove_duplicates([1,2,3,4,5,2,4]))
    print(find_maximum_and_minimum([100,500,34,6,-1,0]))

    #for loops harder

    right_angle_triangle()
    prime_numbers()
    A = [[4],[5],[6]]
    B = [[1,2,3]]
    print(matrix_multiply(A,B))
    nested_list = [[1, 2], [3, 4], [5]]
    print(flatten(nested_list))
    list1 = [1,2,2,3,4,5]
    list2 = [2,6,8,6,4]

    #while loops harder

    print(find_common_elements(list1,list2))
    print(collatz_sequence(12))
    print(fibonacci_sequance(45))
    print(guess_game(10))
    number = int(input("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial_calc(number)
        print(f"The factorial of {number} is {result}.")
    print(digits_sum())

    #dictionary harder
    
    dict1 = {'name':'Daphna'}
    dict2 = {'last_name':'Kirshner'}
    print(merge_dicts(dict1,dict2))
    original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    inverted_dict = invert_dict(original_dict)
    print(inverted_dict)
    t_list = [(1, 2), (3, 4), (5, 6)]
    print(t_list[0][1])
    t_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
    print(group_by_key(t_list))
    print(words_frequency('i love Israel Ogalbo and i am living in Israel'))

    #lists harder

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(rotate_90_degrees_clockwise(matrix))
    lst = [1, 5, 8, 5, 3, 4, 6, 8]
    print(find_pairs(lst, 9))
    reversed_list = lst[::1]
    print(reversed_list)
    every_second = lst[::2]
    print(every_second)
    print(remove_even_numbers(lst))
    print(matrix_diagonal_sum(matrix))