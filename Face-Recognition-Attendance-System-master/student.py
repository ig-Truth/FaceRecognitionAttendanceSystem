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


class Student:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_session=StringVar()
        self.var_semester=StringVar()
        self.var_admNo=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_pincode=StringVar()


        # bg image
        img = Image.open(r"Images\bg_img.webp")
        img = img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(bg_img, text="STUDENT  MANAGMENT  SYSTEM", font=("sans-serif",35,"bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20,y=120,width=1480, height=620)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white" ,relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left = Image.open(r"Images\student_details.jpg")
        img_left = img_left.resize((730,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=130)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white" ,relief=RIDGE, text="Current course information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=730,height=130)

        # department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman",13,"bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep ,font=("times new roman",13,"bold") , state="readonly", width=27)
        dep_combo["values"] = ("Select Department","Computer Science Engineering","Electronics and Electrical Engineering","Mechanical Engineering","Electrical Engineering","Civil Engineering","Chemical Engineering", "Petroleum Engineering", "Mining Engineering", "Metallurgical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # session year
        sess_year_label = Label(current_course_frame, text="Session Year", font=("times new roman",13,"bold"), bg="white")
        sess_year_label.grid(row=0, column=2, padx=10, sticky=W)

        sess_year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman",13,"bold") , state="readonly", width=20)
        sess_year_combo["values"] = ("Select Session Year","2020-21","2021-22","2022-23")
        sess_year_combo.current(0)
        sess_year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # session
        session_label = Label(current_course_frame, text="Session", font=("times new roman",13,"bold"), bg="white")
        session_label.grid(row=1, column=0, padx=10, sticky=W)

        session_combo = ttk.Combobox(current_course_frame, textvariable=self.var_session,font=("times new roman",13,"bold") , state="readonly", width=20)
        session_combo["values"] = ("Select Session","Monsoon","Winter")
        session_combo.current(0)
        session_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semster
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman",13,"bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,font=("times new roman",13,"bold") , state="readonly", width=20)
        semester_combo["values"] = ("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student personal information
        student_personal_frame = LabelFrame(Left_frame, bd=2, bg="white" ,relief=RIDGE, text="Student Personal information", font=("times new roman",12,"bold"))
        student_personal_frame.place(x=5,y=265,width=730,height=290)

        # Admission number
        admNo_label = Label(student_personal_frame, text="Admission Number:", font=("times new roman",13,"bold"), bg="white")
        admNo_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        admNo_entry = ttk.Entry(student_personal_frame,textvariable=self.var_admNo,width=20,font=("times new roman",13,"bold"))
        admNo_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        name_label = Label(student_personal_frame, text="Student Name:", font=("times new roman",13,"bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(student_personal_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Student Branch
        branch_label = Label(student_personal_frame, text="Department:", font=("times new roman",13,"bold"), bg="white")
        branch_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        branch_entry = ttk.Entry(student_personal_frame,width=20,font=("times new roman",13,"bold"))
        branch_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # gender
        gender_label = Label(student_personal_frame, text="Gender:", font=("times new roman",13,"bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_personal_frame, textvariable=self.var_gender,font=("times new roman",13,"bold") , state="readonly", width=18)
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # DOB
        dob_label = Label(student_personal_frame, text="Date of Birth:", font=("times new roman",13,"bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(student_personal_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # email
        email_label = Label(student_personal_frame, text="Email:", font=("times new roman",13,"bold"), bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(student_personal_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # phone
        phone_label = Label(student_personal_frame, text="Phone:", font=("times new roman",13,"bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(student_personal_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(student_personal_frame, text="Address:", font=("times new roman",13,"bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(student_personal_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # pincode
        pincode_label = Label(student_personal_frame, text="Pincode:", font=("times new roman",13,"bold"), bg="white")
        pincode_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        pincode_entry = ttk.Entry(student_personal_frame,textvariable=self.var_pincode,width=20,font=("times new roman",13,"bold"))
        pincode_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_personal_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(student_personal_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # buttons frame
        btn_frame = Frame(student_personal_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=200, width=705, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data,width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data,width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(student_personal_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame1.place(x=10, y=235, width=705, height=35)

        takephoto_btn = Button(btn_frame1,command=self.generate_dataset ,text="Take Photo Sample", width=35 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=0, column=0)

        updatephoto_btn = Button(btn_frame1, text="Update Photo Sample", width=35 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=0, column=1)



        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white" ,relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=710,height=580)

        img_right = Image.open(r"Images\student_details.jpg")
        img_right = img_right.resize((730,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=730, height=130)


        # Search System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white" ,relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700,height=90)

        search_label = Label(search_frame,text="Search By:", font=("times new roman",15,"bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # self.var_com_search = StringVar()

        search_combo = ttk.Combobox(search_frame , font=("times new roman",13,"bold") , state="readonly", width=15)
        search_combo["values"] = ("Select","Admission_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame ,text="Search", width=12 ,font=("times new roman",12,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame ,text="Show All", width=12 ,font=("times new roman",12,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white" ,relief=RIDGE)
        table_frame.place(x=5,y=230,width=700,height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep","year","session","semester","admissionNo","name","gender","phone","dob","email","address","pincode","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Session_Year")
        self.student_table.heading("session", text="Session")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("admissionNo", text="Admission_No")
        self.student_table.heading("name", text="Student_Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone_No")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("pincode", text="Pincode")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("session", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("admissionNo", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("pincode", width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # functions

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_admNo.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_session.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_admNo.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_pincode.get(),
                                                                                                            self.var_radio1.get()

                                                                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
        
    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_session.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_admNo.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_address.set(data[10]),
        self.var_pincode.set(data[11]),
        self.var_radio1.set(data[12])                                                                                                   


    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_admNo.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update details?", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, year=%s, session=%s, semester=%s, name=%s, gender=%s, phone=%s, dob=%s, email=%s, address=%s, pincode=%s, photoSample=%s where admNo=%s", (
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_session.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_pincode.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_admNo.get()
                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_admNo.get()=="":
            messagebox.showerror("Error","Student Admission Number must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where admNo=%s"
                    val = (self.var_admNo.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)


    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Session Year")
        self.var_session.set("Select Session")
        self.var_semester.set("Select Semester")
        self.var_admNo.set("")
        self.var_name.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_pincode.set("")



    # Gennerate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_admNo.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s, year=%s, session=%s, semester=%s, name=%s, gender=%s, phone=%s, dob=%s, email=%s, address=%s, pincode=%s, photoSample=%s where admNo=%s", (
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_session.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_pincode.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_admNo.get() == id+1
                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # load predefined data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor = 1.3
                    #minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)


    # search data
    # def search_data(self):
    #     if self.var_com_search.get()=="" or self.var_search.get()=="":
    #         messagebox.showerror("Error", "Please select option")
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", username="root", password="@#shashank123", database="face_recognizer")
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
    #             rows = my_cursor.fetchall()
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 conn.commit()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
        
