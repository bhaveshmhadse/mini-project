from required_modules import *


class vaccinationd:
    def __init__(self, window4):
        self.window4 = window4
        self.window4.geometry("1200x350+300+300")
        window4.attributes("-fullscreen", True)
        self.window4.title("COVID-19 VACCINATION SYSTEM")
        self.window4.configure(background="white")
        lable = tk.Label(self.window4, text="ENTER HOSPITAL NAME:", font=("arial", 12, "bold"), bg="powder blue")
        lable.place(x=60, y=20)
        self.hos_name = tk.StringVar()
        textbox2 = tk.Entry(
            self.window4, font=("arial", 12), textvariable=self.hos_name, width=50, borderwidth=2, relief=tk.SOLID
        )
        textbox2.place(x=280, y=20)
        button4 = tk.Button(
            self.window4,
            font=("arial", 12, "bold"),
            text="SEARCH",
            command=self.search,
            borderwidth=2,
            relief=tk.SOLID,
            bg="powder blue",
        )
        button4.place(x=750, y=20)
        button4 = tk.Button(
            self.window4,
            font=("arial", 12, "bold"),
            text="BACK",
            command=self.bc,
            borderwidth=2,
            relief=tk.SOLID,
            bg="powder blue",
        )
        button4.place(x=850, y=20)
        self.generate_tree()
        self.display_all()

    def generate_tree(self):
        self.my_tree = ttk.Treeview(self.window4)

        self.my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.my_tree["show"] = "headings"
        self.my_tree.column("1", width=100, anchor="n")
        self.my_tree.column("2", width=100, anchor="n")
        self.my_tree.column("3", width=100, anchor="n")
        self.my_tree.column("4", width=70, anchor="n")
        self.my_tree.column("5", width=200, anchor="n")
        self.my_tree.column("6", width=60, anchor="n")
        self.my_tree.column("7", width=200, anchor="n")
        self.my_tree.column("8", width=200, anchor="n")
        self.my_tree.column("9", width=200, anchor="n")

        self.my_tree.heading("1", text="Serial No")
        self.my_tree.heading("2", text="FIRST NAME")
        self.my_tree.heading("3", text="LAST NAME")
        self.my_tree.heading("4", text="GENDER")
        self.my_tree.heading("5", text="PHONE NO.")
        self.my_tree.heading("6", text="DOSE NO.")
        self.my_tree.heading("7", text="VACCINE NAME")
        self.my_tree.heading("8", text="HOSPITAL NAME")
        self.my_tree.heading("9", text="AADHAR NO.")

        self.my_tree.place(x=20, y=70)

    def clear_tree(self):
        for item in self.my_tree.get_children():
            self.my_tree.delete(item)

    def display_all(self):
        con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="project")
        cur = con.cursor()
        cur.execute(f"select id,first_name,last_name,gender,phone_no,dose_n,vaccine_n,center_n,aadhar_n from customer")

        row = cur.fetchall()
        for i in row:
            self.my_tree.insert("", "end", values=i)

    def bc(self):
        self.window4.destroy()

    def search(self):
        try:
            if self.hos_name.get() == "":
                self.clear_tree()
                self.generate_tree()
                self.display_all()
            else:
                con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="project")
                cur = con.cursor()
                cur.execute(
                    f"select id,first_name,last_name,gender,phone_no,dose_n,vaccine_n,center_n,aadhar_n from customer where center_n='{self.hos_name.get()}'"
                )

                row = cur.fetchall()
                self.clear_tree()
                self.generate_tree()
                for i in row:
                    self.my_tree.insert("", "end", values=i)
        except Exception as es:
            print(str(Exception))
            messagebox.showerror("error", f"Error due to:{str(Exception)}")


if __name__ == "__main__":
    window4 = tk.Tk()
    obj = vaccinationd(window4)
    window4.mainloop()
