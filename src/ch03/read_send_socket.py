import socket


def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.bind(server_address)
    server_socket.listen()

    try:
        connection, client_address = server_socket.accept()
        print(f"I got a connection from {client_address}")

        buffer = b""

        while buffer[-2:] != b"\r\n":
            data = connection.recv(2)
            if not data:
                break
            else:
                print(f"I got data: {data!r}")
                buffer += data
        print(f"all the data is: {buffer!r}")
        connection.sendall(buffer)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
