import imp
import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # bg image
        img = Image.open(r"Images\bg_img.webp")
        img = img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, height=1080)
        #

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  PORTAL", font=("sans-serif",35,"bold"), bg="light blue", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        # student button
        img1 = Image.open(r"Images\student.jpg")
        img1 = img1.resize((220,220),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img, image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=120,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=200,y=320,width=220,height=40)

        # Detect face button
        img2 = Image.open(r"Images\face_detector.webp")
        img2 = img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img, image=self.photoimg2,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=120,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=600,y=320,width=220,height=40)

        # Attendance face button
        img3 = Image.open(r"Images\attendance.jpeg")
        img3 = img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image=self.photoimg3,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=120,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=1000,y=320,width=220,height=40)

        # Train face button
        img4 = Image.open(r"Images\train_data.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=200,y=650,width=220,height=40)

        # View Photos
        img5 = Image.open(r"Images\view_photos.png")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="View Photos",cursor="hand2",command=self.open_img,font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=600,y=650,width=220,height=40)

        # Exit Portal
        img6 = Image.open(r"Images\exit.webp")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit Portal",cursor="hand2",command=self.iExit,font=("sans-serif",15,"bold"), bg="blue", fg="white")
        b1_1.place(x=1000,y=650,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Exit the project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #Function buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
        