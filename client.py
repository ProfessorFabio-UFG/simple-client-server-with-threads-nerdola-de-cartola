from socket import *
from constCS import *
from calculator import encode_expression, get_random_operation
import random
from threading import Thread


class Client:
    def __init__(self):
        self.responses_buffer = ""
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((HOST, PORT)) 
        self.s.setblocking(False)
        self.requests = []

    def make_random_request(self, req_id):
        operand1 = random.uniform(0.0, 9.9)
        operation = get_random_operation().value
        operand2 = random.uniform(0.001, 9.9)
        self.make_request(operand1, operation, operand2, req_id)

    def make_request(self, operand1, operation, operand2, req_id):
        expression = encode_expression(operand1, operation, operand2)
        req = f"|{req_id},{expression}|"
        self.s.send(req.encode())
        self.requests.append((req_id, expression))

    def process(self):
        for i in range(NUMBER_OF_REQUESTS):
            self.make_random_request(i)

    def process_threads(self):
        threads = []

        for i in range(NUMBER_OF_REQUESTS):
            thread = Thread(target=Client.make_random_request, args=(self,i))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join() 

    
    def read_responses(self):
        buffer = ""
        while True:
            try:
                buffer += self.s.recv(1024).decode()
                if len(buffer.split("|")) == NUMBER_OF_REQUESTS*3 + 1:
                    break
            except Exception as e:
                #print(e)
                continue

        responses = buffer.split("|")

        for response in responses:
            if response == "":
                continue

            response = response.split(',')
            id = int(response[0])
            result = float(response[1])

            for req in self.requests:
                req_id = req[0]
                expression = req[1]
                if req_id != id:
                    continue

                a = eval(expression)
                message = "correta" if a == result else "incorreta"
                print(f"{expression} = {result:.3f} | Operação {message}")


def main():
    client = Client()

    if THREADS:
        client.process_threads()
    else:
        client.process()

    client.read_responses()
    client.s.send("@".encode())
    client.s.close()    

main()