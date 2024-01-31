import tkinter as tk
from tkinter import ttk, filedialog

class JanelaPrincipal:
    cor_padrao = "#242424"

    def __init__(self):
        self.window = tk.Tk()
        self.config()
        self.frames()
        self.styles()
        self.labels()
        self.apks()
        
        self.window.mainloop()
    
    def config(self):
        self.window.title("Ferramentas")
        #self.window.iconbitmap()
        self.window.geometry("320x463") # Possível Alteração
        self.window.resizable(False, False)
        self.window.configure(bg=self.cor_padrao)

    def linha_separadora(self):
        self.separator = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=20, pady=5)

    def frames(self):
        self.frames_names = ['navegadores', 'compressao', 'email', 'antivírus', 'outros']
        self.frames = {}

        for frame_name in self.frames_names:
            frame = tk.Frame(self.window, bg=self.cor_padrao)
            frame.pack(pady=5)
            self.frames[frame_name] = frame
            self.linha_separadora()

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
        self.apks_names = ["Chrome", "Firefox","7zip", "Winrar", "Thunderbird", "Antivírus", "Small Office", "Anydesk", "CCleaner", "Java 8"]
        self.apks = {}
        self.frame_names_apk = ["navegadores", "navegadores", "compressao", "compressao", "email", "antivírus", "antivírus", "outros", "outros", "outros"]
        self.apks_var = {}

        for apks_name, frame_name in zip(self.apks_names, self.frame_names_apk ):
            self.apks_var[apks_name] = tk.IntVar()
            apks = ttk.Checkbutton(self.frames[frame_name], text=apks_name, variable=self.apks_var[apks_name], style='Custom.TCheckbutton', takefocus=False)
            self.apks[apks_name] = apks
            apks.pack(side=tk.LEFT, padx=5)
        
        self.apks["Antivírus"].config(command=self.on_antivirus_checkbox_changed)
        self.apks["Small Office"].config(command=self.on_smalloffice_checkbox_changed)

    def button():


window = JanelaPrincipal()