import tkinter as tk
class taskPerf:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Performer")
        self.root.geometry("300x400")
        self.createApp()

    def createApp(self):
        self.entry = tk.Entry(self.root, font=('TimesNewRoman', 16))
        self.entry.pack(pady=20)
        self.checkPrime = tk.IntVar()
        self.checkEven = tk.IntVar()
        self.checkOdd = tk.IntVar()
        self.checkPerfect = tk.IntVar()
        self.checkArmstrong = tk.IntVar()
        tk.Checkbutton(self.root, text="Prime", variable=self.checkPrime).pack(pady=5)
        tk.Checkbutton(self.root, text="Even", variable=self.checkEven).pack(pady=5)
        tk.Checkbutton(self.root, text="Odd", variable=self.checkOdd).pack(pady=5)
        tk.Checkbutton(self.root, text="Perfect", variable=self.checkPerfect).pack(pady=5)
        tk.Checkbutton(self.root, text="Armstrong", variable=self.checkArmstrong).pack(pady=5)
        tk.Button(self.root, text="Check", command=self.checkTask).pack(pady=5)
        self.result = tk.Label(self.root, text="")
        self.result.pack(pady=20)  

    def checkTask(self):
        num = int(self.entry.get())
        result = ""
        if self.checkPrime.get():
            result += "Prime: " + str(self.is_prime(num)) + "\n"
        if self.checkEven.get():
            result += "Even: " + str(self.is_even(num)) + "\n"
        if self.checkOdd.get():
            result += "Odd: " + str(self.is_odd(num)) + "\n"
        if self.checkPerfect.get():
            result += "Perfect: " + str(self.is_perfect(num)) + "\n"
        if self.checkArmstrong.get():
            result += "Armstrong: " + str(self.is_armstrong(num))
        self.result.config(text=result)


    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def is_even(self, num):
        return num % 2 == 0
    
    def is_odd(self, num):
        return num % 2 != 0
    
    def is_perfect(self, num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return num == sum

    def is_armstrong(self, num):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        return num == sum

if __name__ == '__main__':
    root = tk.Tk()
    app = taskPerf(root)
    

    root.mainloop()
