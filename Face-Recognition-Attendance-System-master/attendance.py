import cv2
from cgitb import text
from logging import exception
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import meanShift
import mysql.connector
from mysql.connector import cursor
from numpy import delete
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")


        # variables
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()



        # first img
        img = Image.open(r"Images\atten1.webp")
        img = img.resize((800,250),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=250)

        # seccond img
        img1 = Image.open(r"Images\atten2.jpg")
        img1 = img1.resize((800,250),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=250)

        title_lbl = Label(self.root, text="ATTENDANCE  MANAGMENT  SYSTEM", font=("sans-serif",35,"bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=250, width=1530, height=50)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20,y=300,width=1480, height=480)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white" ,relief=RIDGE, text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=740,height=460)

        img_left = Image.open(r"Images\attendance.jpeg")
        img_left = img_left.resize((730,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=100)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=105,width=730, height=300)

        # labels and entry
        #attendance id
        attendannceId_label = Label(left_inside_frame, text="Attendance Id:", font=("times new roman",13,"bold"), bg="white")
        attendannceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendannceId_label = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendannceId_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #name
        name_label = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        name_label.grid(row=0, column=2, padx=40, pady=8)

        atten__name = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name ,font="comicsansns 11 bold")
        atten__name.grid(row=0, column=3, pady=8)

        #Department
        dep_label = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        dep_label.grid(row=1, column=0, padx=10, pady=8)

        atten__dep = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep ,font="comicsansns 11 bold")
        atten__dep.grid(row=1, column=1, padx=10,pady=8)

        #Time
        time_label = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        time_label.grid(row=1, column=2, padx=40, pady=8)

        atten__time = ttk.Entry(left_inside_frame,width=22, textvariable=self.var_atten_time ,font="comicsansns 11 bold")
        atten__time.grid(row=1, column=3, pady=8)

        #Date
        date_label = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        date_label.grid(row=2, column=0, padx=10, pady=8)

        atten__date = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date, font="comicsansns 11 bold")
        atten__date.grid(row=2, column=1, padx=10,pady=8)

        #attendacne
        attendance_label = Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold")
        attendance_label.grid(row=3, column=0)

        self.attendance_combo = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold", state="readonly")
        self.attendance_combo["values"] = ("Statuts","Present","Absent")
        self.attendance_combo.grid(row=3, column=1, pady=8)
        self.attendance_combo.current(0)

        #buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=260, width=705, height=35)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCSV ,width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv,width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update",width=17,font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white" ,relief=RIDGE, text="Attendance Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=5,width=720,height=460)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=420)

        # scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)


    # fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSF File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)



    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
        
