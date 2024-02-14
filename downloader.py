import os
import wget
from tkinter import filedialog
from link import links

class Download:
    def __init__(self, apks_var, window):
        self.apk_name = []
        self.apk_var = []
        self.apk_def = []
        self.window = window
        for apk_name, apk_var in apks_var.items():
            self.apk_name.append(apk_name) 
            self.apk_var.append(apk_var)
            formatted_name = apk_name.replace(" ", "_")
            formatted_name = formatted_name.replace("7", "")
            self.apk_def.append(formatted_name)
        output_folder = self.select_output_folder()
        if output_folder:
            self.list_download()
            self.get_link()
            self.download(output_folder)

    def select_output_folder(self):
        #instalado_label.config(text=" ", fg="white") 
        self.window.geometry("320x463")
        self.window.update()
        output_folder = filedialog.askdirectory()
        return output_folder
        
    def list_download(self):
        self.apk_function = []
        apk_nomes = []
        for i, (apk_def, apk_var) in enumerate(zip(self.apk_def, self.apk_var)):
            if apk_var.get() == 1:
                apk_nomes.append(self.apk_name[i])
                apk_function = getattr(links, apk_def, None)
                if apk_function is not None and callable(apk_function):
                    self.apk_function.append(apk_function)
        self.apk_name.clear()
        self.apk_name = apk_nomes
                   
    def get_link(self):
        for i in range(len(self.apk_function)):
            self.apk_function[i] = self.apk_function[i]()
    
    def download(self, output_folder):
        path_folder = output_folder
        for i in range(len(self.apk_function)):
            output_folder = os.path.join(path_folder, self.apk_name[i] + ".exe")
            wget.download(self.apk_function[i], out=output_folder)

    
