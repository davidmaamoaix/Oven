# Oven
A util package that includes algorithms, functions and IO similar to those of other languages' standard libraries.

## Installation
Installation with pip is recommended.
```sh
pip install oven
```

## Table of Contents

- [Standard I/O](#standard-io)
	- [Creating Session](#creating-session)
	- [Calling cin/cout](#calling-cincout)
- [Pointer](#pointer)
	- [Instantiating Pointers](#instantiating-pointers)
	- [Calling Pointers](#calling-pointers)
- [Structs](#structs)
	- [Stack](#stack)
	- [Queue](#queue)
	- [Tree](#tree)
	- [BinaryTree](#binarytree)

## Standard I/O
The [stdio](/oven/stdio) package includes convient functions to redefine basic I/O.

```python
from oven.stdio import *
```

### Creating Session

The [stdio](/oven/stdio) session is required in order to call any I/O functions. A session is created as such:
```python
set_io(IO_STREAM, 'path/to/file', METHOD)
```

The *IO_STREAM* can be any of:
* stdio.FILE: Redirect the IO stream to a file
* stdio.CONSOLE: Redirect the IO stream to the console

The *METHOD* can be any of:
* *r* : Read from a file
* *w* : Write to a file, create/override if nessesary
* *a* : Append to a file, create if nessesary

Method *w* overrides the file and dump all output from the session, while *a* append all output from the session to the end of the file.

If the *IO_STREAM* is set to *CONSOLE*, then the *path* argument will be ignored.

Note that the [stdio]() session is created on the global scope, therefore one session will always suffice for one method of IO action.

An example is given below. This code reads a line of input from a file and print it to the screen.
```python
from oven.stdio import *

set_io(FILE, 'text.in', 'r')
set_io(CONSOLE, None, 'w')

text = cin()
cout(text)
```

### Calling cin/cout
Despite the name, the cin/cout also applies to file IO.
```python
cin() # Read one line.
cout('Hello World') # Write. Note that \n is not added at the end.
```

## Pointer
The [Pointer](/oven/pointer) package includes a pointer object.

```python
from oven.pointer import Pointer
```

### Instantiating Pointers
A [Pointer](/oven/pointer) is created as such:
```python
ptr_1 = Pointer()
ptr_2 = Pointer(INIT_VALUE)
```

### Calling Pointers
Getting value from pointer:
```python
value = ptr()
```

Assigning value to pointer:
```python
ptr(value)
```

## Structs
The [structs](/oven/structs) package features some data structures.

```python
from oven.structs import *
```

### Stack
```python
from oven.structs import Stack
```

The [Stack](/oven/structs/stack.py) class is a subclass of python's list, its methods are:
* *push* : Push a value to the stack
* *pop* : Remove and return the ending element of the stack

### Queue
```python
from oven.structs import Queue
```

The [Queue](/oven/structs/queue.py) class is a subclass of python's list, its methods are:
* *push* : Push a value to the queue
* *pop* : Remove and return the starting element of the queue

### Tree
```python
from oven.structs import Tree
```

The [Tree](/oven/structs/tree.py) class is a recursive node of a tree. The value of the node can be assigned either in the constructor or by calling the *value* attribute (variable).
```python
# Both nodes are tree nodes with the value 42

node_1 = Tree(42)

node_2 = Tree()
node_2.value = 42
```

A child can be added to a node by calling the *addChild* method and passing the child as the parameter. The children of a node can be accessed by calling the *children* attribute (variable).

Other methods include:
* *dfs* : Returns a list of the tree's nodes in *depth first search* order.
* *bfs* : Returns a list of the tree's nodes in *breadth first search* order.

### BinaryTree
```python
from oven.structs import BinaryTree
```

The [BinaryTree](/oven/structs/binarytree.py) class is a subclass of the [Tree](/oven/structs/tree.py) class. The *left* and *right* children can be accessed by:
```python
node.left() # Returns the left node
node.right() # Returns the right node

node.left(newNode) # Sets the left node
node.right(newNode) # Sets the right node
```

Due to this, the *addChild* method is removed.

All other methods are identical to that of the [Tree](/oven/structs/tree.py) class except the *dfs* method, which is tweaked so that the calling of it becomes:
```python
node.dfs(MODE)
```

The *MODE* can be any of:
* *PREORDER*
* *INORDER*
* *POSTORDER*

All of the above modes are imported as such:
```python
from oven.structs import PREORDER, INORDER, POSTORDER
```
