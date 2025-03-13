import customtkinter as ctk
import requests

class ConversorMoeda:
    def __init__(self, parent):
        """Cria a interface do conversor de moeda."""
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Conversor de Moeda")
        self.label.pack(pady=10)

        self.entry_valor = ctk.CTkEntry(self.frame, placeholder_text="Valor em USD")
        self.entry_valor.pack(pady=5)

        self.btn_converter = ctk.CTkButton(self.frame, text="Converter para BRL", command=self.converter)
        self.btn_converter.pack(pady=10)

        self.resultado = ctk.CTkLabel(self.frame, text="")
        self.resultado.pack()

    def converter(self):
        """Obtém a taxa de câmbio e converte o valor."""
        valor = float(self.entry_valor.get())
        resposta = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
        taxa = resposta["rates"]["BRL"]
        convertido = valor * taxa
        self.resultado.configure(text=f"Valor em BRL: {convertido:.2f}")

class ConversorUnidades:
    def __init__(self, parent):
        """Cria a interface do conversor de unidades."""
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Conversor de Unidades (Km para Milhas)")
        self.label.pack(pady=10)

        self.entry_valor = ctk.CTkEntry(self.frame, placeholder_text="Valor em Km")
        self.entry_valor.pack(pady=5)

        self.btn_converter = ctk.CTkButton(self.frame, text="Converter", command=self.converter)
        self.btn_converter.pack(pady=10)

        self.resultado = ctk.CTkLabel(self.frame, text="")
        self.resultado.pack()

    def converter(self):
        """Converte quilômetros para milhas."""
        km = float(self.entry_valor.get())
        milhas = km * 0.621371
        self.resultado.configure(text=f"{km} km = {milhas:.2f} milhas")
