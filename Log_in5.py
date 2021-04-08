from tkinter import *
import PyMySQL as database


db = database.connect('127.0.0.1', 'root', 'root', 'kytsyk_d')

'''
																			def VVV(event):
																			    cur = db.cursor()
																			    cur.execute('SELECT * FROM new_table;')
																			    for row in cur.fetchall():
																			        print(*row)'''


def TakNi():
	Vikno = Toplevel()
	Vikno.title("Tak Ni")
	Vikno.geometry("250x200")
	Vikno.configure(bg='#1f1f2e')
	Vikno.resizable(width=False, height=False)

	Mess = Label(Vikno, text="Логін або пароль неправильні", font=("Helvetica", 10))
	Mess.place(x=34, y=16)

	Mess_2 = Label(Vikno, text="Можливо ви ще не зареєстровані", font=("Helvetica", 10))
	Mess_2.place(x=24, y=76)

	Mess_3 = Label(Vikno, text="Бажаєте це зробити?", font=("Helvetica", 10))
	Mess_3.place(x=58, y=98)


	def quit():
		Vikno.destroy()

	b = Button(Vikno, text = 'Ні', command = quit, width = 5, height = 1)
	b.place(x=135, y=130)

	insert = Button(Vikno, text="Так", width=5, height=1, command = OpenReg)
	insert.place(x=75, y=130)


def Dialog():
	DiaWin = Toplevel()
	DiaWin.title("Dialog Window")
	DiaWin.geometry("600x750")
	DiaWin.configure(bg='#1f1f2e')
	DiaWin.resizable(width=False, height=False)




def Zareg():
	ZarVik = Toplevel()
	ZarVik.title("Зареєстровано!")
	ZarVik.geometry("300x70")
	ZarVik.configure(bg='#1f1f2e')
	ZarVik.resizable(width=False, height=False)

	Mess = Label(ZarVik, text="Вітаю! Ви успішно зареєструвались!", font=("Helvetica", 10))
	Mess.place(x=34, y=16)



def OpenReg():
	Lowroot = Toplevel()
	Lowroot.title("Реєстрація")
	Lowroot.geometry("300x300")
	Lowroot.configure(bg = '#1f1f2e')
	Lowroot.resizable(width=False, height=False)

	def reg(*args):
		e_code = i_code.get()
		e_name = i_name.get()
		e_price = i_price.get()
		Lowroot = database.connect('127.0.0.1', 'root', 'root', 'kytsyk_d')
		cursor = Lowroot.cursor()

		cursor.execute("INSERT INTO new_table(Login, Password, UserName) VALUES(%s, %s, %s)", (e_code, e_name, e_price))
		Lowroot.commit()
		Zareg()
		Dialog()
		Lowroot.close()


	def VVV():
		cur = db.cursor()
		cur.execute('SELECT * FROM new_table;')
		for row in cur.fetchall():
			print(*row)

	i_code = StringVar()
	i_name = StringVar()
	i_price = StringVar()

	reg_lbl = Label(Lowroot, text="REGISTRATION", font=("Helvetica", 15))
	reg_lbl.place(x=85, y=10)

	login_lbl = Label(Lowroot, text="Login", font=("Helvetica", 10))
	login_lbl.place(x=70, y=48)
	#===================================================================
	password_lbl = Label(Lowroot, text = "Password", font = ("Helvetica", 10))
	password_lbl.place(x=44, y=73)
	#===================================================================
	user_name_lbl = Label(Lowroot, text = "UserName", font = ("Helvetica", 10))
	user_name_lbl.place(x = 40, y = 98)

	login_edit = Entry(Lowroot, width=15, textvariable = i_code)
	login_edit.place(x = 120, y = 50)
	#=================================
	password_edit = Entry(Lowroot, width = 15, textvariable = i_name)
	password_edit.place(x = 120, y = 75)
	#=================================
	user_name_edit = Entry(Lowroot, width=15, textvariable = i_price)
	user_name_edit.place(x=120, y=100)


	insert = Button(Lowroot, text="Зареєструвати", width=20, height=2, bg="white", fg="black", command = reg)
	#insert.bind("<Button-1>")
	insert.place(x=85, y=130)


	btn_3 = Button(Lowroot,
	             text="Вивести БД",
	             width=20, height=2,
	             bg="white", fg="black", command = VVV)
	#btn_3.bind("<Button-1>")
	btn_3.place(x=85, y=180)



	def quit():
		Lowroot.destroy()

	b = Button(Lowroot, text = 'Quit', command = quit, width = 42, height = 1)
	b.place(x=0, y=274)






