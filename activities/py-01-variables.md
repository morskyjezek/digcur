# Python 1: Expressions, Variables, Types, Inputs

### Python basics

Indentation is important in Python. Each line typically indicates an individual expression or statement of processing instructions. Lines that are indented indicate nested statements within loops or subroutines.

## Variables

Python assigns values to variables using the `=`. It is useful for understandability of any python code you write to use meaningful names for variables. That is, something like `data_file` rather than plain old `x` or `fahbio3095ja`, which are easier to lose track of. Variables can be named with combinations of letters and numbers. Certain special characters are not allowed in variable names and variable names may not begin with a number. Python convention is to use underscores (`_`) between parts of a variable name (like `users_input`), but you might also use camel case or another convention.

## Reserved words

Python reserves 33 short words or phrases, which have specific meanings within any python program. These reserved cannot be used as variable names. When you're working in a smart text editor or in a Jupyter Notebook, these words will automatically highlight, so it can help to point out their status. These words are:

```
and       del       from      None      True
as        elif      global    nonlocal  try
assert    else      if        not       while
break     except    import    or        with
class     False     in        pass      yield
continue  finally   is        raise
def       for       lambda    return
```

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

Mathematical expressions may evaluate according to usual math functions, such as basic operations like addition, subtraction, multiplication, and division.

Other "comparison operators" allow you to evaluate two things to return a single value known as a Boolean value, which python will evaluate as either `True` or `False`. Here are the comparison operators

| Operator | Meaning |
| ----- | ----- |
| != | Not equal |
| == | Equal / equivalent |
| >  | greater than |
| <  | less than |
| <= | less than or equal to |
| >= | greater than or equal to |

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

Here's an example with a string:

```python
word = 'terps'               # the word variable is assigned
for i in word:               # we initiate the iteration with a for loop
    print(word.index(i), i)  # we use the index() method to print the value of the index position and also to print the index letter  
```

Here's an example, using the `cheeses` list:

```python
cheeses = ['brie', 'eidam', 'cheddar', 'gouda', 'gorgonzola', 'camembert']

for cheese in cheeses:
    print(cheese, len(cheese))
```

## Reflection activity

1. What is the operator that indicates equivalency ("equal to") and what is the operator for assignment ("name a variable")? Give an example of each.
1. What are the types of these variables: `mascot = 'Testudo'`, `founded = 1856`, `cheeses = ['brie', 'gouda', 'mozarella']`. Hint: use the built-in `type()` function to determine the data type.
1. Python has a built-in function `input()` that allows you to ask the user for input. To add a prompt to the input, you can place a string inside the parentheses as an argument, like so: `input('What is your name?')`. Write a short program that prompts the user for their name, then outputs a greeting. Use the `say_hello()` function from last week as a model. _Hints: you can assign the input to a variable. Then, use a function you define or the `print()` function to produce a greeting with the new variable that you created._  

<!-- 1. We saw that each line in a python program evaluates and can produce a result. This can be some sort of output that we could use again, and it could also be a Boolean value (that is, `True` or `False`). What are the results of the following statements, and what do you think is happening? Use the python notebook to evaluate each statement:
1.  We talked about how each line may be an expression, and python will evaluate each expression. This can be an output, but it also can be a Boolean condition (`True` or `False`). Using the comparison operators and the Boolean values, record the results of the following expressions:
  * (5 > 4) and () -->

### More Practice

Find basic, interactive problems and practice activities here: https://codingbat.com/python

An additional resource is the open [Python Textbook](https://python-textbok.readthedocs.io/en/1.0/index.html).

### Credits
This content generously draws up on the work of Charles Severance in [_Python for Informatics_](http://www.pythonlearn.com/book.php) and [_Python for Everybody_](https://www.py4e.com/).

[1]: https://www.py4e.com/html3/02-variables "Python 4 Everybody: Variables"
[2]: https://www.python.org/dev/peps/pep-0008/ "PEP 8"
