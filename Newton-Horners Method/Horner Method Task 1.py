import numpy as np
"""
Task  1: Finding the real root of a polynominal using Newton-Horners Method

This polynomial was evaluated using "Synthetic division Method of Horners Scheme"
"""


print("****************************START***************************")
poly = [1, -7, 6, 5]  # Polynominal
task = np.poly1d(poly)
error = 10e-6

print("The inputed Polynomial is: ", task)
print("*************************************************************")


def p(x):  # f(x) = an*x ^ n + an-1x ^ n-a ... a0, evaluation of polynominal with numpy
    return abs(np.polyval(poly, x))  # USing numpy to evaluate the polynomials


def pd(x):  # returns f'(x)=g(x)=bn-1*x^n-1...b0
    n = np.polyder(poly)
    return abs(np.polyval(n, x))


def netwon():  # Newton method for outter loop
    yi = xi - p(xi)/pd(xi)

    print("Guess Value from Newton method is: ", yi)
    return yi


def newton_horner(poly, x):  # Horner Method for the inner loop
    """
    This polynomial was evaluated using "Synthetic division Method of Horners Scheme" we take a polynomial keep track of the coeffiecent
    """
    n = len(poly)
    bn = poly[0]
    c3 = bn
    print("value for ( b 0 ) ", poly[0])
    # print(c3)
    for i in range(1, n):
        b = x * bn
        bn = poly[i] + b

        c = poly[1] + x
        cn = bn + x * c

        print("value for ( b", i, ")", bn)
    print("value for ( c", i, ")", cn)
    #print("value for cn: ", cn)
    # print("***************************************")
    i = 1
    sum = []
    while i < 1+n:
        y = x - bn/cn
        x = y
        sum.append(y)
        i += 1
    print(sum)

    print("The real root value from Newton-Horners Method is: ", y)
    print("******************************END**************************************")


# def Newton_Honers(bo, co):
#     x2 = xi - bo(x)/co(y)
#     return x2


xi = 2  # Guess value for Netwon
yi = netwon()
x = newton_horner(poly, yi)
