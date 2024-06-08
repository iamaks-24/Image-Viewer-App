from tkinter import  *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer App")

# defining width n height
width,height=1000,500

# The Image.ANTIALIAS filter is used to make the resized image look smooth.-->to maintain the quality after resizing
# Image.LANCZOS in the updated versions of the library (Pillow, the friendly PIL fork).

my_img1=ImageTk.PhotoImage(Image.open("images/1.jpg").resize((width,height),Image.LANCZOS))
my_img2=ImageTk.PhotoImage(Image.open("images/2.jpg").resize((width,height),Image.LANCZOS))
my_img3=ImageTk.PhotoImage(Image.open("images/3.jpg").resize((width,height),Image.LANCZOS))
my_img4=ImageTk.PhotoImage(Image.open("images/4.jpg").resize((width,height),Image.LANCZOS))
my_img5=ImageTk.PhotoImage(Image.open("images/5.jpg").resize((width,height),Image.LANCZOS))
my_img6=ImageTk.PhotoImage(Image.open("images/6.jpg").resize((width,height),Image.LANCZOS))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

# status bar
status=Label(root,text="Image 1 of "+str(len(image_list)),bg="#cccccc",bd=1,relief=SUNKEN,anchor=E) #anchor to keep the text at right #sunken to get the depth around text #border - bd

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)


def forward(img_no):
    global my_label
    global button_back
    global button_front

    my_label.grid_forget()#removes the existing image as clicked forward
    my_label=Label(image=image_list[img_no-1])#-1 coz,list indexing starts from 0
    button_front=Button(root,text=">>",bg="grey",command=lambda: forward(img_no+1))
    button_back=Button(root,text="<<",bg="grey",command=lambda: backward(img_no-1))

    status=Label(root,text="Image " + str(img_no) + " of "+str(len(image_list)),bg="#cccccc",bd=1,relief=SUNKEN,anchor=E)

    # if last image then disable forward icon
    if img_no==6:
        button_front=Button(root,text=">>",state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_front.grid(row=1,column=2)

    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def backward(img_no):
    global my_label
    global button_back
    global button_front

    my_label.grid_forget()
    my_label=Label(image=image_list[img_no-1])#-1 coz,list indexing starts from 0
    button_front=Button(root,text=">>",bg="grey",command=lambda: forward(img_no+1))
    button_back=Button(root,text="<<",bg="grey",command=lambda: backward(img_no-1))
    status=Label(root,text="Image " + str(img_no) + " of "+str(len(image_list)),bg="#cccccc",bd=1,relief=SUNKEN,anchor=E)

    if img_no==1:
        button_back=Button(root,text="<<",state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_front.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

    


button_back=Button(root,text="<<",bg="grey",command=backward,state=DISABLED)#we r not passing any thing at initial stage coz,as the app launches it vl be on first image,where v cant go backward
button_exit=Button(root,text="exit program",bg="grey",command=root.quit)
button_front=Button(root,text=">>",bg="grey",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_front.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

# grid system has some navigation type system (south-below,north-above,east E,west W)
root.mainloop()