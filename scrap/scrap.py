import ast
import astor

expr="""
def foo():
   print("hello world")
"""
p=ast.parse(expr)
print p
print ast.get_docstring(p)
print p._fields
print p.body
print p.body[0]
print ast.get_docstring(p.body[0])

p.body[0].body = [ ast.parse("return 42").body[0] ] # Replace function body with "return 42"

print(astor.to_source(p))
