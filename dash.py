from required_modules import *


class dashb:
    def __init__(self, window5):
        self.window5 = window5
        self.window5.title("COVID-19 VACCINATION REGITRATION")
        self.window5.geometry("800x700+300+100")
        window5.attributes("-fullscreen", True)

        self.window5.focus_force()

        self.window5.title("DASHBORAD")
        self.window5.geometry("900x520+300+250")
        self.window5.configure(background="WHITE")
        self.window5.configure(background="white", borderwidth=5, relief=tk.SOLID)
        self.lable = tk.Label(self.window5, text="ENTER HOSPITAL NAME:", font=("arial", 12, "bold"), bg="WHITE")
        self.lable.place(x=40, y=20)
        self.lable1 = tk.Label(
            self.window5,
            text="PERSON VACCINATED\n[0]",
            bd=5,
            relief=tk.RIDGE,
            font=("arial", 12, "bold"),
            bg="#33bbf9",
            fg="white",
            height=10,
            width=20,
        )
        self.lable1.place(x=100, y=70)
        self.lable2 = tk.Label(
            self.window5,
            text="VACCINATED\nFOR COVAXIN\n[0]",
            bd=5,
            relief=tk.RIDGE,
            font=("arial", 12, "bold"),
            bg="#ff5722",
            fg="white",
            height=10,
            width=20,
        )
        self.lable2.place(x=350, y=70)
        self.lable3 = tk.Label(
            self.window5,
            text="VACCINATED\nFOR COVISHIELD\n[0]",
            bd=5,
            relief=tk.RIDGE,
            font=("arial", 12, "bold"),
            bg="#009688",
            fg="white",
            height=10,
            width=20,
        )
        self.lable3.place(x=600, y=70)
        self.lable4 = tk.Label(
            self.window5,
            text="VACCINATED\nFOR DOSE1\n[0]",
            bd=5,
            relief=tk.RIDGE,
            font=("arial", 12, "bold"),
            bg="#607d8b",
            fg="white",
            height=10,
            width=20,
        )
        self.lable4.place(x=200, y=290)
        self.lable5 = tk.Label(
            self.window5,
            text="VACCINATED\nFOR DOSE2\n[0]",
            bd=5,
            relief=tk.RIDGE,
            font=("arial", 12, "bold"),
            bg="#ffc107",
            fg="white",
            height=10,
            width=20,
        )
        self.lable5.place(x=450, y=290)
        self.hos_name = tk.StringVar()
        textbox2 = tk.Entry(
            self.window5, font=("arial", 12), textvariable=self.hos_name, width=50, borderwidth=2, relief=tk.SOLID
        )
        textbox2.place(x=260, y=20)
        button4 = tk.Button(
            self.window5,
            font=("arial", 11, "bold"),
            text="SEARCH",
            command=self.dash_search,
            borderwidth=2,
            relief=tk.SOLID,
            bg="#009688",
        )
        button4.place(x=730, y=20)
        button4 = tk.Button(
            self.window5,
            font=("arial", 11, "bold"),
            text="BACK",
            command=self.dash_bc,
            borderwidth=2,
            relief=tk.SOLID,
            bg="WHITE",
        )
        button4.place(x=830, y=20)
        self.window5.mainloop()

    def dash_search(self):
        try:
            con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="project")
            cur = con.cursor()

            cur.execute(f"select * from customer where center_n='{self.hos_name.get()}'")
            row = cur.fetchall()
            self.lable1.configure(text=f"PERSON VACCINATED\n[{str( len( row ) )}]")

            cur.execute(f"select * from customer where center_n='{self.hos_name.get()}' AND vaccine_n='COVISHIELD' ")
            row1 = cur.fetchall()
            self.lable3.configure(text=f"VACCINATED\nFOR COVISHIELD\n[{str( len( row1 ) )}]")

            cur.execute(f"select * from customer where center_n='{self.hos_name.get()}' AND vaccine_n='COVAXIN' ")
            row2 = cur.fetchall()
            self.lable2.configure(text=f"VACCINATED\nFOR COVAXIN\n[{str( len( row2 ) )}]")

            cur.execute(f"select * from customer where center_n='{self.hos_name.get()}' AND dose_n='1' ")
            row3 = cur.fetchall()
            self.lable4.configure(text=f"VACCINATED\nFOR DOSE1\n[{str( len( row3 ) )}]")

            cur.execute(f"select * from customer where center_n='{self.hos_name.get()}' AND dose_n='2'  ")
            row4 = cur.fetchall()
            self.lable5.configure(text=f"VACCINATED\nFOR DOSE2\n[{str( len( row4 ) )}]")

        except Exception as es:
            messagebox.showerror("error", f"Error due to:{str( es )}")

    def dash_bc(self):
        self.window5.destroy()


if __name__ == "__main__":
    window5 = tk.Tk()
    obj = dashb(window5)
    window5.mainloop()
