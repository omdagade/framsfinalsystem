from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog
import os
import cv2

import mysql.connector
from mysql.connector import Error
import time

project_name = "Attendance System"




from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
import generate_new_attendance_sheet
import Take_attendance

from Take_attendance import train_dataset

########################################################################################



def start_GUI():
    GUI_page = Tk()
    GUI_page.geometry("1350x690+0+0")
    GUI_page.configure(background="#ffffff")

    global B_color
    global F_color
    B_color = "#FFFFFF"
    F_color = "#000000"

    #textbox = tk.Entry(GUI_page)
    
    #textbox.place(x = 250,y = 325 ,height=30, width=350)

    def select_subject():
        new_window1 = tk.Toplevel(GUI_page)
        new_window1.title("Select Subject")
        new_window1.geometry("300x400")
        def on_radio_button_change():
            radiostr=selected_radio.get()
            subradiodict={1:"Cloud Computing",2:"Machine Learning",3:"Data Science",4:"Web Technology"}

            if(radiostr!=""):
                Take_attendance.take(subradiodict[radiostr])
                
                
            

        selected_radio = tk.IntVar()
        radio_button1 = tk.Radiobutton(new_window1, text="Cloud Computing", variable=selected_radio, value=1, command=on_radio_button_change)
        radio_button1.place(x=100,y=100)

        radio_button2 = tk.Radiobutton(new_window1, text="Machine Learning", variable=selected_radio, value=2, command=on_radio_button_change)
        radio_button2.place(x=100,y=150)

        radio_button3 = tk.Radiobutton(new_window1, text="Data Science", variable=selected_radio, value=3, command=on_radio_button_change)
        radio_button3.place(x=100,y=200)

        radio_button4 = tk.Radiobutton(new_window1, text="Web Technology", variable=selected_radio, value=4, command=on_radio_button_change)
        radio_button4.place(x=100,y=250)

    
    def add_student():
        new_window = tk.Toplevel(GUI_page)
        new_window.title("Add Student")
        new_window.geometry("300x400")

        
        textbox1 = tk.Entry(new_window)
        textbox1.insert(0,"Enter Id")
        textbox1.pack(pady=10)

        textbox2 = tk.Entry(new_window)
        textbox2.insert(0,"Enter Name")
        textbox2.pack(pady=10)

        textbox3 = tk.Entry(new_window)
        textbox3.insert(0,"Enter Branch")
        textbox3.pack(pady=10)

        textbox4 = tk.Entry(new_window)
        textbox4.insert(0,"Enter Year")
        textbox4.pack(pady=10)

        textbox5 = tk.Entry(new_window)
        textbox5.insert(0,"Enter Parents Email")
        textbox5.pack(pady=10)

        
        submit_button = tk.Button(new_window, text="Add Student", command=lambda: on_submit(textbox1.get(), textbox2.get(), textbox3.get(), textbox4.get(), textbox5.get()))
        submit_button.pack(pady=10)
    
    def on_submit(value1,value2,value3,value4,value5):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="frams")
        print(myconn)
        mycursor = myconn.cursor()
        if(value1!="Enter Id" and value5!="Enter Parents Email" and value2!="Enter Name" and value3!="Enter Branch" and value4!="Enter Year"):
            directory = value1
                 
            parent_dir = "D:/face recognition attendance monitoring system/data"
            path = os.path.join(parent_dir, directory)    
            os.makedirs(path)

            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            save_path = os.path.join(path,value1+".png") 
            
            while(result):
                ret,frame = videoCaptureObject.read()
                imagename=save_path
                cv2.imshow('frame',frame)
                if cv2.waitKey(1)== ord("q"):
                    cv2.imwrite(imagename,frame)
                    result=False
                    #textbox1.insert(0,"Student Added Successfully-: ")
                    
                    mycursor.execute(f"CREATE TABLE {value1} (subject VARCHAR(255), date varchar(255));")
                    mycursor.execute(f"INSERT INTO studentdetails values('{value1}','{value1}','{value2}','{value3}','{value4}','{value5}');")
                    myconn.commit()
            
            videoCaptureObject.release()
            cv2.destroyAllWindows()  



    def LOGIN():

        def take_attendance(subjectstr):
            print('Take Attendance')
            



        def generate_sheet():
            print('Generate ')
            generate_new_attendance_sheet.generate()
            
        label2 = Label(GUI_page, text=project_name)
        label2.configure(background=B_color)
        label2.configure(foreground=F_color)
        label2.config(font=("Times new roman", 25))
        label2.place(x = 25,y=20,height=40, width=1300)


        


        

        B1 = Button(GUI_page, text = "Take Attendance", command = select_subject)
        B1.place(x = 250,y = 450 ,height=100, width=350)
        B1.configure(background="#808080")
        B1.configure(foreground=F_color)
        B1.config(font=("Times new roman", 25))

        B3 = Button(GUI_page, text = "Train", command = train_dataset)
        B3.place(x = 750,y = 250 ,height=100, width=350)
        B3.configure(background="#808080")
        B3.configure(foreground=F_color)
        B3.config(font=("Times new roman", 25))

        B4 = Button(GUI_page, text = "Add Student", command = add_student)
        B4.place(x = 250,y = 250 ,height=100, width=350)
        B4.configure(background="#808080")
        B4.configure(foreground=F_color)
        B4.config(font=("Times new roman", 25))
        
        

        B1 = Button(GUI_page, text = "Generate New Sheet", command = generate_sheet)
        B1.place(x = 750,y = 450 ,height=100, width=350)
        B1.configure(background="#808080")
        B1.configure(foreground=F_color)
        B1.config(font=("Times new roman", 25))

        GUI_page.mainloop()

    LOGIN()

start_GUI()


