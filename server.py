import socket
import threading
import DataBase

def handle_client(client_socket):
    try:
        # Ask client
        choice = client_socket.recv(1024).decode()

        # Prompt for username
        client_socket.send("Enter username: ".encode())
        username = client_socket.recv(1024).decode()

        # Prompt for password
        client_socket.send("Enter password: ".encode())
        password = client_socket.recv(1024).decode()

        if choice == "1":  # Register
            if DataBase.check_user(username, password):
                client_socket.send("Username already exists!".encode())
            else:
                DataBase.save_user(username, password)
                client_socket.send("Registration successful!".encode())
        elif choice == "2":  # Login
            if DataBase.check_user(username, password):
                client_socket.send("Login successful!".encode())
            else:
                client_socket.send("Invalid username or password!".encode())
        else:
            client_socket.send("Invalid choice!".encode())
    except Exception as e:
        client_socket.send(f"Error: {str(e)}".encode())
    finally:
        client_socket.close()
        
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(5)
    print("Server listening on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Run the server
if __name__ == "__main__":
    start_server()
