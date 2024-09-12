import socket
import sys

def udp_client(file_size,buffer_size, host='127.0.0.1', port=65432):
    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Read the file in binary mode

        if file_size == 1500:
            file_path = 'arquivo1500.txt'

        elif file_size == 15000:
            file_path = 'arquivo15000.txt'

        print(f"Conectando ao servidor: {host}:{port}")
        print(f"Enviando arquivo '{file_path}' de tamanho {file_size} bytes...")
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(buffer_size)
                if not data:
                    break  # Exit the loop when there is no more data to send
                
                #prints the si
                print(f"[SND] Chunk de {len(data)} bytes enviado")
                s.sendto(data, (host, port))
        
        # Send an end-of-transmission indicator
        print('Encerrando Conexão - EOF enviado')  # Debugging print
        s.sendto(b'EOF', (host, port))

# Run the UDP client
if (len(sys.argv) > 2):
    file_size = int(sys.argv[1])
    buffer_size = int(sys.argv[2])
    udp_client(file_size,buffer_size)

elif (len(sys.argv) > 1):
    print("Defina o tamanho do arquivo e o tamanho do buffer:\n python3 udpClient.py <file_size> <buffer_size>")
    sys.exit(1)