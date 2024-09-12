import socket
import os

def udp_server(host='127.0.0.1', port=65432):
    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Servidor UDP ouvindo em {host}:{port}...")

        # Abre o arquivo para escrita em modo binário
        with open('recebido_udp.txt', 'wb') as f:
            file_size = 0  # Variável para armazenar o tamanho do arquivo em bits
            while True:
                print("Aguardando dados...")
                data, addr = s.recvfrom(1024)  # Recebe até 1024 bytes de dados

                # Verifica se dados foram recebidos
                if data == b'EOF':
                    print("Fim da transmissão recebido.")
                    break
                elif data:
                    print(f"Recebido {len(data)} bytes de {addr}.")
                    f.write(data)  # Escreve os dados recebidos no arquivo
                    f.flush()  # Garante que os dados sejam escritos imediatamente no disco
                    file_size += len(data) * 8  # Atualiza o tamanho do arquivo em bits
                    print(f"Tamanho do arquivo: {file_size} bits")
                else:
                    print("Nenhum dado recebido. Verifique o cliente.")
                    break

        print("Arquivo recebido com sucesso.")

# Executa o servidor UDP
udp_server()
