# Variable in Python: short recap

Inspired by Real Python, [Variables in Python: Usage and Best Practice](https://realpython.com/python-variables/)

## How to name it

Some best practice around variable naming is:

- give a descriptive name (e.g. temperature instead of t)

- variables should be nouns

- single letter are hard to decipher. 

- use leading underscore for non-public variable (e.g. _timeout).

  

The most common practice for multi-word are;

- **Camel case**: numberOfWords
- **Snake case**: number_of_words
- **Pascal case**: NumberOfWords (first word is also captalized)

You can check in the [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) for more info.



## Python in object-oriented programming



```python
In [1]: 2000
Out[1]: 2000

In [2]: type(2000)
Out[2]: int

In [3]: id(2000)
Out[3]: 139984729727632

In [4]: n = 2000

In [5]: id(n)
Out[5]: 139984729731824

In [6]: m = n

In [7]: m
Out[7]: 2000

In [8]: id(m)
Out[8]: 139984729731824
```



## Data Storage Variable

```python
In [1]: >>> contacts = [
   ...: ...     ("Jonas", "2024-10-11", "jonas@example.com"),
   ...: ...     ("Arn", "1978-10-1", "arn@example.com"),
   ...: ...     ("Lara", "2010-11-12", "lara@example.com"),
   ...: ...     ("Joao", "2015-13-1", "joao@example.com"),
   ...: ... ]

In [2]: for name, birthday, email in contacts:
   ...:     print(name, email)
   ...:
Jonas jonas@example.com
Arn arn@example.com
Lara lara@example.com
Joao joao@example.com
```



### Type Hint 

```python
In [1]: contacts: tuple[str,str,str] = [
   ...:    ("Jonas", "2024-10-11", "jonas@example.com"),
   ...:    ("Arn", "1978-10-1", "arn@example.com"),
   ...:    ("Lara", "2010-11-12", "lara@example.com"),
   ...:    ("Joao", "2015-13-1", "joao@example.com"),
   ...:
   ...:
   ...:    ]

In [2]: for name, birthday, email in contacts:
   ...:     print(name, email)
   ...:
Jonas jonas@example.com
Arn arn@example.com
Lara lara@example.com
Joao joao@example.com

In [3]: contacts.append(("mano", "2012-10-1","mano@example.com"))

In [4]: for name, birthday, email in contacts:
   ...:     print(name, email)
   ...:
Jonas jonas@example.com
Arn arn@example.com
Lara lara@example.com
Joao joao@example.com
mano mano@example.com
```





## Global, Local and Non-Local Variables

Global variable: created at module level.

Local variable: created inside your function. Once the function returns the variable disappear.

Non-local variable: created in a function that define inner functions. The variable local to the outer function are non-local to the inner function. Usefull when creating [closure](https://realpython.com/python-closure/) functions or [decorators](https://realpython.com/primer-on-python-decorators/).

```python
In [1]: # Global scope
   ...: global_variable = "global"
   ...:
   ...: def outer_func():
   ...:     # Nonlocal scope
   ...:     nonlocal_variable = "nonlocal"
   ...:     def inner_func():
   ...:         # Local scope
   ...:         local_variable = "local"
   ...:         print(f"Hi from the '{local_variable}' scope!")
   ...:         print(f"Hi from the '{nonlocal_variable}' scope!")
   ...:         print(f"Hi from the '{global_variable}' scope!")
   ...:     inner_func()
   ...:

In [2]: print(outer_func())
Hi from the 'local' scope!
Hi from the 'nonlocal' scope!
Hi from the 'global' scope!
```



## Variables in Class

Class attributes are variables created at class level. (e.g. count in example below)

Instance attributes are variables you attach to instances of a given class (e.g. name, position, email).

```python
#employees.py
class Employee:
    count = 0

    def __init__(self, name, position, email:
        self.name = name
        self.position = position
        self.email = email
        Employee.count += 1

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.email}")
```



```python
In [1]: from employees import Employee

In [2]: mano = Employee("Mano bra", "Developer", "mano@example.com")

In [3]: mano.display_profile()
Name: Mano bra
Position: Developer
Salary: $mano@example.com

In [4]: f"Total employees are: {Employee.count}"
Out[4]: 'Total employees are: 1'
```

