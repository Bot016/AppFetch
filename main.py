import ssl
import tkinter as tk
from tkinter import ttk

from downloader import Download
from image import MainImage

class MainFrame:

    default_color = "#242424"

    def __init__(self, window):
        self.window = window
        # Disable SSL
        ssl._create_default_https_context = ssl._create_unverified_context
        self.config()
        self.frames()
        self.styles()
        self.labels()
        self.apks_names_buttons()
        self.button()
    
    def config(self):
        # Configure main window settings
        self.window.title("Ferramentas")
        #self.window.iconbitmap()
        self.window.geometry("320x463") 
        self.window.resizable(False, False)
        self.window.configure(bg=self.default_color)

    def line(self):
        # Create a separator line
        self.separator = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=20, pady=5)

    def frames(self):
        # Create frames
        self.label_title = tk.Label(self.window, text="SELECIONE OS APLICATIVOS", font=("Bahnschrift", 17, "bold"), bg=self.default_color, fg="white")
        self.label_title.pack(pady=10)
        self.label_title.bind("<Button-1>", self.image_window)
        self.line()

        self.frames_names = ['navegadores', 'compressao', 'email', 'antivírus', 'outros']
        self.frames = {}

        for frame_name in self.frames_names:
            frame = tk.Frame(self.window, bg=self.default_color)
            frame.pack(pady=5)
            self.frames[frame_name] = frame
            self.line()

    def styles(self):
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('Custom.TCheckbutton', background=self.default_color, foreground='white', selectcolor=self.default_color, activebackground=self.default_color, highlightthickness=0, activeforeground='white', font=("Bahnschrift", 10))

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Bahnschrift", 10), foreground=self.default_color, background=self.default_color, padding=-1)

        self.style = ttk.Style()
        self.style.configure("TCheckbutton", background=self.default_color, foreground='green', selectcolor=self.default_color, activebackground=self.default_color, highlightthickness=0, activeforeground='white', font=("Bahnschrift", 10))
    
    def on_antivirus_checkbox_changed(self):
        if self.apks_var["Antivírus"].get() == 1:
            self.apks_var["Small Office"].set(0)

    def on_smalloffice_checkbox_changed(self):
        if self.apks_var["Small Office"].get() == 1:
            self.apks_var["Antivírus"].set(0)

    def labels(self):
        # Create labels and buttons
        self.label_names = [name.upper() for name in self.frames_names]
        self.labels = {}

        for label_name, frame_name in zip(self.label_names, self.frames_names):
            label = tk.Label(self.frames[frame_name], text=label_name, font=("Bahnschrift", 13), bg=self.default_color, fg="white")
            label.pack(anchor="center")
            self.labels[frame_name] = label
    
    def apks_names_buttons(self):
        # Create checkboxes for application names
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
        #'download' Keep a reference to prevent garbage collection
        download = Download(self.apks_var,self.window, self.progress_bar_main, self.apks, self.download_button, self.instalando_label)
    
    def image_window(self, event=None):
        #'image' Keep a reference to prevent garbage collection
        image_window = tk.Toplevel(self.window)
        image = MainImage(image_window)
        
    def button(self):
        # Create download button and progress bar
        self.download_button = ttk.Button(self.window, text="BAIXAR APLICATIVOS", style="Custom.TButton", command=self.download_button_callback, takefocus=False)
        self.download_button.pack(anchor="center", pady=10)

        self.progress_bar_main = ttk.Progressbar(self.window, length=300, takefocus=False)

        self.instalando_label = tk.Label(self.window, text=" ", font=("Bahnschrift", 12), bg=self.default_color, fg="white")

        #self.instalar_botao = ttk.Button(self.window, text="INSTALAR APLICATIVOS", takefocus=False, style="Custom.TButton")
        # instalar_botao.pack(anchor='center', pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = MainFrame(window)
    window.mainloop()