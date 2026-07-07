# The Python compile() function takes source code as input and returns a code object, which can later be executed by the exec() function.

code_str = 'x=5\ny=10\nprint("sum =",x+y)'    
code = compile(code_str, 'sum.py', 'exec')    
print(type(code))    
exec(code)    
exec(x)    