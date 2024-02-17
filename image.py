import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MainImage:
    
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.parent_window.title("Clicou por que?")
        self.parent_window.resizable(False, False)

        # Image Url
        image_url = "https://cdn.discordapp.com/attachments/894746176375623690/1208525183623888988/image.png?ex=65e399c9&is=65d124c9&hm=398f7c166eb8c15f1007938f084c09d11860a4c281fbbb56927681ca1ac9417a&"

        # Download image
        response = requests.get(image_url)
        image_data = response.content

        # Load image using Pillow (PIL)
        example_image = Image.open(BytesIO(image_data))
        
        # Resize image
        resized_image = example_image.resize((400, 300), Image.LANCZOS)

        # Convert image to Tkinter PhotoImage
        MainImage.image_reference = ImageTk.PhotoImage(resized_image)

        # Create new Canvas for image
        self.canvas = tk.Canvas(self.parent_window)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Create image in Canvas on position (0,0) and anchor in NW
        # The image is loaded from MainImage.image_reference
        self.canvas.create_image(0, 0, anchor=tk.NW, image=MainImage.image_reference)