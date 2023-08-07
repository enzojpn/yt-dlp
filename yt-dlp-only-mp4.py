import os
from tkinter import *
from tkinter import filedialog
import subprocess

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Cole a URL do Vídeo do YouTube -> Video")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.urlLabel = Label(self.segundoContainer, text="URL", font=self.fontePadrao)
        self.urlLabel.pack(side=LEFT)
        self.url = Entry(self.segundoContainer)
        self.url["width"] = 60
        self.url["font"] = self.fontePadrao
        self.url.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Download"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.realizaDownload
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def realizaDownload(self):
        url = self.url.get()

        # Obter informações do vídeo para usar no nome de arquivo padrão
        info_process = subprocess.Popen(["yt-dlp", "--get-title", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = info_process.communicate()
        video_title = stdout.strip()

        # Abre a caixa de diálogo para escolher o local e nome de arquivo de download
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")],
                                                 initialfile=f"{video_title}.mp4")

        if not file_path:
            self.mensagem["text"] = "Download cancelado."
            return

        # Comando para download no formato MP4 com o caminho escolhido
        comando = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "{file_path}" {url}'
        try:
            subprocess.run(comando, shell=True)
            self.mensagem["text"] = "Download concluído!"
        except Exception as e:
            self.mensagem["text"] = f"Erro: {str(e)}"

root = Tk()
Application(root)
root.mainloop()