def Log_in(*args):
	e_code = i_code.get()
	e_name = i_name.get()
	db = database.connect('127.0.0.1', 'root', 'root', 'kytsyk_d')
	cursor = db.cursor()

	cursor.execute(f"SELECT Login, Password FROM new_table WHERE Login = '{e_code}' AND Password = '{e_name}'")
	if cursor.fetchone() is None:
		TakNi()
	else:
		Dialog()
	db.close()


def In():
	e_code = i_code.get()
	e_name = i_name.get()
	db = database.connect('127.0.0.1', 'root', 'root', 'kytsyk_d')

	cursor = db.cursor()
	y = cursor.execute(f"SELECT Login FROM new_table WHERE Login = '{e_code}'")
	for row in cursor.fetchall():
		y = row
		#print('Login: ',*row)

	t = cursor.execute(f"SELECT Password FROM new_table WHERE Password = '{e_name}'")
	for row in cursor.fetchall():
		t = row
		#print('Password: ', *row)
	#print(y)
	return [y, t]


def BBB():
	[y,t]  = In()
	y = login5_lbl = Label(root, text=("User Login: ",y), font=("Helvetica", 10))
	login5_lbl.place(x=60, y=202)
	t = login6_lbl = Label(root, text=("User Password: ",t), font=("Helvetica", 10))
	login6_lbl.place(x=60, y=232)



root= Tk()
root.title("Log in")
root.geometry("300x300")
root.configure(bg = '#1f1f2e')
root.resizable(width = False, height = False)

i_code = StringVar()
i_name = StringVar()
'''
													def openfile():
													    return filedialog.askopenfilename(Reg.py)'''
'''
Open = Button(root, text="Open", command = openfile)  # <------
Open.grid(column=1, row=1)'''




Log_lbl = Label(root, text = "Log in", font=("Helvetica", 15))
Log_lbl.place(x=125, y=10)


login_lbl = Label(root, text="Login", font=("Helvetica", 10))
login_lbl.place(x= 60, y = 62)


password_lbl = Label(root, text = "Password", font = ("Helvetica", 10))
password_lbl.place(x = 34, y = 96)


#login5_lbl = Label(root, text=y, font=("Helvetica", 10))
#login5_lbl.place(x=60, y=202)


login_edit = Entry(root, width = 20, textvariable = i_code)
login_edit.place(x = 105, y = 65)


password_edit = Entry(root, width = 20, textvariable = i_name)
password_edit.place(x = 105, y = 95)

'''Mess_2 = Label(root, font=("Helvetica", 10))
Mess_2.place(x=34, y=146)'''


Log_in = Button(root,
             text="Log in",
             width=20, height=2,
             bg="white", fg="black", command = Log_in)
Log_in.bind("<Button-1>")
Log_in.place(x = 85, y = 130)


Reg = Button(root,
             text="Registration",
             width=10, height=1,
             bg="white", fg="black", command = OpenReg)
Reg.place(x=115, y=180)

Log_in = Button(root,
             text="Log in",
             width=20, height=2,
             bg="white", fg="black", command = BBB)
Log_in.bind("<Button-1>")
Log_in.place(x = 85, y = 230)



def quit():
	root.destroy()

button = Button(root, text = 'Quit', command = quit, width = 42, height = 1)
button.place(x = 0, y = 274)
root.mainloop()
root.mainloop()



'''
from tkinter import *
import PyMySQL as database

from tkinter import ttk


#functions
def functionHolder():
	cursor = dbi.cursor()
	cursor.execute('SELECT Login FROM users WHERE UserId = 1;')
	for row in cursor.fetchall():
		print(*row)


root = Tk()
dbi = database.connect('127.0.0.1', 'root', 'KurwaScript', 'bazadate')
cursor = dbi.cursor()

cursor.execute("""SELECT Login FROM users WHERE UserId = 1 """)
dbi.commit()
data = cursor.fetchone()[0]
dbi.close()

result =str("%s " % data)



varButt = Button(root,textvariable=data, command=functionHolder)
varButt.pack()

root.mainloop()'''