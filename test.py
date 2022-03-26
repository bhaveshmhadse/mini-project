from required_modules import *


con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="testing")

cur = con.cursor()
print(cur.execute("select * from test"))
row = cur.fetchall()
# cur.
print(row)
# if row == None:

con = mysql.connector.connect(host="localhost", user="bhavesh", passwd="bhavesh", database="testing")
cur = con.cursor()
# cur.execute("insert into test(first_name)", ["Bhavesh"])
name = "pranav"

sql = "INSERT INTO test(first_name) values(%s)"
val = ("Baray",)

cur.execute("INSERT INTO test(first_name) values(%s)", [("Baray")])

cur = con.cursor()
print(cur.execute("select * from test"))
row = cur.fetchall()
# cur.
print(row)
#     con = mysql.connector.connect(host="localhost", user="root", passwd="Shekhar@2002", database="database2")
#     cur = con.cursor()
#     cur.execute(
#         "insert into testing(first_name,last_name,BOD ,gender,email,phone_no,aadhar_n,address,dose_n,vaccine_n,center_n) valuess(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#         (
#             # self.fn.get(),
#             "Bhavesh",
#             "Mhadse",
#             "11/05/2001",
#             "male",
#             "baray@gmail.com",
#             9136298868,
#             123412344321,
#             "sdsddsd sdsdsd sdsd sd",
#             1,
#             2,
#             3
#             # self.ln.get(),
#             # self.bd.get(),
#             # self.gend.get(),
#             # self.email.get(),
#             # self.pn.get(),
#             # self.an.get(),
#             # self.address.get(),
#             # self.don.get(),
#             # self.vn.get(),
#             # self.cn.get(),
#         ),
#     )
#     con.commit()
#     con.close()
#     messagebox.showinfo(title="status", message="Data Enter sucessful")
