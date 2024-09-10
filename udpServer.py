import socket

def udp_server(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Servidor UDP ouvindo em {host}:{port}...")
        with open('recebido_udp.txt', 'wb') as f:
            while True:
                data, addr = s.recvfrom(1024)
                if not data:
                    break
                f.write(data)
            print("Arquivo recebido com sucesso.")

# Executa o servidor UDP
udp_server()
