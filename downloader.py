from tkinter import filedialog

class Download:
    def __init__(self, apks_var, output_folder):
        self.output_folder = output_folder
        self.apk_name = []
        self.apk_var = []
        for apk_name, apk_var in apks_var.items():
            self.apk_name.append(apk_name) 
            self.apk_var.append(apk_var)
    