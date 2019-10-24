# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

# JA: You should move the main function to the calculator.py file

def process(eq, op):
    if op == '/':
        print("here",eq)
        index = eq.index('/')
        op1 = float(eq[index - 1])
        op2 = float(eq[index + 1])
        result = op1 / op2
        del(eq[index - 1:index + 2])
        eq.insert(index-1, result)
    elif op == '*':
        index = eq.index('*')
        op1 = float(eq[index - 1])
        op2 = float(eq[index + 1])
        result = op1 * op2
        del(eq[index - 1:index + 2])
        eq.insert(index-1, result)
    elif op == '+':
        index = eq.index('+')
        op1 = float(eq[index - 1])
        op2 = float(eq[index + 1])
        result = op1 + op2
        del(eq[index - 1:index + 2])
        eq.insert(index - 1, result)
    elif op == '-':
        index = eq.index('-')
        op1 = float(eq[index - 1])
        op2 = float(eq[index + 1])
        result = op1 - op2
        del(eq[index - 1:index + 2])
        eq.insert(index-1, result)
    else:
        print("Invalid operation")

def solve(eqStr):
    eq = eqStr.split()
    while len(eq) > 1:
        if '/' in eq:
            process(eq, '/')
        elif '*' in eq:
            process(eq, '*')
        elif '+' in eq:
            process(eq, '+')
        elif '-' in eq:
            process(eq, '-')
    return eq[0]

