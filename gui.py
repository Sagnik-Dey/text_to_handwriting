from tkinter import Image, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter import filedialog, messagebox
from tkinter import NW, INSERT, END, DISABLED, NORMAL
import pywhatkit
from PIL import Image, ImageTk
import threading 

class Window:
    def __init__(self):
        self.TITLE = "T2H"
        self.WIDTH = 598
        self.HEIGHT = 424
        self.LEFT = 200
        self.TOP = 100
        
        self.init_window()
        
    def init_window(self): 
        self.window = Tk()

        self.window.title(self.TITLE)
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.LEFT}+{self.TOP}")
        self.window.configure(bg = "#FFDDD2")
        self.window.resizable(False, False)
        
        self.init_window_widgets()
        
        self.window.mainloop()
        
    def init_window_widgets(self):
        self.canvas = Canvas(
            self.window,
            bg = "#FFDDD2",
            height = 424,
            width = 598,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            52.0,
            51.99999999999997,
            anchor="nw",
            text="T2H",
            fill="#D3649C",
            font=("Cinzel Decorative Black", 24 * -1)
        )

        self.canvas.create_rectangle(
            52.0,
            40.99999999999997,
            121.0,
            45.99999999999997,
            fill="#FFB9B9",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=("assets/frame0/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            293.5,
            198.49999999999997,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            bd=0,
            bg="#F0C0B0",
            fg="#000716",
            highlightthickness=0,
            font=("Montserrat", 8)
        )
        self.entry_1.place(
            x=63.0,
            y=141.99999999999997,
            width=461.0,
            height=111.0
        )

        self.entry_image_2 = PhotoImage(
            file=("assets/frame0/entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            351.0,
            342.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F0C0B0",
            fg="#000716",
            highlightthickness=0,
            cursor="target"
        )
        self.entry_2.place(
            x=173.0,
            y=327.0,
            width=356.0,
            height=29.0
        )

        self.canvas.create_text(
            52.0,
            89.99999999999997,
            anchor="nw",
            text="A Simple App that converts text to handwriting",
            fill="#DE74AA",
            font=("Montserrat Regular", 11 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=("assets/frame0/button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.convert_text_to_img,
            relief="flat"
        )
        self.button_1.place(
            x=52.0,
            y=278.0,
            width=202.0,
            height=31.0
        )

        self.button_image_2 = PhotoImage(
            file=("assets/frame0/button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_img,
            relief="flat",
            state=DISABLED
        )
        self.button_2.place(
            x=52.0,
            y=327.0,
            width=104.0,
            height=31.0
        )

        self.button_image_3 = PhotoImage(
            file=("assets/frame0/button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_txt_file,
            relief="flat"
        )
        self.button_3.place(
            x=285.0,
            y=277.0,
            width=250.0,
            height=31.0
        )

        self.canvas.create_rectangle(
            0.0,
            400.0,
            598.0,
            424.0,
            fill="#D79797",
            outline="")
        
        self.canvas.create_text(
            13.0,
            405.0,
            anchor="nw",
            text="Status : ",
            fill="#000000",
            font=("Montserrat Regular", 11 * -1)
        )

        self.status_lb = self.canvas.create_text(
            68.0,
            405.0,
            anchor="nw",
            text="App Loaded",
            fill="#000000",
            font=("Montserrat Regular", 11 * -1)
        )
        
    def convert_text_to_img(self):
        self.thread1 = threading.Thread(target=self.convert_text_to_image)
        self.thread1.start()
        
        self.thread2 = threading.Thread(target=self.check_alive)
        self.thread2.start()
        
    def convert_text_to_image(self):
        self.text_entered = self.entry_1.get(1.0, END)
        if self.text_entered == "\n":
            self.entry_2.delete(0, END)
            self.canvas.itemconfig(
                self.status_lb, text="There should be some text to convert")
            messagebox.showerror("Error", "There should be some text to convert")         
            return
        else:
            self.save_file = filedialog.asksaveasfile(initialfile='Untitled.png',
                                                      defaultextension=".png", filetypes=[("Image", "*.png")])
            pywhatkit.text_to_handwriting(
                self.text_entered, save_to=str(self.save_file.name))
            self.entry_2.delete(0, END)
            self.entry_2.insert(0, self.save_file.name)
            self.button_2["state"] = NORMAL
        
    def open_txt_file(self):
        self.open_file = filedialog.askopenfile(
            mode="r", filetypes=[("Text Documents", "*.txt"), ("All Files", "*")])
        if self.open_file is not None:
            self.entry_1.delete(1.0, END)
            self.content = self.open_file.read()
            self.entry_1.insert(INSERT, self.content)
            self.canvas.itemconfig(self.status_lb, text=f"Opened .txt file - {self.open_file.name}")
            
    def open_img(self):
        self.img_window = Toplevel(self.window)
        self.img_window.title("Image")
        self.img_window.geometry("800x450+100+100")
        
        canvas2 = Canvas(self.img_window, width = 750, height = 400)
        canvas2.pack()
        image_ = Image.open(self.entry_2.get())
        image_ = image_.resize((750, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image_)
        canvas2.create_image(20,20, anchor=NW, image=img)

        self.img_window.mainloop()
    
    def check_alive(self):
        self.canvas.itemconfig(
            self.status_lb, text="Text is converting to image.......")
        while True:
            if self.thread1.is_alive() == False:
                self.canvas.itemconfig(
                    self.status_lb, text="Successfully converted into image")
                break
        if self.entry_2.get() == "":
            self.canvas.itemconfig(
                self.status_lb, text="There should be some text to convert")
            
if __name__ == "__main__":
    window = Window()
