import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
massage = None
while True and massage != "quit":
    massage = input("Введіть два числа: ")
    sock.send(bytes(massage, encoding='UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    print("Повідомлення від сервера: " + data)
sock.close()
