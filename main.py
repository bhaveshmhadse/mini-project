from required_modules import *


from vf import vaccinationf
from vd import vaccinationd
from dash import dashb


class main_page:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x900")
        self.root.title("COVID-19 VACCINATION SYSTEM")
        self.root.state("normal")

        ##photo##
        self.photo = tk.PhotoImage(file="p1.png")
        label1 = tk.Label(self.root, image=self.photo)
        label1.grid()

        ##lables#
        lebel1 = tk.Label(
            self.root,
            font=("goudy old style", 50, "bold"),
            text="COVID-19 VACCINATION  SYSTEM ",
            bd=10,
            fg="WHITE",
            bg="#033054",
        )
        lebel1.place(x=0, y=50, relwidth=1)
        lebel2 = tk.Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            text="WELCOME TO COVID-19 VACCINATION  ",
            bd=10,
            fg="GRAY1",
            bg="#4d636d",
        )
        lebel2.place(x=0, y=140, relwidth=1)

        # logout button
        button1 = tk.Button(
            self.root,
            font=("goudy old style", 15),
            text="LOGOUT",
            command=self.login,
            borderwidth=2,
            relief=tk.SOLID,
            bg="YELLOW",
            fg="black",
            width=10,
            height=1,
        )
        button1.place(x=1450, y=80)

        # LEFT MENU#
        leftmenu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, width=300, height=600, bg="white")
        leftmenu.place(x=0, y=190)
        self.photo2 = tk.PhotoImage(file="p5.png")
        label1 = tk.Label(leftmenu, image=self.photo2)
        label1.place(x=0, y=0)
        lebel2 = tk.Label(
            leftmenu,
            font=("goudy old style", 15, "bold"),
            text="MENU ",
            bd=10,
            fg="WHITE",
            bg="#4d636d",
        )
        lebel2.place(x=0, y=200, relwidth=1)

        # BUTTON#
        button1 = tk.Button(
            leftmenu,
            font=("goudy old style", 15),
            text="VACCINATION FORM",
            command=self.vf,
            borderwidth=2,
            relief=tk.SOLID,
            bg="POWDER BLUE",
            fg="black",
            width=20,
            height=2,
        )
        button1.place(x=0, y=250, relwidth=1)
        button2 = tk.Button(
            leftmenu,
            font=("goudy old style", 15),
            text="VACCINATED PEOPLE DETAILS",
            command=self.vd,
            borderwidth=2,
            relief=tk.SOLID,
            bg="POWDER BLUE",
            fg="black",
            width=20,
            height=2,
        )
        button2.place(x=0, y=330, relwidth=1)
        button3 = tk.Button(
            leftmenu,
            font=("goudy old style", 15),
            text="DASHBOARD",
            borderwidth=2,
            relief=tk.SOLID,
            command=self.dash,
            bg="POWDER BLUE",
            fg="black",
            width=20,
            height=2,
        )
        button3.place(x=0, y=410, relwidth=1)

    def login(self):
        self.root.destroy()

    # Pages
    def vf(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = vaccinationf(self.new_win)

    def vd(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = vaccinationd(self.new_win)

    def dash(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = dashb(self.new_win)


if __name__ == "__main__":
    root = tk.Tk()
    obj = main_page(root)
    root.mainloop()
