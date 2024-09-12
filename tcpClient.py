import socket
import os
import sys

def tcp_client(fileSize,buffer_size, host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        if fileSize == 1500:
            file_path = 'arquivo1500.txt'

        elif fileSize == 15000:
            file_path = 'arquivo15000.txt'

        with open(file_path, 'rb') as f:
            file_size = os.path.getsize(file_path)  # Obtém o tamanho do arquivo
            print(f"Enviando arquivo '{file_path}' de tamanho {file_size} bytes...")
            total_bytes_sent = 0  # Variável para rastrear o total de bytes enviados
            
            while True:
                data = f.read(buffer_size)  # Lê o arquivo em chunks de 1024 bytes
                if not data:
                    break
                
                s.sendall(data)
                
                # Calcula e exibe o tamanho dos dados enviados
                bytes_sent = len(data)
                total_bytes_sent += bytes_sent
                print(f"[DEBUG] Chunk de {bytes_sent} bytes enviado")
            
            # Exibe o tamanho total do arquivo enviado
            print(f"Arquivo enviado com sucesso. Total de {total_bytes_sent} bytes enviados.")

# Executa o cliente TCP
if (len(sys.argv) > 2):
    fileSize = int(sys.argv[1])
    buffer_size = int(sys.argv[2])
    tcp_client(fileSize,buffer_size)

elif (len(sys.argv) > 1):
    print("Defina o tamanho do arquivo e o tamanho do buffer:\n python3 tcpClient.py <fileSize> <buffer_size>")
    sys.exit(1)