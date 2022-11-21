import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(5)
print('Сервер запущено, натисніть CTRL+C для зупинки')

while True:
    conn, addr = sock.accept()
    print('Підключено: ', addr)
    data = conn.recv(1024)
    print('Отримано повідомлення: ', data.decode('utf-8'))
    conn.send(bytes(str(data.decode('utf-8').upper()), encoding='UTF-8'))
conn.close()
