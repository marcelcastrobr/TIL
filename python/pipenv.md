# PIPENV 



**[Pipenv](https://pypi.org/project/pipenv/)** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

After working with conda I decided to give a try to [pipenv](https://pypi.org/project/pipenv/). Thanks to [alexeygrigorev](https://github.com/alexeygrigorev) which introduce it very well in this [video](https://www.youtube.com/watch?v=BMXh8JGROHM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR). 



## Installation

```bash
#Installation
$ sudo apt install pipenv

# Or using pip
$ pip3 install pipenv

```

For other operating system, check [here](https://pypi.org/project/pipenv/).

Pipenv creates two files: **Pipfile** and **Pipfile.lock**



## Useful commands:

```bash
#Activate pipenv
$ pipenv shell

# Install a package
$pipenv install requests

# Install from requirements
$ pipenv install -r ./requirements.txt

# Check security vulnerabilities
$ pipenv check

# Exiting environment
$ exit

# Run with pipenv
$ pipenv run <your code>

# Check installed dependency
$ pipenv graph

# Locate your project
$ pipenv --where

# Locate your virtualenv
$ pipenv --venv

# Locate your python interpreter
$ pipenv --py

# Generate a lock file
$ pipenv lock

# Create a new project using Python 3.9
$ pipenv --python 3.9

```

