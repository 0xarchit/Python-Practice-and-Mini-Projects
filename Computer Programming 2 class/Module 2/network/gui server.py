import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Setup tkinter GUI window and components
root = tk.Tk()
root.title("Server GUI")

chat_area = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_area.pack(padx=10, pady=10)
entry = tk.Entry(root, width=40)
send_button = tk.Button(root, text="Send")

# Hide text bar widgets initially
entry.pack_forget()
send_button.pack_forget()

# Create socket object and start server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.16.146.248', 12345))
server_socket.listen(1)

def update_chat(message):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, message + "\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

client_socket = None

def handle_client():
    global client_socket
    client_socket, addr = server_socket.accept()
    update_chat(f"Connected to {addr}")
    # Show text bar widgets after connection established
    root.after(0, lambda: [
        entry.pack(padx=10, pady=(0,10), side=tk.LEFT),
        send_button.pack(padx=10, pady=(0,10), side=tk.LEFT)
    ])
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower() == 'exit':
                update_chat("Client disconnected.")
                break
            update_chat("Client: " + message)
        except Exception as e:
            update_chat("Error: " + str(e))
            break
    client_socket.close()
    server_socket.close()

def send_message(event=None):  # modified to accept an optional event
    msg = entry.get()
    if client_socket:
        try:
            client_socket.send(msg.encode('utf-8'))
            update_chat("You: " + msg)
        except Exception as e:
            update_chat("Send error: " + str(e))
    entry.delete(0, tk.END)

send_button.config(command=send_message)
entry.bind("<Return>", send_message)

# Start client handler thread
threading.Thread(target=handle_client, daemon=True).start()

root.mainloop()