import socket

def create_tcp_socket():
    # Create a TCP socket
    try:
        # AF_INET specifies the address family (IPv4), and SOCK_STREAM specifies the socket type (TCP)
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return tcp_socket
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None

def connect_to_google(tcp_socket):
    # Google's IP address and port for HTTP (non-secure)
    target_host = 'www.google.com'
    target_port = 80

    # Connect to Google
    try:
        tcp_socket.connect((target_host, target_port))
        print(f"Connected to {target_host}:{target_port}")
    except socket.error as e:
        print(f"Error connecting to {target_host}:{target_port}: {e}")
        tcp_socket.close()

def main():
    # Create a TCP socket
    tcp_socket = create_tcp_socket()

    if tcp_socket:
        # Connect to Google
        connect_to_google(tcp_socket)

        # Close the socket
        tcp_socket.close()

if __name__ == "__main__":
    main()
