import tkinter as tk
from tkinter import ttk, messagebox
from db_requests import LocalDB
from utils import validar_data, validar_hora, verificar_diferenca_hora
from static.style import label_style_title, button_style


class ViewVoo:
    def show_voos(self):
        self.clear_frame()

        tk.Label(self.frame, text="Registro de Voos", **label_style_title).pack(
            pady=10
        )

        form_frame = tk.Frame(self.frame)
        form_frame.pack(pady=10)
        db = LocalDB()
        localidades = [
            f"{info[3]} - {info[2]} - {info[1]} | {info[0]}"
            for info in db.select_all_for_table("localidade")
        ]

        tk.Label(form_frame, text="Origem:").grid(row=0, column=0, padx=5, pady=5)
        origem_combobox = ttk.Combobox(form_frame, values=localidades)
        origem_combobox.grid(row=0, column=1, padx=5, pady=5)
        origem_combobox.set("Selecione a origem")

        tk.Label(form_frame, text="Destino:").grid(row=0, column=2, padx=5, pady=5)
        destino_combobox = ttk.Combobox(form_frame, values=localidades)
        destino_combobox.grid(row=0, column=3, padx=5, pady=5)
        destino_combobox.set("Selecione o destino")

        tk.Label(form_frame, text="Data:").grid(row=1, column=0, padx=5, pady=5)
        data_entry = tk.Entry(form_frame)
        data_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Horário:").grid(row=1, column=2, padx=5, pady=5)
        horario_entry = tk.Entry(form_frame)
        horario_entry.grid(row=1, column=3, padx=5, pady=5)

        def delete_voo():
            selected_item = self.tree_voos.selection()
            item_data = self.tree_voos.item(selected_item, "values")
            db = LocalDB()
            db.delete_in_table("voo", "code", item_data[0])
            if selected_item:
                self.tree_voos.delete(selected_item)
            else:
                messagebox.showwarning("Erro", "Nenhum voo selecionado para exclusão")

        def cep_search(cep: str) -> str:
            localidade = db.select_table("localidade", "cep", cep)[0]
            return f"{localidade[3]} - {localidade[2]} - {localidade[1]}"

        def possibilidade_voo(data: str, hora: str, destino: str) -> bool:
            date_voos = db.select_table("voo", "data", data)
            for voo in date_voos:
                if voo[2] == destino:
                    return False
            all_date_voos = db.select_all_for_table("voo")
            for voo in all_date_voos:
                print(voo[4])
                if verificar_diferenca_hora(voo[4], hora):
                    return False
            return True

        def load_treeview_voos(information: list[tuple[str]]):
            for info in information:
                self.tree_voos.insert(
                    "",
                    "end",
                    values=(
                        info[0],
                        cep_search(info[1]),
                        cep_search(info[2]),
                        info[3],
                        info[4],
                    ),
                )

        def add_voo():
            origem = origem_combobox.get()
            destino = destino_combobox.get()
            data = data_entry.get()
            horario = horario_entry.get()

            if (
                origem != "Selecione a origem"
                and destino != "Selecione o destino"
                and data
                and horario
            ):
                destino = destino[destino.find("|") + 1 :].strip()
                if not validar_data(data):
                    messagebox.showinfo(
                        "Data Inválida", "A data deve seguir o padrão dd/mm/aaaa!"
                    )
                    return
                if not validar_hora(horario):
                    messagebox.showinfo(
                        "Horario Inválido", "A hora deve seguir o padrão hh:mm!"
                    )
                    return
                if not possibilidade_voo(data, horario, destino):
                    messagebox.showinfo(
                        "Voo Sem Possibilidade",
                        "Os voos devem ter mais de meia hora de diferença entre si e não pode haver dois voos no mesmo dia para o mesmo local!",
                    )
                    return

                voo_code = db.unique_key("voo", "code")
                db.insert_table(
                    "voo",
                    {
                        "code": voo_code,
                        "origem": origem[origem.find("|") + 1 :].strip(),
                        "destino": destino[destino.find("|") + 1 :].strip(),
                        "data": data,
                        "hora": horario,
                    },
                )
                self.tree_voos.insert(
                    "",
                    "end",
                    values=(
                        voo_code,
                        cep_search(origem[origem.find("|") + 1 :].strip()),
                        cep_search(destino),
                        data,
                        horario,
                    ),
                )
                origem_combobox.set("Selecione a origem")
                destino_combobox.set("Selecione o destino")
                data_entry.delete(0, tk.END)
                horario_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos")

        tk.Button(self.frame, text="Adicionar Voo", command=add_voo).pack(pady=5)

        columns = ("code", "origem", "destino", "data", "hora")
        self.tree_voos = ttk.Treeview(self.frame, columns=columns, show="headings")
        self.tree_voos.heading("code", text="Code")
        self.tree_voos.heading("origem", text="Origem")
        self.tree_voos.heading("destino", text="Destino")
        self.tree_voos.heading("data", text="Data")
        self.tree_voos.heading("hora", text="Hora")
        self.tree_voos.pack(fill="both", expand=True)

        self.tree_voos.column("code", width=120, anchor=tk.W)
        self.tree_voos.column("origem", width=170, anchor=tk.W)
        self.tree_voos.column("destino", width=170, anchor=tk.W)
        self.tree_voos.column("data", width=60, anchor=tk.W)
        self.tree_voos.column("hora", width=30, anchor=tk.W)

        load_treeview_voos(db.select_all_for_table("voo"))

        tk.Button(self.frame, text="Excluir Voo", command=delete_voo).pack(pady=5)

        tk.Button(self.frame, text="Voltar", command=self.main_menu).pack(pady=10)


if __name__ == "__main__":
    ...
