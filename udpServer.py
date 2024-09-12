import socket
import os
import sys

def udp_server(buffer_size, host='127.0.0.1', port=65432):
    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Servidor UDP ouvindo em {host}:{port}...")

        print("\nAguardando dados...")
        # Abre o arquivo para escrita em modo binário
        with open('recebido_udp.txt', 'wb') as f:
            file_size = 0  # Variável para armazenar o tamanho do arquivo em bits
            while True:
                
                data, addr = s.recvfrom(buffer_size)  # Recebe até 1024 bytes de dados

                # Verifica se dados foram recebidos
                if data == b'EOF':
                    print("EOF Recebido - Fim da transmissão.")
                    print(f"\nArquivo recebido com sucesso.\nTamanho total: {file_size} bytes.")
                    break
                elif data:
                    print(f"[RCV] {len(data)} bytes de {addr}.")
                    f.write(data)  # Escreve os dados recebidos no arquivo
                    f.flush()  # Garante que os dados sejam escritos imediatamente no disco
                    file_size += len(data)  # Atualiza o tamanho do arquivo em bits
                    print(f"Tamanho do arquivo: {file_size} bytes")
                else:
                    print("Nenhum dado recebido. Verifique o cliente.")
                    break

        print("Arquivo recebido com sucesso.")

# Executa o servidor UDP
if (len(sys.argv) > 1):
    buffer_size = int(sys.argv[1])
    udp_server(buffer_size)

else:
    print("Defina o tamanho do buffer: python3 udpServer.py <buffer_size>")
    sys.exit(1)