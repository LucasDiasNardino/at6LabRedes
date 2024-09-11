import socket
import os

def tcp_client(host='127.0.0.1', port=65433, file_path='tcpText.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(file_path, 'rb') as f:
            file_size = os.path.getsize(file_path)  # Obtém o tamanho do arquivo
            print(f"Enviando arquivo '{file_path}' de tamanho {file_size} bytes...")
            total_bytes_sent = 0  # Variável para rastrear o total de bytes enviados
            
            while True:
                data = f.read(1024)  # Lê o arquivo em chunks de 1024 bytes
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
tcp_client()
