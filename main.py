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

# Exercsies Code
def comma_code(arr):
    last_element = arr[-1]
    arr.insert(-1, 'and ' + last_element)
    del arr[-1]
    return arr
    
def main():
    # print_name('*')
    # tuple_implementation()
    # convert_collections()
    # references()
    names = ['Sophia', 'Jackson', 'Emily']
    brands = ['Lenovo', 'Apple', 'Samsung', 'Xiaomi']
    currency = ['PHP', 'USD', 'CAD', 'SGD', 'EUR']
    print(comma_code(names))
    print(comma_code(brands))
    print(comma_code(currency))
    print()
    
if __name__ == '__main__':
    main()
