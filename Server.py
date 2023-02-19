import socket


# Function to reverse the message received from the client
def reverse_message(data):
    return data[::-1]


# Function to run the server and receive message from client
def run_server():
    port = 6000
    # Creating a TCP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding the server socket to the specified port
    server_socket.bind(('', port))
    # Listening for incoming connections
    server_socket.listen(1)

    while True:
        # Accepting a connection from the client
        client_socket, client_address = server_socket.accept()

        # Receiving data from the client
        data = client_socket.recv(1024).decode()
        # Checking if the received message is "end"
        if data == "end":
            client_socket.send("dne".encode())
            break
        else:
            # Sending the reversed message to the client
            client_socket.send(reverse_message(data).encode())

    # Closing the server socket
    server_socket.close()


if __name__ == "__main__":
    run_server()
