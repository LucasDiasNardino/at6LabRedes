import socket

def udp_client(host='127.0.0.1', port=65433, file_path='udpText.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        with open(file_path, 'rb') as f:
            print(f"Enviando arquivo '{file_path}' para {host}:{port}...")
            for data in f:
                s.sendto(data, (host, port))
                print(f"Enviado {len(data)} bytes.")
        print("Arquivo enviado com sucesso.")

# Executa o cliente UDP
udp_client()
