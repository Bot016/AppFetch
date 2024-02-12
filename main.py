import tkinter as tk
from tkinter import ttk

from downloader import Download

class MainFrame:
    cor_padrao = "#242424"

    def __init__(self):
        self.window = tk.Tk()
        self.config()
        self.frames()
        self.styles()
        self.labels()
        self.apks()
        self.button()
        
        self.window.mainloop()
    
    def config(self):
        self.window.title("Ferramentas")
        #self.window.iconbitmap()
        self.window.geometry("320x463") # Possível Alteração
        #self.window.resizable(False, False)
        self.window.configure(bg=self.cor_padrao)

    def line(self):
        self.separator = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=20, pady=5)

    def frames(self):
        self.label_tile = tk.Label(self.window, text="SELECIONE OS APLICATIVOS", font=("Bahnschrift", 17, "bold"), bg=self.cor_padrao, fg="white")
        self.label_tile.pack(pady=10)
        self.line()

        self.frames_names = ['navegadores', 'compressao', 'email', 'antivírus', 'outros']
        self.frames = {}

        for frame_name in self.frames_names:
            frame = tk.Frame(self.window, bg=self.cor_padrao)
            frame.pack(pady=5)
            self.frames[frame_name] = frame
            self.line()

    def styles(self):
        self.style = ttk.Style()
        self.style.configure('Custom.TCheckbutton', background=self.cor_padrao, foreground='white', selectcolor=self.cor_padrao, activebackground=self.cor_padrao, highlightthickness=0, activeforeground='white', font=("Bahnschrift", 10))

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Bahnschrift", 10), foreground="#242424", background="#242424", padding=-1)
    
    def on_antivirus_checkbox_changed(self):
        if self.apks_var["Antivírus"].get() == 1:
            self.apks_var["Small Office"].set(0)

    def on_smalloffice_checkbox_changed(self):
        if self.apks_var["Small Office"].get() == 1:
            self.apks_var["Antivírus"].set(0)

    def labels(self):
        self.label_names = [name.upper() for name in self.frames_names]
        self.labels = {}

        for label_name, frame_name in zip(self.label_names, self.frames_names):
            label = tk.Label(self.frames[frame_name], text=label_name, font=("Bahnschrift", 13), bg=self.cor_padrao, fg="white")
            label.pack(anchor="center")
            self.labels[frame_name] = label
    
    def apks(self):
    # Nomes dos APKs e dos frames combinados em uma única lista
        apk_frame_list = [
            ("Chrome", "navegadores"),
            ("Firefox", "navegadores"),
            ("7zip", "compressao"),
            ("Winrar", "compressao"),
            ("Thunderbird", "email"),
            ("Antivírus", "antivírus"),
            ("Small Office", "antivírus"),
            ("Anydesk", "outros"),
            ("CCleaner", "outros"),
            ("Java 8", "outros")
        ]
        self.apks = {}
        self.apks_var = {}

        for apk_name, frame_name in apk_frame_list:
            self.apks_var[apk_name] = tk.IntVar()
            apk = ttk.Checkbutton(self.frames[frame_name], text=apk_name, variable=self.apks_var[apk_name], style='Custom.TCheckbutton', takefocus=False)
            self.apks[apk_name] = apk
            apk.pack(side=tk.LEFT, padx=5)

        self.apks["Antivírus"].config(command=self.on_antivirus_checkbox_changed)
        self.apks["Small Office"].config(command=self.on_smalloffice_checkbox_changed)

    def download_button_callback(self):
        Download(self.apks_var,self.window)
        
    def button(self):
        self.DownloadButton = ttk.Button(self.window, text="BAIXAR APLICATIVOS", style="Custom.TButton", command=self.download_button_callback, takefocus=False)
        self.DownloadButton.pack(anchor="center", pady=10)

        self.instalando_label = tk.Label(self.window, text=" ", font=("Bahnschrift", 12), bg="#242424", fg="white")
        # instalado_label.pack(anchor='center')

        #self.progress_bar = ttk.Progressbar(self.window, length=300, variable=porcentagem, takefocus=False)

        self.instalar_botao = ttk.Button(self.window, text="INSTALAR APLICATIVOS", takefocus=False, style="Custom.TButton")
        # instalar_botao.pack(anchor='center', pady=10)

window = MainFrame()