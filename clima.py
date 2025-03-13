import customtkinter as ctk
import requests

class Clima:
    def __init__(self, parent):
        """Cria a interface da previsão do clima."""
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Previsão do Clima")
        self.label.pack(pady=10)

        self.entry_cidade = ctk.CTkEntry(self.frame, placeholder_text="Digite a cidade")
        self.entry_cidade.pack(pady=5)

        self.btn_buscar = ctk.CTkButton(self.frame, text="Buscar Clima", command=self.buscar_clima)
        self.btn_buscar.pack(pady=10)

        self.resultado = ctk.CTkLabel(self.frame, text="")
        self.resultado.pack()

    def buscar_clima(self):
        """Obtém a previsão do tempo de uma API pública."""
        cidade = self.entry_cidade.get()
        resposta = requests.get(f"https://wttr.in/{cidade}?format=%C+%t")
        self.resultado.configure(text=resposta.text)
