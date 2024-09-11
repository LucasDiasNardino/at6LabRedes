import socket
import sys

def tcp_server(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor TCP ouvindo em {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Conexão estabelecida com {addr}")
            with open('recebido_tcp.txt', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print("Arquivo recebido com sucesso.")

# Executa o servidor TCP
tcp_server()
