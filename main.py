import copy
def notes():
    '''
    -------- Tuples --------
    You can use tuples to convey to anyone reading your code that you
don’t intend for that sequence of values to change. If you need an ordered
sequence of values that never changes, use a tuple. A second benefit of
using tuples instead of lists is that, because they are immutable and their
contents don’t change, Python can implement some optimizations that
make code using tuples slightly faster than code using lists.

    -------- References --------
    for string, int, list - it stores the value itself
    for list, dict - it stores the reference
    
    -------- copy() and deepcopy() --------
    using copy() prevents the issue with referencing lists
    using deepcopy() prevents the with referencing 2D lists
    the key difference is that copy() creates a shallow copy that shares references to the same objects within the list, while deepcopy() creates a deep copy with new objects for the elements, ensuring that changes in one do not affect the other. 
    '''

def print_name(character):
    name = 'python'
    for i in name:
        print(f'{character * 5} {i} {character * 5}')

def tuple_implementation():
    # Changing elements - stackoverflow
    my_tuple = (1, 2, 3)
    my_tuple += (400, 500,)
    print(my_tuple)
    print(500 in my_tuple)
    
    # my_tuple = list(my_tuple)
    # my_tuple.append(50)
    # my_tuple.insert(0, 100)
    # my_tuple = tuple(my_tuple)
    # print(my_tuple)

def convert_collections():
    animals = ['dog', 'cat', 'chicken', 'lion']
    print(animals)
    print(type(animals))
    print('Converting into tuple ...')
    animals = tuple(animals)
    print(animals)
    print(type(animals))
    print()
    currency = ('PHP', 'USD', 'CAD', 'SGD', 'EUR')
    print(currency)
    print(type(currency))
    currency = list(currency)
    print(currency)
    print(type(currency))
    
def references():
    brands = ['Lenovo', 'Apple', 'Samsung', 'Xiaomi']
    print(brands)
    another_brands = brands
    another_brands[0] = 'Nokia'
    print(another_brands)
    print(brands)

def copy_deep():
    print('copy()')
    letters = ['a', 'b', 'c', 'd']
    spam = copy.copy(letters)
    letters[0] = 'laj'
    letters.append('e')
    letters.insert(1, 'u')
    print(letters)
    print(spam)
    print()
    
    print('without deepcopy()')
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(arr)
    my_arr = copy.copy(arr)
    my_arr[0][0] = 100
    print(arr)
    print(my_arr)
    print()
    
    print('with deepcopy()')
    your_arr = [[900, 800, 700], [600, 500, 400], [300, 200, 100]]
    our_arr = copy.deepcopy(arr)
    your_arr[0][0] = 350
    your_arr[1][0] = 111
    print(our_arr)
    print(your_arr)
    

# Exercsies Code
def comma_code(arr):
    last_element = arr[-1]
    arr.insert(-1, 'and ' + last_element)
    del arr[-1]
    return arr

def character_picture_grid():
    grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]
    print(grid)

def exercises():
    # Comma Code
    '''
    names = ['Sophia', 'Jackson', 'Emily']
    brands = ['Lenovo', 'Apple', 'Samsung', 'Xiaomi']
    currency = ['PHP', 'USD', 'CAD', 'SGD', 'EUR']
    print(comma_code(names))
    print(comma_code(brands))
    print(comma_code(currency))
    '''
    character_picture_grid()

def practice_questions():
    print('1. What is []?')
    print('Answer: List is a mutable data structure in python. List represents two square brackets')
    print('2. How would you assign the value hello as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)')
    spam = [2, 4, 6, 8, 10]
    spam[2] = 'Hello'
    print(f'Answer: {spam}')
    print('3. What does spam[int(3 * 2) / 11] evaluate to?')
    print('Answer: ' + str(spam[int(3 * 2) // 11]) + ' - Index: 0')
    print('4. What does spam[-1] evaluate to ?')
    print('Answer: Last Element: ' + str(spam[-1]))
    print('45 What does spam[-2] evaluate to ?')
    print('Answer: Second Last Element: ' + str(spam[-2]))
    bacon = [3.14, 'cat', 11, 'cat', True]
    print(bacon)
    print('6. What does bacon.index(cat) evaluate to?')
    print('Answer: ' + str(bacon.index('cat')))
    print('7. What does bacon.append(99) make the list value in bacon look like?')
    bacon.append(99)
    print('Answer: ' + str(bacon))
    print('8. What does bacon.remove(cat) make the list value in bacon look like?')
    bacon.remove('cat')
    print(f'Answer: {bacon}')  # It removes the first occurence of cat
    print('9. What are the operators for list concatenation and list replication?')
    print('Answer: List Concatenation (+), List Replication (*)')
    print('10. What is the difference between the append() and insert() list methods?')
    print('Answer: append() - adds the element to the end of the list, insert() - adds the element to the specified index')
    print('11. What are two ways to remove values from a list?')
    print('Answer: del and remove()')
    print('12. Name a few ways that list values are similar to string values')
    print('Answer: ')
    print('13. What is the difference between lists and tuples?')
    print('Answer: Lists are mutable and changable, compared to tuples wherein the values are immutable and fixed. But, we can wrap the tuple with list() to convert it into list then tuple again')
    print('How do you type the tuple value that has just the integer value 42 in it?')
    numbers = (42,)
    print(f'Answers: {numbers}')
    print('15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?')
    print('Answer: wrap the variable with either tuple or list, depends on the requirement')
    print('16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?')
    print('Answer: They just contain reference to the list')
    print('17. What is the difference between copy.copy() and copy.deepcopy()?')
    print('Answer: copy() - is used for 1D List if we want to create a copy of a list and modify it without changing the original one.\ndeepcopy() - is used for multi-dimension list if we want to create a copy of list and modify it without changing the original one')
    
def main():
    # print_name('*')
    # tuple_implementation()
    # convert_collections()
    # references()
    exercises()
    # copy_deep()
    # practice_questions()
    print()

if __name__ == '__main__':
    main()
