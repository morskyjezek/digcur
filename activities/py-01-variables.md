# Python 1: Expressions, Variables, Types, Inputs

### Python basics

Indentation is important in Python. Each line typically indicates an individual expression or statement of processing instructions. Lines that are indented indicate subroutines.

Reserved words

## Statements

Statements are "unit[s] of code that the Python interpreter can execute".[1] Above, for example, the assignment of a value to a variable is an assignment statement. The functions, like `print()`, are also statements. Statements often correspond to the line or two of input that you might make use of
in interactive mode. Statements are often placed on a single line in python, while
dependent statements or conditionals that become part of a larger loop are placed
on the next line and indented. Various guides for the style of code writing in python are
given in the "Style Guide for Python Code".[2]

## Responses

Python expressions are evaluated and will return a response. In some cases this
response is formally requested using the word _return_ in a function. Other times,
the response may be output through the `print()` function.

Mathematical expressions may evaluate according to usual math functions, such as basic operations:

Other expressions may evaluate as boolean and return `True` or `False`:

```
!= # Not equal
== # Equal / equivalent
>  # greater than
<  # less than
<= # less than or equal to
```

## Data Types

We talked about three main data types: integers, strings, and lists.
There are many other data types

## Iterations

Iteration, or looping, is a common technique in many computer programs.
It is a basic pattern that initiates a request to work through a list
and apply the same set of operations over and over.

We looked at the basic syntax for iteration in python, which follows this general pattern:

```
for ________ in ________: # for the subunits in a given things (may be a variable or group of data)
    ________ # do this thing
```

Here's an example, using the `cheeses` list:

```python
cheeses = ['brie', 'eidam', 'cheddar', 'gouda', 'gorgonzola', 'camembert']

for cheese in cheeses:
    print(cheese, len(cheese))
```

## Reflection activity

1.

### More Practice

Find basic, interactive problems and practice activities here: https://codingbat.com/python

An additional resource is the open [Python Textbook](https://python-textbok.readthedocs.io/en/1.0/index.html).

### Credits
This content generously draws up on the work of Charles Severance in [_Python for Informatics_](http://www.pythonlearn.com/book.php) and [_Python for Everybody_](https://www.py4e.com/).

[1]: https://www.py4e.com/html3/02-variables "Python 4 Everybody: Variables"
[2]: https://www.python.org/dev/peps/pep-0008/ "PEP 8"
