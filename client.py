import socket

def interact_with_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    # Ask user
    choice = input("Do you want to [1] Register or [2] Login? ")
     # Check valid input
    if choice not in ["1", "2"]:
        print("Invalid choice! Exiting...")
        client.close()
        return  # Exit

    client.send(choice.encode())

    username_prompt = client.recv(1024).decode()
    print(username_prompt, end="")
    username = input()
    client.send(username.encode())

    password_prompt = client.recv(1024).decode()
    print(password_prompt, end="")
    password = input()
    client.send(password.encode())


    response = client.recv(1024).decode()
    print(response)
    client.close()

if __name__ == "__main__":
    interact_with_server()
