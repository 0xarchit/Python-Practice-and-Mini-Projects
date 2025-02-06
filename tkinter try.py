import tkinter as tk

class PalindromeChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Palindrome Checker")
        
        self.label = tk.Label(root, text="Enter a word:", font=("Arial", 16), fg='blue')
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Check Palindrome", command=self.check_palindrome, font=("Arial", 14))
        self.check_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg='green')
        self.result_label.pack(pady=20)

    def check_palindrome(self):
        """Check if the entered word is a palindrome."""
        user_input = self.entry.get().strip()
        cleaned_input = ''.join(e for e in user_input if e.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lowercase
        
        if cleaned_input == cleaned_input[::-1]:
            self.result_label.config(text=f"'{user_input}' is a palindrome!", fg='green')
        else:
            self.result_label.config(text=f"'{user_input}' is not a palindrome.", fg='red')

root = tk.Tk()
root.geometry("600x400")

checker = PalindromeChecker(root)
root.mainloop()
