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
            formatted_name = apk_name.replace("7", "")
            self.apk_def.append(formatted_name)
        self.output_folder = self.select_output_folder()
        if self.output_folder:
            self.list_download()
            self.get_link()

    def select_output_folder(self):
        #instalado_label.config(text=" ", fg="white") 
        self.window.geometry("320x463")
        self.window.update()
        output_folder = filedialog.askdirectory()
        return output_folder
        
    def list_download(self):
        self.apk_function = []
        for apk_def, apk_var in zip(self.apk_def, self.apk_var):
            if apk_var.get() == 1:
                apk_function = getattr(links, apk_def, None)
                if apk_function is not None and callable(apk_function):
                    self.apk_function.append(apk_function)
                   
    def get_link(self):
        for i in range(len(self.apk_function)):
            self.apk_function[i] = self.apk_function[i]()
        #use threading or concurrent.futures 
        print(self.apk_function)
    