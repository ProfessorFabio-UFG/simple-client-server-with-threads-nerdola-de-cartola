from socket  import *
from constCS import *
from calculator import Calculator

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT)) 
s.listen(1)           
calc = Calculator()
(conn, addr) = s.accept() 

while True:                
  data = conn.recv(1024)  
  if not data: break
  
  req = data.decode()
  calc.parse_expression(req)
  res = str(calc.compute())
  conn.send(res.encode())

conn.close()               
