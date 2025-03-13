import customtkinter as ctk
import qrcode
import cv2
from PIL import Image, ImageTk

class QRCodeUtil:
    def __init__(self, parent):
        """Cria a interface do gerador e leitor de QR Code."""
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Gerador e Leitor de QR Code")
        self.label.pack(pady=10)

        # Entrada para gerar QR Code
        self.entry_qr = ctk.CTkEntry(self.frame, placeholder_text="Digite o texto ou link")
        self.entry_qr.pack(pady=5)

        self.btn_gerar = ctk.CTkButton(self.frame, text="Gerar QR Code", command=self.gerar_qr)
        self.btn_gerar.pack(pady=5)

        # Botão para selecionar imagem do QR Code
        self.btn_ler = ctk.CTkButton(self.frame, text="Ler QR Code", command=self.ler_qr)
        self.btn_ler.pack(pady=5)

        self.resultado = ctk.CTkLabel(self.frame, text="")
        self.resultado.pack(pady=10)

        self.qr_imagem_label = ctk.CTkLabel(self.frame, text="")
        self.qr_imagem_label.pack(pady=10)

    def gerar_qr(self):
        """Gera um QR Code a partir do texto inserido."""
        texto = self.entry_qr.get()
        if texto:
            qr = qrcode.make(texto)
            qr.save("qrcode.png")

            imagem = Image.open("qrcode.png")
            imagem = imagem.resize((150, 150))
            img_tk = ImageTk.PhotoImage(imagem)

            self.qr_imagem_label.configure(image=img_tk)
            self.qr_imagem_label.image = img_tk

    def ler_qr(self):
        """Lê um QR Code a partir de uma imagem."""
        arquivo = "qrcode.png"  # Aqui você pode modificar para abrir um arquivo escolhido pelo usuário
        img = cv2.imread(arquivo)
        detector = cv2.QRCodeDetector()
        valor, _, _ = detector.detectAndDecode(img)

        if valor:
            self.resultado.configure(text=f"Conteúdo do QR: {valor}")
        else:
            self.resultado.configure(text="Nenhum QR Code detectado.")
