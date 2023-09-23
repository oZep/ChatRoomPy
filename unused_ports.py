import socket

def find_unused_ports(start_port, end_port):
    unused_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        if result != 0:
            unused_ports.append(port)
        sock.close()
    return unused_ports

start_port = 1
end_port = 65535

unused_ports = find_unused_ports(start_port, end_port)

print(f"The following ports are currently unused: {unused_ports}")
