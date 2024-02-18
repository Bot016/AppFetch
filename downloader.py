import os
import wget
import tkinter as tk
from tkinter import filedialog

# Import Class
from link import links

class Download:

    def __init__(self, apks_var, window, progress_bar, apks_names, download_button, instalando_label):
        # Create arrays and store information from variables
        self.apk_name = []
        self.apk_var = []
        self.apk_def = []
        self.window = window # Reference to the Tkinter window
        self.porcentagem = tk.IntVar() # Variable to track download progress
        self.apks = apks_names # Dictionary containing APK names as keys and Checkbutton widgets as values
        for apk_name, apk_var in apks_var.items():
            self.apk_name.append(apk_name) 
            self.apk_var.append(apk_var)
            formatted_name = apk_name.replace(" ", "_")
            formatted_name = formatted_name.replace("7", "")
            self.apk_def.append(formatted_name)
        
        # Process APK information and select output folder
        output_folder = self.select_output_folder()
        if output_folder:
            # Main frame setings
            download_button.pack_forget()
            instalando_label.pack(anchor='center')
            self.window.geometry("320x485")
            progress_bar.pack(pady=10)
            progress_bar.config(variable=self.porcentagem)
            # If download again, back Labels to default color
            for i in self.apks:
                self.apks[i].config(style="TCheckbutton")
            self.window.update()

            # Start find links and download
            self.list_download()
            instalando_label.config(text="Obtendo Links...", fg="green")
            self.window.update()
            self.get_link()
            instalando_label.config(text="Baixando...", fg="green")
            self.window.update()
            self.download(output_folder)

            # After download back button
            progress_bar.pack_forget()
            instalando_label.pack_forget()
            self.window.geometry("320x463")
            download_button.pack(anchor="center", pady=10)
            self.window.update()

    def select_output_folder(self):
        # Open a file dialog to select the output folder
        self.window.update()
        output_folder = filedialog.askdirectory()
        return output_folder
        
    def list_download(self):
        # Process selected APKs and update lists
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
        # Call functions to get links
        for i in range(len(self.apk_function)):
            self.apk_function[i] = self.apk_function[i]()
    
    def download(self, output_folder):
        # Download selected APKs
        path_folder = output_folder
        for i in range(len(self.apk_function)):
            self.porcentagem.set(0)
            output_folder = os.path.join(path_folder, self.apk_name[i] + ".exe")
            try:
                # Download APK using wget and update progress bar
                wget.download(self.apk_function[i], out=output_folder, bar=self.progress_bar)
                # Update the Checkbutton style if download archive
                self.apks[self.apk_name[i]].config(style="Green.TCheckbutton")
                self.window.update()
            except:
                # Update the Checkbutton style to red if archive don't download
                self.apks[self.apk_name[i]].config(style="Red.TCheckbutton")
                self.window.update()
            
            
        
    def progress_bar(self, current, total, width=80):
        progresso = current / total
        self.porcentagem.set(int(progresso * 100))
        self.window.update()
    
