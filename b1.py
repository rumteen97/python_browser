import socket



addr = input('Enter URL: ')
addr_1=(addr,80)
msg= 'GET / HTTP/1.1\r\n'
msg+= 'Host: ' + addr + ':80\r\n'
msg+= 'Accept-Language: en-us\r\n'
msg+= 'Accept-Charset: ISO-8859-1,utf-8\r\n'
# msg+= 'Keep-Alive: 97\r\n'
msg+= 'Connection: close\r\n'
msg+= '\r\n'
B_msg= str.encode(msg)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addr_1)
sock.sendall(B_msg)

data= b''
while True:
    buf = sock.recv(1024)
    if not buf:
          break
    data += buf

sock.close()
print(data.decode())