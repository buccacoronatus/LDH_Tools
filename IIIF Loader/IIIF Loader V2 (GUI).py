from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os


root = Tk()
root.title('IIF Loader')
root.geometry('800x600')

global metadata
metadata=''
global url
url=''
global my_image
my_image=''

# default_font=font.nametofont('TkDefaultFont').configure(family='Segoe UI',size=16)
# default_font=font.nametofont('TkTextFont').configure(family='Segoe UI',size=16)
# default_font=font.nametofont('TkHeadingFont').configure(family='Segoe UI',size=16)

# default_font.configure(size=18)


def connect(url):
    print('--attempting to connect to:', url.get())
    return


def fetch_manifest(url):
    print('--fetching manifest')
    return


def save():
    print('--attempting to save pages', first_page.get(), ' - ', last_page.get())
    
    if first_page.get() or last_page.get()=='':
        print('--missing number')
        messagebox.showinfo(message='missing number')
        Mainroutine()
    elif int(first_page.get())==0:
        print('--entered first:0')
        messagebox.showinfo(message='wrong number')
        Mainroutine()
    elif int(last_page.get())==0:
        print('--entered last:0')
        messagebox.showinfo(message='wrong number')
        Mainroutine()
    elif int(first_page.get())<int(last_page.get()):
        print('--last smaller than first')
        messagebox.showinfo(message='wrong numbers')
        Mainroutine()



    # folder_path = "my_data_folder"
    # os.makedirs(folder_path, exist_ok=True)

    # file_path = os.path.join(folder_path, "data.txt")
    # with open(file_path, "w") as file:
    #     file.write("Hello, this is some stored data.")


def open_images():
    print('--attempting to open image')

    # root.filename = filedialog.askopenfilename(
    #     initialdir = 'E:\Googledrive\IT Lernen\Learn Tkinter\images', title='Select A File', 
    #     filetypes = (('jpg files','*.jpg'), ('all files', '*.*'))
    #     )
    # my_image = ImageTk.PhotoImage(Image.open(root.filename))
    # my_image_Label = Label (image=my_image).pack()
    # my_Label = Label(root, text=root.filename).pack()
    return


def Mainroutine():
    global first_page 
    global last_page
    Label(root, text="IIF and METS Loader").grid(row=0, column=0, columnspan=5)
    url = Entry(root, text=' ')
    url.grid(row=1, column=0, columnspan=5)

    Button(root, text='Connect', command=lambda:(connect(url))).grid(row=2, column=0, columnspan=5)

    Label(root, text='metadata').grid(row=3, column=0, columnspan=5)


    Label(root, text='from:').grid(row=4, column=0, columnspan=1)
    first_page = Entry(root, text='from page:')
    first_page.grid(row=5, column=0)

    Label(root, text='to:').grid(row=4, column=1, columnspan=1)
    last_page = Entry(root, text='to page:')
    last_page.grid(row=5, column=1)

    Button(root, text='Save file', command=save).grid(row=6, column=0, columnspan=5)

Mainroutine()
root.mainloop()
