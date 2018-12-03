''' Handler for IO requests. '''

__all__ = [
			'set_io',
			'cin',
			'cout',
		  ]

''' For type hints. '''
from types import FunctionType

in_buffer = None

in_method = None
out_method = None

def set_io(io_stream: FunctionType, path: str, method: str):
	''' Initialize the method of IO '''
	if method == 'r':

		global in_buffer, in_method

		in_buffer = None
		in_method = (io_stream, path, method)

	elif method in ['w', 'a']:

		''' Override the current file if nessesary. '''
		with open(path, method) as f:
			pass

		global out_method

		out_method = (io_stream, path, 'w')

def cin() -> str:
	''' Request io_stream to read line. '''
	global in_buffer, in_method

	io_stream, path, method = in_method
	out, in_buffer = io_stream(path, method, buffer = in_buffer)
	return out

def cout(value: str):
	''' Request io_stream to write line. '''
	global out_method

	io_stream, path, method = out_method
	io_stream(path, method, value = value)