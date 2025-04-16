from socket  import *
from constCS import *
from calculator import encode_expression, Operation, get_random_operation
import random

def make_random_request(s):
    operand1 = random.uniform(0.0, 9.9)
    operation = get_random_operation().value
    operand2 = random.uniform(0.0, 9.9)
    make_request(s, operand1, operation, operand2)

def make_request(s, operand1, operation, operand2):
    req = encode_expression(operand1, operation, operand2)
    s.send(req.encode())
    res = s.recv(1024).decode()
    print(f"{req[:5]} = {res[:5]}")

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
make_random_request(s)       
make_random_request(s)       
make_random_request(s)       
make_request(s, 10.0, '/', 0.0)       
s.close()               
