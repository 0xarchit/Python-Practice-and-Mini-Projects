import tkinter as tk

class HelloWorldApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Hello World")
        self.root.geometry("300x200")  # Set window size
        
        # Create and configure the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True)
        
        # Create a label with "Hello World" text
        self.label = tk.Label(self.main_frame, 
                            text="Hello World!", 
                            font=("Arial", 24))
        self.label.pack(pady=20)
        
        # Create a quit button
        self.quit_button = tk.Button(self.main_frame,
                                   text="Quit",
                                   command=self.root.quit,
                                   font=("Arial", 12))
        self.quit_button.pack(pady=10)

def main():
    # Create the root window
    root = tk.Tk()
    # Create an instance of our HelloWorldApp class
    app = HelloWorldApp(root)
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()