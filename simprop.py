def test():
	return "Hello World"
    
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy import sqrt

def sim(expression):
    """A Simple function to calculate an error propagation of absolute error

    expression:     is the Formula given without an equals (=) sign and as a string.
    return:         It will return the Errorpropagation as an Absolute Error as a Sympy expression 
    
    """
    expr = parse_expr(expression)
    vars = list(expr.free_symbols)
    prop = 0
    for i in vars:
        d = sp.symbols("d_"+ i.name)
        partial = sp.diff(expr,i)*d
        prop = prop + partial**2    
    return sp.sqrt(prop)