import socket
import os
import sys

def tcp_server(buffer_size, host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor TCP ouvindo em {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Conexão estabelecida com {addr}")
            total_bytes_received = 0  # Variável para rastrear o total de bytes recebidos


            with open('recebido_tcp.txt', 'wb') as f:
                while True:
                    data = conn.recv(buffer_size)
                    if not data:
                        break
                    
                    # Calcula e exibe o tamanho dos dados recebidos
                    bytes_received = len(data)
                    total_bytes_received += bytes_received
                    print(f"[DEBUG] Chunk de {bytes_received} bytes recebido")

                    f.write(data)
            
            # Exibe o tamanho total do arquivo recebido
            print(f"Arquivo recebido com sucesso. Tamanho total do arquivo: {total_bytes_received} bytes.")

# Executa o servidor TCP
if (len(sys.argv) > 1):
    buffer_size = int(sys.argv[1])
    tcp_server(buffer_size)

else:
    print("Defina o tamanho do buffer: python3 tcpServer.py <buffer_size>")
    sys.exit(1)