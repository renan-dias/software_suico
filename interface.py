import customtkinter as ctk
from conversor import ConversorMoeda, ConversorUnidades
from imagem import RemovedorFundo
from qrcode_util import QRCodeUtil
from clima import Clima

class SoftwareSuico(ctk.CTk):
    def __init__(self):
        super().__init__()  # Inicializa o Tkinter

        self.title("Software Suíço")  # Define o título da janela
        self.geometry("600x400")  # Define o tamanho da janela
        ctk.set_appearance_mode("dark")  # Define o tema escuro

        # Criando o menu lateral
        self.sidebar = ctk.CTkFrame(self, width=150)
        self.sidebar.pack(side="left", fill="y")

        # Criando botões para cada funcionalidade
        self.btn_moeda = ctk.CTkButton(self.sidebar, text="Converter Moeda", command=self.abrir_conversor_moeda)
        self.btn_moeda.pack(pady=10)

        self.btn_unidade = ctk.CTkButton(self.sidebar, text="Converter Unidade", command=self.abrir_conversor_unidade)
        self.btn_unidade.pack(pady=10)

        self.btn_remover_fundo = ctk.CTkButton(self.sidebar, text="Remover Fundo", command=self.abrir_removedor_fundo)
        self.btn_remover_fundo.pack(pady=10)

        self.btn_qr = ctk.CTkButton(self.sidebar, text="QR Code", command=self.abrir_qrcode)
        self.btn_qr.pack(pady=10)

        self.btn_clima = ctk.CTkButton(self.sidebar, text="Previsão do Clima", command=self.abrir_clima)
        self.btn_clima.pack(pady=10)

        # Criando o espaço principal onde os módulos serão carregados
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

    # Métodos para abrir cada módulo
    def abrir_conversor_moeda(self):
        ConversorMoeda(self.main_frame)

    def abrir_conversor_unidade(self):
        ConversorUnidades(self.main_frame)

    def abrir_removedor_fundo(self):
        RemovedorFundo(self.main_frame)

    def abrir_qrcode(self):
        QRCodeUtil(self.main_frame)

    def abrir_clima(self):
        Clima(self.main_frame)

if __name__ == "__main__":
    app = SoftwareSuico()
    app.mainloop()
