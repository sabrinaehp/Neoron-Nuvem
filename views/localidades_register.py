import tkinter as tk
from tkinter import ttk, messagebox
from db_requests import LocalDB


class ViewLocalidade:
    def show_localidades(self):
        self.clear_frame()

        tk.Label(
            self.frame, text="Localidades Disponíveis", font=("Helvetica", 14)
        ).pack(pady=10)

        form_frame = tk.Frame(self.frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="CEP:").grid(row=0, column=0, padx=5, pady=5)
        cep_entry = tk.Entry(form_frame)
        cep_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="País:").grid(row=0, column=2, padx=5, pady=5)
        pais_entry = tk.Entry(form_frame)
        pais_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Estado:").grid(row=1, column=0, padx=5, pady=5)
        estado_entry = tk.Entry(form_frame)
        estado_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Cidade:").grid(row=1, column=2, padx=5, pady=5)
        cidade_entry = tk.Entry(form_frame)
        cidade_entry.grid(row=1, column=3, padx=5, pady=5)

        def load_treeview(information: list[tuple[str]]):
            for info in information:
                self.tree_localidades.insert(
                    "", "end", values=(info[0], info[1], info[2], info[3])
                )

        def delete_localidade():
            selected_item = self.tree_localidades.selection()
            item_data = self.tree_localidades.item(selected_item, "values")
            db = LocalDB()
            db.delete_in_table("localidade", "cep", item_data[0])
            if selected_item:
                self.tree_localidades.delete(selected_item)
            else:
                messagebox.showwarning(
                    "Erro", "Nenhuma localidade selecionada para exclusão"
                )

        def add_localidade() -> None:
            cep = cep_entry.get()
            pais = pais_entry.get()
            estado = estado_entry.get()
            cidade = cidade_entry.get()
            db = LocalDB()
            if db.select_table("localidade", "cep", f"{cep}"):
                messagebox.showwarning("Erro", "Já existe uma localidade com este CEP!")
                return
            if cep and pais and estado and cidade:
                self.tree_localidades.insert(
                    "", "end", values=(cep, pais, estado, cidade)
                )

                db.insert_table(
                    "localidade",
                    {
                        "cep": f"{cep}",
                        "pais": f"{pais}",
                        "estado": f"{estado}",
                        "cidade": f"{cidade}",
                    },
                )
                cep_entry.delete(0, tk.END)
                pais_entry.delete(0, tk.END)
                estado_entry.delete(0, tk.END)
                cidade_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos")

        tk.Button(self.frame, text="Adicionar Localidade", command=add_localidade).pack(
            pady=5
        )

        columns = ("cep", "pais", "estado", "cidade")
        self.tree_localidades = ttk.Treeview(
            self.frame, columns=columns, show="headings"
        )

        self.tree_localidades.heading("cep", text="CEP")
        self.tree_localidades.heading("pais", text="País")
        self.tree_localidades.heading("estado", text="Estado")
        self.tree_localidades.heading("cidade", text="Cidade")

        self.tree_localidades.column("cep", width=100, anchor=tk.W)
        self.tree_localidades.column("pais", width=150, anchor=tk.W)
        self.tree_localidades.column("estado", width=100, anchor=tk.W)
        self.tree_localidades.column("cidade", width=150, anchor=tk.W)

        tk.Button(self.frame, text="Voltar", command=self.main_menu).pack(pady=10)

        self.tree_localidades.pack(fill="both", expand=True)
        tk.Button(
            self.frame, text="Excluir Localidade", command=delete_localidade
        ).pack(pady=5)

        db = LocalDB()
        load_treeview(db.select_all_for_table("localidade"))


if __name__ == "__main__":
    ...
