from distutils.command.config import config
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
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("sans-serif",35,"bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        img_top = Image.open(r"Images\recognize.jpg")
        img_top = img_top.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=100,width=1530,height=630)

        # Button
        b1 = Button(f_lbl, text="Face Recognizer", command=self.face_recog,cursor="hand2", font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1.place(x=1200, y=450, width=200, height=40)

    # attendance
    def mark_attendance(self,i,n,r):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist = f.readlines()
            name_list=[]
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{dtString},{d1},Present")

    
    # face recognition

    def face_recog(self):
        def draw_boundary(img,classifier,sacleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,sacleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where admNo="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Dep from student where admNo="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select admNo from student where admNo="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                
                if confidence>75:
                    cv2.putText(img,f"Admission No:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2) 

                coord = [x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
        
