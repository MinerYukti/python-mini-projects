import socket
import threading
from datetime import datetime

clients = []
nicknames = []

# ---------- Utility ----------

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# ---------- Server ----------

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if message.decode().startswith("/users"):
                users = ", ".join(nicknames)
                client.send(f"[{timestamp()}] Active Users: {users}".encode())

            else:
                broadcast(message)

        except:
            index = clients.index(client)
            nickname = nicknames[index]

            clients.remove(client)
            nicknames.remove(nickname)
            client.close()

            broadcast(f"[{timestamp()}] {nickname} left the chat.".encode())
            break


def start_server():

    host = "127.0.0.1"
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print("Server started... Waiting for connections")

    while True:

        client, address = server.accept()
        print("Connected with", address)

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} joined the chat")

        broadcast(f"[{timestamp()}] {nickname} joined the chat.".encode())
        client.send("Connected to chat server!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# ---------- Client ----------

def start_client():

    nickname = input("Enter your nickname: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    def receive():

        while True:
            try:
                message = client.recv(1024).decode()

                if message == "NICK":
                    client.send(nickname.encode())

                else:
                    print(message)

            except:
                print("Disconnected from server")
                client.close()
                break

    def write():

        while True:

            message = input()

            if message == "/exit":
                client.close()
                break

            time = timestamp()
            formatted = f"[{time}] {nickname}: {message}"

            client.send(formatted.encode())

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

# ---------- Main Menu ----------

print("===== CHAT APPLICATION =====")
print("1. Start Server")
print("2. Start Client")

choice = input("Enter choice: ")

if choice == "1":
    start_server()

elif choice == "2":
    start_client()

else:
    print("Invalid option")