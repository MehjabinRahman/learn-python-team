"""Function Definition

@see: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

The keyword def introduces a function definition. It must be followed by the function name and the
parenthesized list of formal parameters. The statements that form the body of the function start at
the next line, and must be indented.
"""

import pytest


def fibonacci_function_example(number_limit):
    """Generate a Fibonacci series up to number_limit.

    The first statement of the function body can optionally be a string literal; this string
    literal is the function’s documentation string, or docstring. There are tools which use
    docstrings to automatically produce online or printed documentation, or to let the user
    interactively browse through code; it’s good practice to include docstrings in code that you
    write, so make a habit of it.
    """

    # The execution of a function introduces a new symbol table used for the local variables of the
    # function. More precisely, all variable assignments in a function store the value in the local
    # symbol table; whereas variable references first look in the local symbol table, then in the
    # local symbol tables of enclosing functions, then in the global symbol table, and finally in
    # the table of built-in names. Thus, global variables cannot be directly assigned a value
    # within a function (unless named in a global statement), although they may be referenced.
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        # The statement result.append(a) calls a method of the list object result. A method is a
        # function that ‘belongs’ to an object and is named obj.methodname, where obj is some
        # object (this may be an expression), and methodname is the name of a method that is
        # defined by the object’s type. Different types define different methods. Methods of
        # different types may have the same name without causing ambiguity. (It is possible to
        # define your own object types and methods, using classes, see Classes) The method
        # append() shown in the example is defined for list objects; it adds a new element at
        # the end of the list. In this example it is equivalent to result = result + [a], but
        # more efficient.
        fibonacci_list.append(previous_number)
        # This is multiple assignment statement. We make current number to be previous one and the
        # sum of previous and current to be a new current.
        previous_number, current_number = current_number, previous_number + current_number

    # The return statement returns with a value from a function. return without an expression
    # argument returns None. Falling off the end of a function also returns None.
    return fibonacci_list


def test_function_definition():
    """Function Definition"""

    # Now call the function we just defined.
    assert fibonacci_function_example(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # A function definition introduces the function name in the current symbol table. The value of
    # the function name has a type that is recognized by the interpreter as a user-defined function.
    # This value can be assigned to another name which can then also be used as a function. This
    # serves as a general renaming mechanism
    fibonacci_function_clone = fibonacci_function_example
    assert fibonacci_function_clone(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # In Python, functions are first class citizens, they are objects and that means we can do a
    # lot of useful stuff with them.

    # Assign functions to variables.

    def greet(name):
        return 'Hello, ' + name

    greet_someone = greet

    assert greet_someone('John') == 'Hello, John'

    # Define functions inside other functions.

    def greet_again(name):
        def get_message():
            return 'Hello, '

        result = get_message() + name
        return result

    assert greet_again('John') == 'Hello, John'

    # Functions can be passed as parameters to other functions.

    def greet_one_more(name):
        return 'Hello, ' + name

    def call_func(func):
        other_name = 'John'
        return func(other_name)

    assert call_func(greet_one_more) == 'Hello, John'

    # Functions can return other functions. In other words, functions generating other functions.

    def compose_greet_func():
        def get_message():
            return 'Hello there!'

        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == 'Hello there!'

    # Inner functions have access to the enclosing scope.

    # More commonly known as a closure. A very powerful pattern that we will come across while
    # building decorators. Another thing to note, Python only allows read access to the outer
    # scope and not assignment. Notice how we modified the example above to read a "name" argument
    # from the enclosing scope of the inner function and return the new function.

    def compose_greet_func_with_closure(name):
        def get_message():
            return 'Hello there, ' + name + '!'

        return get_message

    greet_with_closure = compose_greet_func_with_closure('John')

    assert greet_with_closure() == 'Hello there, John!'


def test_function_default_and_keyword_parameters():
    """Default and keyword parameters

    A parameter can have a default value. If the caller does not pass that argument, the default
    value is used. Arguments can also be passed by name (keyword arguments), so their order does
    not matter.
    """

    def make_greeting(name, greeting='Hello', punctuation='!'):
        return greeting + ', ' + name + punctuation

    # Only the required parameter is given, so both defaults are used.
    assert make_greeting('Omar') == 'Hello, Omar!'

    # A positional argument replaces the first default.
    assert make_greeting('Omar', 'Hi') == 'Hi, Omar!'

    # Keyword arguments can be given in any order and can skip a default in the middle.
    assert make_greeting('Omar', punctuation='?') == 'Hello, Omar?'
    assert make_greeting(punctuation='.', name='Omar', greeting='Bye') == 'Bye, Omar.'


def test_function_return_values():
    """Return values

    A function can send back more than one value by returning them separated by commas. Python
    packs them into a tuple, and the caller can unpack the tuple into separate variables. A
    function that ends without a return statement (or uses return with no value) returns None.
    """

    def get_min_and_max(numbers):
        return min(numbers), max(numbers)

    # The two returned values come back as one tuple.
    result = get_min_and_max([4, 9, 1, 7])
    assert result == (1, 9)
    assert isinstance(result, tuple)

    # The tuple can be unpacked straight into two variables.
    smallest, largest = get_min_and_max([4, 9, 1, 7])
    assert smallest == 1
    assert largest == 9

    # No return statement means the function returns None.
    def add_to_list(items, value):
        items.append(value)

    my_list = [1, 2]
    assert add_to_list(my_list, 3) is None
    assert my_list == [1, 2, 3]


def test_function_input_validation():
    """Simple input validation

    A function can check its arguments before using them. If a value does not make sense, the
    function can stop and raise an exception such as ValueError instead of returning a wrong
    result. pytest.raises lets the test check that the error really happens.
    """

    def calculate_average(numbers):
        if not numbers:
            raise ValueError('numbers must not be empty')
        return sum(numbers) / len(numbers)

    # Valid input returns the normal result.
    assert calculate_average([2, 4, 6]) == 4

    # An empty list is rejected with a ValueError.
    with pytest.raises(ValueError):
        calculate_average([])

    def set_age(age):
        if age < 0:
            raise ValueError('age cannot be negative')
        return age

    assert set_age(20) == 20

    # The error message can also be checked.
    with pytest.raises(ValueError, match='age cannot be negative'):
        set_age(-5)
