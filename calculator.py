import enum
import random

class Operation(enum.Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

    def values():
        return [op.value for op in Operation]
    
class Calculator:
    def __init__(self):
        self.expression = None  # remove any spaces
        self.operand1 = None
        self.operand2 = None
        self.operator = None

    def parse_expression(self, expression: str):
        if not expression:
            raise Exception("Expected a string")

        self.expression = expression.replace(" ", "")  # remove any spaces

        for op in Operation.values():
            if op not in self.expression:
                continue

            parts = self.expression.split(op)
            if len(parts) != 2:
                break

            self.operand1 = float(parts[0])
            self.operand2 = float(parts[1])
            self.operator = op
            return
                
        raise ValueError("Invalid expression. Must contain two operands and one operator.")

    def compute(self):
        match self.operator:
            case Operation.ADD:
                return self.operand1 + self.operand2
            case Operation.SUBTRACT:
                return self.operand1 - self.operand2
            case Operation.MULTIPLY:
                return self.operand1 * self.operand2
            case Operation.DIVIDE:
                return self.operand1 / self.operand2
            case _:
                raise ValueError("Unsupported operator.")
        
    
def encode_expression(operand1, operation, operand2):
    return f"{operand1} {operation} {operand2}"


def get_random_operation():
    return random.choice(list(Operation))