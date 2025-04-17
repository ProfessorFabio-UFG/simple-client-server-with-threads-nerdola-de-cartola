from socket  import *
from constCS import *
from calculator import parse_expression
from threading import Thread
import time

class Server:
  def __init__(self):
    self.s = socket(AF_INET, SOCK_STREAM) 
    self.s.bind((HOST, PORT)) 
    self.s.listen(1)
    self.conn = None
    self.threads = []
    self.buffer = ""

  def parse_req(self, data):
    data = data.split(',')

    if len(data) != 2:
      print(f"{RED} error data: {data} {RESET}")
      raise Exception("Wrong data format, expected (id, expression)")

    return (data[0], data[1])

  def get_data(self):
      data = ""
      i = 0

      for char in self.buffer:
        i += 1
        if char == "|":
          break

        data += char

      self.buffer = self.buffer[i:]
      return data

  def run(self):
    (conn, addr) = self.s.accept()
    self.conn = conn

    while True:
      if "@" in self.buffer:
        break

      while self.buffer != "":
        data = self.get_data()
        self.handle_connection(data)

      self.buffer += self.conn.recv(1024).decode()

    for thread in self.threads:
      thread.join()

    self.conn.close()

  def handle_data(self, data):
    (req_id, expression) = self.parse_req(data)
    print(f"Request {req_id}, received: {expression}")

    time.sleep(1)
    calc = parse_expression(expression)
    res = f"{req_id},{calc.compute()}|"
    self.conn.send(res.encode())

  def handle_connection(self, data):
    if THREADS:
      thread = Thread(target=Server.handle_data, args=(self, data))
      thread.start()
      self.threads.append(thread)
    else:
      self.handle_data(data)

def main():
  server = Server()
  server.run()        

main()