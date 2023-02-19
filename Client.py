
import socket


# Function to run the client and send messages to the server
def run_client():
    name = socket.gethostname()
    port = 6000
    # Creating a TCP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecting to the server at the specified IP and port
    client_socket.connect((name, port))

    while True:
        # Reading input message from the user
        message = input("Enter message (enter 'end' to terminate): ")
        # Sending the message to the server
        client_socket.send(message.encode())

        # Receiving the response from the server
        response = client_socket.recv(1024).decode()
        # Checking if the received message is "dne"
        if response == "dne":
            print(response)
            break
        else:
            # Printing the received message
            print("Received response:", response)

    # Closing the client socket
    print("Closing client socket")
    client_socket.close()


if __name__ == "__main__":
    run_client()
