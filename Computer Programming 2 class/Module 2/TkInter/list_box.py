import tkinter as tk
class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("300x400")
        self.createApp()

    def createApp(self):
        self.entry = tk.Entry(self.root, font=('TimesNewRoman', 16))
        self.entry.pack(pady=20)
        tk.Button(self.root, text="Add", command=self.addItem).pack(pady=5)
        tk.Button(self.root, text="Remove", command=self.removeItem).pack(pady=5)

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=20)

    def addItem(self):
        if self.entry.get() != '':
            self.listbox.insert(tk.END, self.entry.get())
            self.entry.delete(0, tk.END)


    def removeItem(self):
        self.listbox.delete(tk.ANCHOR)

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoList(root)
    

    root.mainloop()