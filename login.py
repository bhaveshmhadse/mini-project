from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from main import main_page


class login:
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry("1350x600+0+0")
        self.root1.title("COVID-19 VACCINATION SYSTEM")
        self.root1.state( "zoomed" )
        self.photo = PhotoImage( file="p3.png" )
        label1 = Label( self.root1, image=self.photo )
        label1.grid()
        lebel1 = Label( self.root1, font=('goudy old style', 50, 'bold'), text="COVID-19 VACCINATION  SYSTEM ", bd=10,
                        fg="white", bg="#033054" )
        lebel1.place( x=0, y=50, relwidth=1 )
        lebel2 = Label( self.root1, font=('goudy old style', 15, 'bold'), text="WELCOME TO COVID-19 VACCINATION  ",
                        bd=10, fg="GRAY1", bg="#4d636d" )
        lebel2.place( x=0, y=140, relwidth=1 )
         ##login##

        left3 = Frame( self.root1, bd=2, relief=RIDGE, width=500, height=500, bg="white" )
        left3.place( x=500, y=220 )
        self.photo1= PhotoImage( file="p2.png" )
        label1 = Label( left3, image=self.photo1,bg="white" )
        label1.place(x=70,y=10)
        lable3=Label(left3, font=('goudy old style', 30, 'bold'), text="LOGIN", bd=10,
                        fg="black")
        lable3.place(x=170,y=10)


        ###########
        self.photo2 = PhotoImage( file="p6.png" )
        label2 = Label( left3, image=self.photo2 )
        label2.grid()
        lable4 = Label( left3, font=('goudy old style', 15, 'bold'), text="USERNAME :", bd=10,bg="powder blue",
                       fg="black" )
        lable4.place( x=50, y=120 )
        lable5= Label( left3, font=('goudy old style', 15, 'bold'), text="PASSWORD :", bd=10,bg="powder blue",
                        fg="black" )
        lable5.place( x=50, y=170 )
        self.user=StringVar()
        textbox1 = Entry( left3, font=('arial', 15), textvariable=self.user, width=25, borderwidth=2,
                          relief=SOLID )
        textbox1.place( x=200, y=130 )
        self.password=StringVar()
        textbox2= Entry( left3, font=('arial', 15), textvariable=self.password,show="*" ,width=25, borderwidth=2,
                          relief=SOLID )
        textbox2.place( x=200, y=180 )

        btn1=Button(left3,text="LOGIN",font=('arial', 12),bg="powder blue",command=self.login, borderwidth=2,relief=GROOVE,bd=3)
        btn1.place(x=200,y=250)
        btn2= Button( left3, text="CLEAR", font=('arial', 12), bg="powder blue",command=self.clear, borderwidth=2, relief=GROOVE,bd=3)
        btn2.place( x=270, y=250 )
        btn3 = Button( left3, text="EXIT", font=('arial', 12), bg="powder blue",command=self.exit, borderwidth=2, relief=GROOVE,bd=3  )
        btn3.place( x=345, y=250 )
        btn4 = Button( left3, text="NEW REGISTER", font=('arial', 12), bg="powder blue",fg="red",command=self.new_user, relief=GROOVE,width=20,bd=3  )
        btn4.place( x=200, y=300 )

    def login(self):

            if self.user.get()=="" and self.password.get()=="":
              messagebox.showerror( "error", "PLEASE ENTER THE USER NAME AND PASSWORD" )
            else:
              try:
                  con = mysql.connector.connect( host='localhost', user='root', passwd='',
                                                 database="registration" )
                  cur = con.cursor()

                  cur.execute( "select * from new_user where un=%s and dist=%s",
                               (self.user.get(), self.password.get()) )
                  row = cur.fetchone()
                  if row == None:
                      messagebox.showerror( "error", " INVALID username and password " )
                  else:
                    self.new_win = Toplevel( )
                    self.new_obj = main_page( self.new_win )
              except Exception as es:
                  messagebox.showerror( "error", f"Error due to:{str( es )}" )


    def clear(self):
        self.user.set("")
        self.password.set("")

    def exit(self):
        self.root1.destroy()

    def new_user(self):
        self.root1.destroy()
        self.window1 = Tk()
        self.window1.title( "COVID-19 VACCINATION REGITRATION" )
        self.window1.geometry( '800x500+500+200' )
        photo3 = PhotoImage( file="p3.png" )
        label = Label( self.window1, image=photo3 )
        label.grid()
        label1 = Label( self.window1, font=('arial', 30, 'bold'), text="REGITRATION FORM", fg="orange",
                        bg="powder blue" )
        label1.place( x=20, y=30 )
        # LABELS
        lebel1 = Label( self.window1, font=('arial', 12, 'bold'), text="NAME OF HOSPITAL : ", bg="light blue" )
        lebel1.place( x=20, y=90 )
        lebel2 = Label( self.window1, font=('arial', 12, 'bold'), text="NAME OF DOCTOR :", bg="light blue" )
        lebel2.place( x=20, y=140 )
        lebel3 = Label( self.window1, font=('arial', 12, 'bold'), text="ENTER NEW USERNAME :", bg="light blue" )
        lebel3.place( x=20, y=190 )
        lebel4 = Label( self.window1, font=('arial', 12, 'bold'), text="ENTER NEW PASSWORD :", bg="light blue" )
        lebel4.place( x=20, y=240 )
        lebel5 = Label( self.window1, font=('arial', 12, 'bold'), text="STATE :", bg="light blue" )
        lebel5.place( x=20, y=290 )
        lebel6 = Label( self.window1, font=('arial', 12, 'bold'), text="DISTRICT :", bg="light blue" )
        lebel6.place( x=420, y=290 )
        lebel7 = Label( self.window1, font=('arial', 12, 'bold'), text="CITY/VILLAGE :", bg="light blue" )
        lebel7.place( x=20, y=340 )
        lebel8 = Label( self.window1, font=('arial', 12, 'bold'), text="PINCODE :", bg="light blue" )
        lebel8.place( x=420, y=340 )
        # TEXTBOXT AND VARIABLES
        self.name_hos = StringVar()
        textbox1 = Entry( self.window1, font=('arial', 12), textvariable=self.name_hos, width=40, borderwidth=2,
                          relief=SOLID )
        textbox1.place( x=290, y=90 )
        self.name_doctor = StringVar()
        textbox2 = Entry( self.window1, font=('arial', 12), textvariable=self.name_doctor, width=40, borderwidth=2,
                          relief=SOLID )
        textbox2.place( x=290, y=140 )
        self.username = StringVar()
        textbox3 = Entry( self.window1, font=('arial', 12), textvariable=self.username, width=40, borderwidth=2,
                          relief=SOLID )
        textbox3.place( x=290, y=190 )
        self.password = StringVar()
        textbox4 = Entry( self.window1, font=('arial', 12), textvariable=self.password, width=40, borderwidth=2,
                          relief=SOLID )
        textbox4.place( x=290, y=240 )
        self.state = StringVar()
        textbox5 = Entry( self.window1, font=('arial', 12), textvariable=self.state, width=20, borderwidth=2,
                          relief=SOLID )
        textbox5.place( x=140, y=290 )
        self.dis = StringVar()
        textbox6 = Entry( self.window1, font=('arial', 12), textvariable=self.dis, width=20, borderwidth=2,
                          relief=SOLID )
        textbox6.place( x=540, y=290 )
        self.cv = StringVar()
        textbox7 = Entry( self.window1, font=('arial', 12), textvariable=self.cv, width=20, borderwidth=2,
                          relief=SOLID )
        textbox7.place( x=180, y=340 )
        self.pin = IntVar()
        textbox8 = Entry( self.window1, font=('arial', 12), textvariable=self.pin, width=20, borderwidth=2,
                          relief=SOLID )
        textbox8.place( x=540, y=340 )

        # BUTTONS
        button1 = Button( font=('arial', 12), text="REGISTER", command=self.register, borderwidth=2, relief=SOLID )
        button2 = Button( font=('arial', 12), text="BACK", command=self.back, borderwidth=2, relief=SOLID )
        button1.place( x=400, y=400 )
        button2.place( x=530, y=400 )
        self.window1.mainloop()

    def register(self):
        name = self.name_hos.get()
        d_name = self.name_doctor.get()
        un = self.username.get()
        pa = self.password.get()
        st = self.state.get()
        dist = self.dis.get()
        state = self.cv.get()
        pi = self.pin.get()

        if name == "" or d_name == "" or un == "" or pa == "" or st == "" or dist == "" or state == "" or pi == "":
            messagebox.showinfo( title="status", message="All Fileld Fill compulsory" )
        else:
            try:
                con = mysql.connector.connect( host='localhost', user='root', passwd='',
                                               database="registration" )
                cur = con.cursor()

                cur.execute(
                    "insert into new_user(hospita,doctor,un ,dist,state,dis,city,pin) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.name_hos.get(),
                     self.name_doctor.get(),
                     self.username.get(),
                     self.password.get(),
                     self.state.get(),
                     self.dis.get(),
                     self.cv.get(),
                     self.pin.get())
                    )
                con.commit()
                con.close()
                messagebox.showinfo( title="status", message="Regitration sucessful" )
            except Exception as es:
                messagebox.showerror( "error", f"Error due to:{str( es )}" )



    def back(self):
        self.window1.destroy()
        root1 = Tk()
        self.__init__(root1)

if __name__ == '__main__':

 root1=Tk()
 obj=login(root1)
 root1.mainloop()