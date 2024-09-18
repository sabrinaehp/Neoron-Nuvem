import tkinter as tk
from views.voo_register import ViewVoo
from views.localidades_register import ViewLocalidade
from views.main_menu import ViewHome


class App(ViewVoo, ViewLocalidade, ViewHome):
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Companhia Aérea")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(fill="both", expand=True)
        self.main_menu()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
