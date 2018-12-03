# Oven
An util package that includes algorithms, functions and IO similar to that of other languages' standard library.

## Installation
* Installation with pip is recommended.
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

## Standard I/O
The [stdio](/stdio) package includes convient functions to redefine basic I/O.

### Creating Session
Import [stdio](/stdio) as such:
```python
from oven.stdio import *
```

The [stdio](/stdio) session is required in order to call any I/O functions. A session is created as such:
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

Note that the [stdio]() session is created on the global scope, therefore one session will always suffice.

### Calling cin/cout
Despite the name, the cin/cout also applies to file IO.
```python
cin() # Read one line.
cout('Hello World') # Write. Note that \n is not added at the end.
```

## Pointer
The [pointer](/pointer) package includes a pointer object.

### Instantiating Pointers
A [pointer](/pointer) is created as such:
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