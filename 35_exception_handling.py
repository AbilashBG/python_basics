
# Syntax:

#    try:
#               # code that might raise an exception
#    except ExceptionType1:
#               # code to handle ExceptionType1
#    except ExceptionType2:
#               # code to handle ExceptionType2
#    except:
#               # code to handle any other exception
#    else:
#               # code to run if no exception was raised
#    finally:
#               # code that will always be executed, regardless of whether an exception was raised or not



# try block in Python

try:
    a = 10 / 0
except Exception as e:
    print(e)

# output

# division by zero
    
# <---------------------------------------------------->    
 
# Try Else
    
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)

# output

# A Value :  0.4
    
# <---------------------------------------------------->    
 
# Try else finally
    
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
finally:
    print("Thank You")

# output

# division by zero
# Thank You
    
# <---------------------------------------------------->    
 
# Type of Exceptions in Python

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# output

# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeErr
# or', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
# 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'Excep
# tionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
# 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'Keyboard
# Interrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'N
# otImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'Recursio
# nError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxEr
# ror', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'Unico
# deDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'W
# arning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__',
#  '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', '
# callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
# 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
# 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next
# ', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', '
# slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# 158
    
# <---------------------------------------------------->    