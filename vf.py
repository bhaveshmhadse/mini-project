from required_modules import *


class vaccinationf:
    def __init__(self, window2):
        self.window2 = window2
        self.window2.title("COVID-19 VACCINATION REGITRATION")
        self.window2.geometry("800x700+300+100")
        self.window2.focus_force()
        self.window2.configure(background="white", borderwidth=5, relief=tk.SOLID)
        label1 = tk.Label(
            self.window2, font=("arial", 30, "bold"), text="COVID-19 VACCINE FORM", fg="BLACK", bg="powder blue"
        )
        label1.place(x=100, y=30)

        # name
        lebel1 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Name: ", bg="white")
        lebel1.place(x=20, y=100)
        lebel2 = tk.Label(self.window2, font=("arial", 10), text="First Name ", bg="white")
        lebel2.place(x=20, y=150)
        lebel3 = tk.Label(self.window2, font=("arial", 10), text="Last Name ", bg="white")
        lebel3.place(x=140, y=150)
        self.fn = tk.StringVar()
        textbox1 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.fn,
            width=12,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox1.place(x=20, y=125)
        self.ln = tk.StringVar()
        textbox2 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.ln,
            width=12,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox2.place(x=140, y=125)

        # brith date
        lebel4 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Brith Date:", bg="white")
        lebel4.place(x=20, y=180)
        lebel5 = tk.Label(self.window2, font=("arial", 9), text="DD/MM/YYYY:", bg="white")
        lebel5.place(x=20, y=230)
        self.bd = tk.StringVar()
        textbox3 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.bd,
            width=12,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox3.place(x=20, y=205)

        # gender
        lebel4 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lebel4.place(x=150, y=180)
        self.gend = tk.StringVar()
        gender = ["SELECT", "MALE", "FEMALE", "TRANSGENDER"]
        cmd = ttk.Combobox(
            self.window2,
            values=gender,
            width=15,
            textvariable=self.gend,
        )
        cmd.place(x=150, y=205)
        cmd.current(0)

        # email
        lebel6 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Email:", bg="white")
        lebel6.place(x=20, y=260)
        self.email = tk.StringVar()
        textbox4 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.email,
            width=30,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox4.place(x=20, y=285)

        # phone no
        lebel7 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Phone No:", bg="white")
        lebel7.place(x=20, y=320)
        self.pn = tk.IntVar()
        textbox5 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.pn,
            width=30,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox5.place(x=20, y=345)

        # aadhar no
        lebel8 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Aadhar No:", bg="white")
        lebel8.place(x=20, y=380)
        self.an = tk.IntVar()
        textbox6 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.an,
            width=30,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox6.place(x=20, y=405)

        # address
        lebel9 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Address:", bg="white")
        lebel9.place(x=20, y=440)
        self.address = tk.StringVar()
        textbox6 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.address,
            width=30,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox6.place(x=20, y=465)

        # dose no
        lebel10 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Dose No:", bg="white")
        lebel10.place(x=20, y=500)
        self.don = tk.IntVar()
        dose_no = ["Select", "1", "2"]
        cmd = ttk.Combobox(self.window2, values=dose_no, width=15, textvariable=self.don)
        cmd.place(x=20, y=525)
        cmd.current(0)

        # vaccine name
        lebel11 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Name of vaccine:", bg="white")
        lebel11.place(x=150, y=500)
        self.vn = tk.StringVar()
        dose_no = ["Select", "COVAXIN", "COVISHIELD"]
        cmd = ttk.Combobox(self.window2, values=dose_no, width=15, textvariable=self.vn)
        cmd.place(x=150, y=525)
        cmd.current(0)

        # center name
        lebel12 = tk.Label(self.window2, font=("arial", 12, "bold"), text="Center name:", bg="white")
        lebel12.place(x=20, y=550)
        self.cn = tk.StringVar()
        textbox6 = tk.Entry(
            self.window2,
            font=("arial", 12),
            bg="light yellow",
            textvariable=self.cn,
            width=30,
            borderwidth=2,
            relief=tk.SOLID,
        )
        textbox6.place(x=20, y=575)

        # overall from
        F3 = tk.Label(self.window2, bd=10, relief=tk.GROOVE)
        F3.place(x=350, y=100, width=400, height=500)
        bill_title = tk.Label(
            F3, text="VACCINATION FORM", font=("Lucida", 13, "bold"), bd=7, relief=tk.GROOVE, bg="powder blue"
        )
        bill_title.pack(fill="both")
        scroll_y = tk.Scrollbar(F3, orient=tk.VERTICAL)
        self.txt = tk.Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill="both")
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=tk.BOTH, expand=1)

        # button
        button1 = tk.Button(self.window2, text="Enter", font=("arial", 12, "bold"), command=self.enter)
        button1.place(x=400, y=600)
        button2 = tk.Button(self.window2, text="Print", font=("arial", 12, "bold"), command=self.welcome_sof)
        button2.place(x=470, y=600)

        self.window2.mainloop()

    def enter(self):
        try:
            con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="project")

            cur = con.cursor()
            cur.execute("select * from customer where aadhar_n=%s and dose_n=%s", (self.an.get(), self.don.get()))
            row = cur.fetchone()

            if row == None:
                cur.execute(
                    "insert into customer(first_name,last_name,BOD ,gender,email,phone_no,aadhar_n,address,dose_n,vaccine_n,center_n) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [
                        (self.fn.get()),
                        (self.ln.get()),
                        (self.bd.get()),
                        (self.gend.get()),
                        (self.email.get()),
                        (self.pn.get()),
                        (self.an.get()),
                        (self.address.get()),
                        (self.don.get()),
                        (self.vn.get()),
                        (self.cn.get()),
                    ],
                )
                con.commit()
                con.close()
                messagebox.showinfo(title="status", message="Data Enter sucessful")

            else:
                messagebox.showerror(title="status", message="Following person has already registered")

        except Exception as es:
            print(str(Exception))
            messagebox.showerror("error", f"Error due to:{str( es )}")

    def welcome_sof(self):
        self.txt.insert(tk.END, f"\nFirst Name. : {str( self.fn.get() )}" "\n")
        self.txt.insert(tk.END, f"\nLast Name. : {str( self.ln.get() )}" "\n")
        self.txt.insert(tk.END, f"\nBrith Date : {str( self.bd.get() )}" "\n")
        self.txt.insert(tk.END, f"\nGender : {str( self.gend.get() )}" "\n")
        self.txt.insert(tk.END, f"\nEmail : {str( self.email.get() )}" "\n")
        self.txt.insert(tk.END, f"\nphone No. : {int( self.pn.get() )}" "\n")
        self.txt.insert(tk.END, f"\nAadhar NO. : {int( self.an.get() )}" "\n")
        self.txt.insert(tk.END, f"\nAddress. : {str( self.address.get() )}" "\n")
        self.txt.insert(tk.END, f"\nDose NO. : {int( self.don.get() )}" "\n")
        self.txt.insert(tk.END, f"\nDose NO. : {str( self.vn.get() )}" "\n")
        self.txt.insert(tk.END, f"\nDose NO. : {str( self.cn.get() )}" "\n")


if __name__ == "__main__":
    window2 = tk.Tk()
    obj = vaccinationf(window2)
    window2.mainloop()
