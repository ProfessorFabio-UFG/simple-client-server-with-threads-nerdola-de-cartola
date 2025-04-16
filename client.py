from socket  import *
from constCS import *
from calculator import encode_expression, Operation, get_random_operation
import random

def make_request(s):
    operand1 = random.uniform(0.0, 9.9)
    operation = get_random_operation().value
    operand2 = random.uniform(0.0, 9.9)
    req = encode_expression(operand1, operation, operand2)
    s.send(req.encode())
    res = float(s.recv(1024).decode())
    print(f"{req} = {res}")

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
make_request(s)       
make_request(s)       
make_request(s)       
s.close()               
