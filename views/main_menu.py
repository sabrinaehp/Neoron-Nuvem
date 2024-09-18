import tkinter as tk
from tkinter import Menu, PhotoImage
from utils import linkedin_link
from static.style import button_style, label_style_title

class ViewHome:
    def main_menu(self):
        self.clear_frame()

        # Menu superior
        self.barrademenu = Menu(self.root)
        self.root.config(menu=self.barrademenu)
        self.icon_linkedin = PhotoImage(file="static/img/linkedin.png").subsample(5, 5)
        contatos = Menu(self.barrademenu, tearoff=0, bg="#F5F5DC")

        self.barrademenu.add_cascade(label="CONTATOS", menu=contatos)
        contatos.add_command(
            label="Linkedin", image=self.icon_linkedin, command=linkedin_link
        )

        # Título principal
        tk.Label(self.frame, text="Nuvem", font=("Arial", 48, "bold"), bg="white").pack(pady=(60, 0))
        tk.Label(self.frame, text="flight management", font=("Arial", 18), bg="white").pack()

        # Botão Registrar Voo
        tk.Button(
            self.frame,
            text="REGISTRO DE VOO",
            command=self.show_voos,
            **button_style
        ).pack(pady=10)

        # Botão Registrar Localidades
        tk.Button(
            self.frame,
            text="LOCALIDADES",
            command=self.show_localidades,
            **button_style
        ).pack(pady=10)

        # Link para tutorial
        tk.Label(self.frame, text="Alguma dúvida? Consulte nosso tutorial.", font=("Arial", 12), bg="white").pack(pady=(30, 5))

        link_label = tk.Label(self.frame, text="Clique aqui.", font=("Arial", 12, "underline"), fg="blue", bg="white", cursor="hand2")
        link_label.pack()

if __name__ == "__main__":
    ...
