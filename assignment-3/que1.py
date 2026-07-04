def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def calculate(op1, op2, operation):
    return operation(op1, op2)

print(calculate(10, 5, add))
print(calculate(10, 5, sub))
print(calculate(10, 5, mul))
print(calculate(10, 5, div))
