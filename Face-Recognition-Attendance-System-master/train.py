import cv2
from cgitb import text
from logging import exception
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import meanShift
import mysql.connector
from mysql.connector import cursor
from numpy import delete, imag
import os
import numpy as np


class Train:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")


        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("sans-serif",35,"bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        img_top = Image.open(r"Images\train.jpg")
        img_top = img_top.resize((1500,300),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=105,width=1530,height=300)

        #Button
        b1 = Button(self.root, text="TRAIN  DATA", command=self.train_classifier,cursor="hand2", font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1.place(x=12, y=405, width=1500, height=70)

        img_bottom = Image.open(r"Images\train1.webp")
        img_bottom = img_bottom.resize((1500,300),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=480,width=1530,height=300)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  #grey scale image        
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
        
