import socket
import sys

def tcp_client(host='127.0.0.1', port=65432, file_path='tcpText.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(file_path, 'rb') as f:
            print(f"Enviando arquivo '{file_path}'...")
            for data in f:
                s.sendall(data)
        print("Arquivo enviado com sucesso.")

# Executa o cliente TCP
tcp_client()
