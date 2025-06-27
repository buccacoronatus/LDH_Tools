from tkinter import *
from tkinter import messagebox, font
import pyperclip
import os

root = Tk()
root.title('2FA - TU Dresden')
#root.geometry('450x350')

default_font=font.nametofont('TkDefaultFont').configure(family='Segoe UI',size=14)
default_font=font.nametofont('TkTextFont').configure(family='Segoe UI',size=12)
default_font=font.nametofont('TkHeadingFont').configure(family='Segoe UI',size=12)

global nums
global x_box
global y_box
nums=''
insert_list=[]


def load_data():
    print('--attempting to load data')
    try: 
        print('--opening file--')
        with open('lists/list.txt', 'r', encoding='UTF-8') as f_handle:
            nums=f_handle.read()
        print('--found existing file')
        
    except:
        print('--no index list found')
        nums=''
    return(nums)    

def process(x_box,y_box,nums):
    print('--Retrieving Key')
    num_length=len(nums)
    print('--length:' + str(num_length) + ' ' + nums)
    try:
        x = int(x_box.get())
        y = int(y_box.get())
        if x > num_length or y > num_length or x==0 or y==0:
            messagebox.showerror(message='Bitte zwei Zahlen zwischen 1 und ' + str(num_length) +  ' eingeben')
            print('--wrong numbers')
        elif x <= num_length or y <= num_length:
            result= nums[x-1]+nums[y-1]
            pyperclip.copy(result)
            messagebox.showinfo(message='Zeichenfolge: \n' + result+'''\n...wurde in Zwischenablage kopiert''')
            print('--successfully copied to clipboard')
    except:
        if isinstance(x_box.get(), str) or isinstance(y_box.get(), str): 
            messagebox.showerror(message='Bitte nur Zahlen zwischen 1 und ' + str(num_length) + ' eingeben')
            print('--no number was entered')
        else:
            messagebox.showerror(message='Eingabefehler')
            print('--unclear user input mistake')
        return
    print('--processing')
    return


def Mainsequence():
    nums=load_data()
    print('--Initializing Main Sequence')
    print(nums)

    Label(root, text='Erste Zahl').grid(row=1, column=0, columnspan=15)
    x_box = Entry(root, width=5, borderwidth=5)
    x_box.grid(row=1, column=5, columnspan=15)
    Label(root, text='Zweite Zahl').grid(row=2, column=0, columnspan=15)
    y_box = Entry(root, width=5, borderwidth=5)
    y_box.grid(row=2, column=5, columnspan=15)
    Button(root, text='Klick mich', padx=20, pady=15, command=lambda:process(x_box,y_box,nums)).grid(row=3, column=5, columnspan=15)

    for i in range(25):
            Label(root, text=str(i+1)).grid(row=4, column=i)
            if nums=='':
                e=Entry(root, width=5, textvariable=StringVar())
            else:    
                try:e=Entry(root, width=5,textvariable=StringVar(value=nums[i]))
                except:e=Entry(root, width=5, textvariable=StringVar())
            e.grid(row=5, column=i) 
            insert_list.append(e)

    def save_file(nums):
        print('--attempting to save file')    
        nums=[e.get() for e in insert_list] 
        print(nums)
        os.makedirs('lists', exist_ok=True)
        with open('lists/list.txt', 'w', encoding='UTF-8') as file:
            file.write(''.join(nums))
        messagebox.showinfo(message='Zeichenfolge gespeichert')
        Mainsequence()

    Button(root, text='Index speichern', command=lambda:save_file(nums)).grid(row=6, column=5, columnspan=15)

Mainsequence()

mainloop()