import customtkinter as ctk
from rembg import remove
from PIL import Image, ImageTk
import io

class RemovedorFundo:
    def __init__(self, parent):
        """Cria a interface do removedor de fundo de imagem."""
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Removedor de Fundo de Imagem")
        self.label.pack(pady=10)

        # Botão para carregar imagem
        self.btn_carregar = ctk.CTkButton(self.frame, text="Carregar Imagem", command=self.carregar_imagem)
        self.btn_carregar.pack(pady=5)

        self.btn_remover = ctk.CTkButton(self.frame, text="Remover Fundo", command=self.remover_fundo)
        self.btn_remover.pack(pady=5)

        self.img_label = ctk.CTkLabel(self.frame, text="")
        self.img_label.pack(pady=10)

        self.imagem_original = None

    def carregar_imagem(self):
        """Carrega uma imagem do sistema."""
        caminho = "imagem_exemplo.png"  # Aqui você pode modificar para abrir um arquivo escolhido pelo usuário
        self.imagem_original = Image.open(caminho)

        imagem_tk = ImageTk.PhotoImage(self.imagem_original.resize((200, 200)))
        self.img_label.configure(image=imagem_tk)
        self.img_label.image = imagem_tk

    def remover_fundo(self):
        """Remove o fundo da imagem carregada."""
        if self.imagem_original:
            img_bytes = io.BytesIO()
            self.imagem_original.save(img_bytes, format="PNG")
            img_sem_fundo = remove(img_bytes.getvalue())

            img_final = Image.open(io.BytesIO(img_sem_fundo))
            img_tk = ImageTk.PhotoImage(img_final.resize((200, 200)))

            self.img_label.configure(image=img_tk)
            self.img_label.image = img_tk
