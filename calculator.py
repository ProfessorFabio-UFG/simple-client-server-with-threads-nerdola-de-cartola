import enum
import random
from constCS import *

class Operation(enum.Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

    def values():
        return [op.value for op in Operation]
    
class Calculator:
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2

    def compute(self):
        match self.operator:
            case Operation.ADD.value:
                return self.operand1 + self.operand2
            case Operation.SUBTRACT.value:
                return self.operand1 - self.operand2
            case Operation.MULTIPLY.value:
                return self.operand1 * self.operand2
            case Operation.DIVIDE.value:
                if self.operand2 == 0:
                    return 'Nan'
                return self.operand1 / self.operand2
            case _:
                raise ValueError("Unsupported operator.")
        
    
def encode_expression(operand1, operation, operand2):
    return f"{operand1:.4f} {operation} {operand2:.4f}"

def parse_expression(expression: str):
    if not expression:
        raise Exception("Expected a string")

    expression = expression.replace(" ", "")  # remove any spaces

    for op in Operation.values():
        if op not in expression:
            continue

        parts = expression.split(op)
        if len(parts) != 2:
            break

        operand1 = float(parts[0])
        operand2 = float(parts[1])
        operator = op
        return Calculator(operand1, operator, operand2)
            
    print(f"{RED} error exp: {expression} {RESET}")
    raise ValueError("Invalid expression. Must contain two operands and one operator.")

def get_random_operation():
    return random.choice(list(Operation))