import socket

def udp_client(file_path, host='127.0.0.1', port=65432):
    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Lê o arquivo em modo binário
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break  # Sai do loop quando não há mais dados a enviar
                s.sendto(data, (host, port))
        
        # Envia um indicador de fim de transmissão
        s.sendto(b'EOF', (host, port))

# Executa o cliente UDP
udp_client('udpText.txt')
