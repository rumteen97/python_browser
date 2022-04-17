import socket
from tkinter import *

browser=Tk()
browser.title('Browser')

label=Label(browser, text= 'Enter URL')
entry=Entry()


def request():
    addr = entry.get()
    addr_1=(addr,80)
    msg= 'GET / HTTP/1.1\r\n'
    msg+= 'Host: ' + addr + ':80\r\n'
    msg+= 'Accept-Language: en-us\r\n'
    msg+= 'Accept-Charset: ISO-8859-1,utf-8\r\n'
    msg+= 'Keep-Alive: 115\r\n'
    msg+= 'Connection: Keep-Alive\r\n'
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
    data= data.decode()
    result.insert(INSERT,data)
    # print(data)

button=Button(browser, text= 'Go', command=request)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
result=Text(browser)
result.pack(side=TOP)

browser.mainloop()