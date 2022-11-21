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
    if data.decode('utf-8') == "Вітаю!":
        data = "Доброго дня!"
        conn.send(bytes(data, encoding='UTF-8'))
    if data.decode('utf-8') == "До побачення!":
        data = "До зустрічі!"
        conn.send(bytes(data, encoding='UTF-8'))
    else:
        conn.send(data)
conn.close()
