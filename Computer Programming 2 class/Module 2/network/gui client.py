import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Client GUI")

chat_area = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_area.pack(padx=10, pady=10)
entry = tk.Entry(root, width=40)
send_button = tk.Button(root, text="Send")

# Hide text bar widgets initially
entry.pack_forget()
send_button.pack_forget()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def update_chat(message):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, message + "\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower() == 'exit':
                update_chat("Server disconnected.")
                break
            update_chat("Server: " + message)
        except Exception as e:
            update_chat("Error: " + str(e))
            break
    client_socket.close()

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

def connect_to_server():
    try:
        client_socket.connect(('172.16.147.84', 12345))
        update_chat("Connected to server.")
        # Show text bar widgets after connection established
        root.after(0, lambda: [
            entry.pack(padx=10, pady=(0,10), side=tk.LEFT),
            send_button.pack(padx=10, pady=(0,10), side=tk.LEFT)
        ])
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        update_chat("Connection error: " + str(e))

threading.Thread(target=connect_to_server, daemon=True).start()

root.mainloop()