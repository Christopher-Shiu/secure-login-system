# Secure Login System

A model of a client-server authentication system that provides secure user registration and login functionality using socket programming and password hashing.

## Features

- **User Registration**: Create new accounts with secure password storage
- **User Login**: Authenticate existing users with credentials
- **Password Security**: Passwords are hashed using SHA-256 before storage
- **Multi-client Support**: Server can handle multiple simultaneous connections
- **Input Validation**: Basic client-side input validation

## Installation & Usage

### 1. Start the Server
```bash
python server.py
The server will start listening on localhost:9999

2. Run the Client
bash
python client.py
3. Follow the Prompts
Choose 1 to register a new account

Choose 2 to login with existing credentials

Enter your username and password when prompted

How It Works
Security Features
Password Hashing: All passwords are hashed using SHA-256 algorithm before storage

Secure Storage: Plain text passwords are never stored in the database

Network Security: Communication happens over local sockets

Components
Server (server.py)

Listens for client connections on port 9999

Handles multiple clients simultaneously using threading

Processes registration and login requests

Interfaces with the database module

Client (client.py)

Connects to the server

Provides user interface for registration/login

Sends credentials to server for processing

Database (DataBase.py)

Manages user data storage in Users_db.txt

Handles password hashing and verification

Provides functions for user registration and authentication
