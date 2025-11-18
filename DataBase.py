import hashlib

def save_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with open("Users_db.txt", "a") as file:
        file.write(f"{username},{password_hash}\n")

    print(f"User '{username}' added!")

def check_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open("Users_db.txt", "r") as file:
            for line in file:
                stored_username, stored_hash = line.strip().split(",")
                if stored_username == username and stored_hash == password_hash:
                    return True
    except FileNotFoundError:
        print("User database not found.")
        return False
    return False
