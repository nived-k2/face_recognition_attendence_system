from tkinter import *
from datetime import datetime
import os

root = Tk()
root.configure(background="ivory4")
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

label1 = Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),bg="red4",fg="white",height=2)
label1.grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)









def v_attendance():
	os.startfile(os.getcwd()+"/Attendance_Files/attendance"+str(datetime.now().date())+'.xlsx')



def destroy():
    root.destroy()




button5 = Button(root, text="View Attendance Sheet",font=("times new roman",20),bg="dodgerblue4",fg='white',command=v_attendance)
button5.grid(row=6,rowspan=2,column=0,sticky=N+E+W+S,padx=10,pady=10)



button7 = Button(root,text="Exit",font=('times new roman',20),bg="red4",fg="white",command=destroy)
button7.grid(row=8,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)


root.mainloop()
