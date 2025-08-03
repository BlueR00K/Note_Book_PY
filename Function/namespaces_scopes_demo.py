"""
namespaces_scopes_demo.py

A practical demonstration of Python namespaces and scopes, including usage of global and nonlocal keywords.
"""

# Built-in namespace example
from types import SimpleNamespace
print(len([1, 2, 3]))  # 'print' and 'len' are built-in

# Global variable
x = 'global x'


def outer():
    # Enclosing namespace
    x = 'outer x'

    def inner():
        # Local namespace
        x = 'inner x'
        print('Inner:', x)  # Prints 'inner x'
    inner()
    print('Outer:', x)      # Prints 'outer x'


outer()
print('Global:', x)         # Prints 'global x'

# LEGB rule demonstration
msg = 'global'


def legb_outer():
    msg = 'enclosing'

    def legb_inner():
        msg = 'local'
        print('LEGB Inner:', msg)  # Local scope
    legb_inner()
    print('LEGB Outer:', msg)      # Enclosing scope


legb_outer()
print('LEGB Global:', msg)         # Global scope

# Using global keyword
counter = 0


def increment_global():
    global counter
    counter += 1
    print('Global counter:', counter)


increment_global()

# Using nonlocal keyword


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print('Nonlocal count:', count)
    return increment


c = make_counter()
c()
c()

# Practical example: global and nonlocal together
user_total = 0


def user_counter(user_name):
    count = 0

    def increment():
        nonlocal count
        global user_total
        count += 1
        user_total += 1
        print(f"{user_name}'s count: {count}, Total count: {user_total}")
    return increment


alice_counter = user_counter('Alice')
bob_counter = user_counter('Bob')

alice_counter()  # Alice's count: 1, Total count: 1
alice_counter()  # Alice's count: 2, Total count: 2
bob_counter()    # Bob's count: 1, Total count: 3
alice_counter()  # Alice's count: 3, Total count: 4
bob_counter()    # Bob's count: 2, Total count: 5

# Scope pitfalls
x = 5


def foo():
    # Uncommenting the next line will cause UnboundLocalError
    # print(x)
    x = 10
    print('Foo local x:', x)


foo()
print('Global x after foo:', x)

# Dynamic namespace creation
person = SimpleNamespace(name='Alice', age=30)
print('Person name:', person.name)
