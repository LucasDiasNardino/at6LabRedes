import socket

def udp_client(file_path, host='127.0.0.1', port=65432):
    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Read the file in binary mode
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break  # Exit the loop when there is no more data to send
                
                #prints the si
                print(f"Sending {len(data)} bytes to {host}:{port}")
                s.sendto(data, (host, port))
        
        # Send an end-of-transmission indicator
        print('Sending end-of-transmission indicator')  # Debugging print
        s.sendto(b'EOF', (host, port))

# Execute the UDP client
udp_client('udpText.txt')
