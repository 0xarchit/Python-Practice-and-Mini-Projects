import tkinter as tk
class taskPerf:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Performer")
        self.root.geometry("300x400")
        self.createApp()

    def createApp(self):
        pass

    def checkTask(self):
        pass

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