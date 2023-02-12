import selectors
import socket


def main() -> None:
    selector = selectors.DefaultSelector()

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()

    selector.register(server_socket, selectors.EVENT_READ)

    while True:
        events = selector.select(timeout=1)

        if len(events) == 0:
            print("No events, waiting a bit more!")

        for event, _ in events:
            event_socket = event.fileobj
            assert isinstance(event_socket, socket.socket)

            if event_socket == server_socket:
                connection, client_address = server_socket.accept()
                connection.setblocking(False)
                print(f"I got a connection from {client_address}!")
                selector.register(connection, selectors.EVENT_READ)
            else:
                data = event_socket.recv(1024)
                if data:
                    print(f"I got some data: {data!r}")
                    event_socket.send(data)
                else:
                    print(f"Disconnecting {event_socket.getpeername()}")
                    selector.unregister(event_socket)


if __name__ == "__main__":
    main()
