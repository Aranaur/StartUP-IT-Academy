import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
string_data = input('Введіть Ваше повідомлення: ')
sock.send(bytes(string_data, encoding='utf-8'))
data = sock.recv(1024)
sock.close()
print(data.decode('utf-8'))
