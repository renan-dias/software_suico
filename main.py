<<<<<<< Updated upstream
=======
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
import requests
import qrcode

class SoftwareSuico:
    def __init__(self, root):
        self.root = root
        self.root.title("Software Suíço")
        self.root.geometry("500x400")
        
        self.label = tk.Label(root, text="Escolha uma ferramenta:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.btn_remove_bg = tk.Button(root, text="Remover Fundo de Imagem", command=self.remover_fundo)
        self.btn_remove_bg.pack(pady=5)
        
        self.btn_converter_moeda = tk.Button(root, text="Conversor de Moedas", command=self.converter_moeda)
        self.btn_converter_moeda.pack(pady=5)
        
        self.btn_qr_code = tk.Button(root, text="Gerar QR Code", command=self.gerar_qr_code)
        self.btn_qr_code.pack(pady=5)

    def remover_fundo(self):
        caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if not caminho_imagem:
            return
        
        imagem = cv2.imread(caminho_imagem)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        
        fundo_branco = np.full(imagem.shape, 255, dtype=np.uint8)
        mascara = np.all(imagem > [200, 200, 200], axis=-1)
        fundo_branco[mascara] = imagem[mascara]
        
        imagem_resultado = Image.fromarray(fundo_branco)
        caminho_salvo = "imagem_sem_fundo.png"
        imagem_resultado.save(caminho_salvo)
        messagebox.showinfo("Sucesso", f"Imagem salva como {caminho_salvo}")
    
    def converter_moeda(self):
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            dados = response.json()
            taxa_brl = dados['rates']['BRL']
            messagebox.showinfo("Conversor de Moedas", f"1 USD = {taxa_brl:.2f} BRL")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao obter taxa de câmbio: {e}")
    
    def gerar_qr_code(self):
        texto = filedialog.askstring("QR Code", "Digite o texto para o QR Code:")
        if not texto:
            return
        
        qr = qrcode.make(texto)
        caminho_qr = "qrcode.png"
        qr.save(caminho_qr)
        messagebox.showinfo("Sucesso", f"QR Code salvo como {caminho_qr}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareSuico(root)
    root.mainloop()
>>>>>>> Stashed changes
