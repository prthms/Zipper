# Developed by Prathamesh kumar sah
# Date : 19/6/2021
# This is use to zip or unzip the files.

from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
from zipfile import ZipFile,ZIP_DEFLATED
from datetime import datetime
from os import chdir

root = Tk()
root.title("Zip Files Converter")
root.iconbitmap("Images/app.ico")
root.geometry("450x450+430+10")
root.resizable(0,0)


# functions
def zip_the_file():
    global zip_but_val
    zip1.config(bg='steel blue')
    unzip1.config(bg='deep sky blue')
    textvariable1.set('')
    textvariable2.set('')
    zip_but_val = 0


def unzip_the_file():
    global zip_but_val
    zip1.config(bg='deep sky blue')
    unzip1.config(bg='steel blue')
    textvariable1.set('')
    textvariable2.set('')
    zip_but_val = 1

def open_file_toread():
    global selected_file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
    textvariable1.set('Selected File : '+file)
    selected_file = file
    get_info_zip(file)

def get_info_zip(filename):
    if filename.split('.')[1] == "zip":
        with ZipFile(filename,'r') as zip:
            for info in zip.infolist():
                textfield.insert(1.0,"\nFile Name : "+info.filename+"\n\tModified:\t"+str(datetime(*info.date_time))+'\n\tOriginal Size:\t'+str(info.file_size)+' bytes\n'+"\tCompressed:\t"+str(info.compress_size)+' bytes\n')


def open_file_tosave():
    global saved_file
    file = askdirectory()
    textvariable2.set('Save To : '+file)
    saved_file = file

def convert_to_zip():
    global selected_file, saved_file
    filename1 = selected_file.split('.')[0]+'.zip'
    filename_zip = filename1.split("/")
    filename_zip_lenght = len(filename1.split("/"))-1
    last_filename = saved_file+'/'+filename_zip[filename_zip_lenght]
    print("filename: : ", last_filename)
    examplezip = ZipFile(last_filename,'w') #
    examplezip.write(selected_file,compress_type=ZIP_DEFLATED)
    examplezip.close()

def convert_to_unzip():
    global selected_file,saved_file
    file_name = selected_file
    
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        print('Extracting all the files now...')
        chdir(saved_file)
        zip.extractall()
        print('Done!')
def select_right_function():
    global zip_but_val
    print(textvariable1)
    print('value:',zip_but_val)
    if zip_but_val == 0:
        convert_to_zip()
    else:
        convert_to_unzip()

    # Elements
# variable
selected_file = ""
saved_file = ""
textvariable1 = StringVar()
textvariable2 = StringVar()
zip_but_val = 0

# first row
zip1 = Button(root,text="ZIP",bg='steel blue', fg='white', font=10, border=0,width=20,command=zip_the_file)
zip1.grid(row=0,column=0)
unzip1 = Button(root,text="UnZip",bg='deep sky blue', fg='white', font=10, border=0,width=20,command=unzip_the_file)
unzip1.grid(row=0,column=1)

# second row
label1 = Label(root,text="Select File/Folder : ",pady=10,fg="indian red",font=8,)
label1.grid(row=2,column=0)
entry1 = Label(root,textvariable=textvariable1,pady=10,fg="sea green")
entry1.grid(row=3,column=0,columnspan=4)
browes_but = Button(root,text="Select File/Folder",bg='lime green', fg='white', font=7, border=0,command=open_file_toread)
browes_but.grid(row=2,column=1)

# third row
label2 = Label(root,text="Save To : ",pady=15,fg="indian red",font=8,)
label2.grid(row=4,column=0)
entry2 = Label(root,textvariable=textvariable2,pady=10,fg="sea green")
entry2.grid(row=5,column=0,columnspan=4)
save_but = Button(root,text="Save To",bg='lime green', fg='white', font=7, border=0,command=open_file_tosave)
save_but.grid(row=4,column=1)

# Fourth row
textfield = Text(root,width=60,height=12,font="calibri 11",cursor="arrow",fg="green4")
textfield.grid(row=6,column=0,columnspan=4)

# fifth row
finalbutton = Button(root,text="Start",bg='spring green', fg='dim gray', font=15, border=0,width=30,command=select_right_function)
finalbutton.grid(row=7,column=0,columnspan=4)

root.mainloop()