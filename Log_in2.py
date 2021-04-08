from tkinter import *
import mysql.connector
from tkinter import filedialog

db = mysql.connector.connect(user='root', password='KurwaScript',
                host='127.0.0.1',
                database='bazadate')


def VVV(event):
    cur = db.cursor()
    cur.execute('SELECT * FROM users;')
    for row in cur.fetchall():
        print(*row)

def Log_in(*args):
	e_code = i_code.get()
	e_name = i_name.get()
	db = mysql.connector.connect(user='root', password='KurwaScript',
                host='127.0.0.1',
                database='bazadate')
	cursor = db.cursor()

	cursor.execute(f"SELECT Login, Password FROM users WHERE Login = '{e_code}' AND Password = '{e_name}'")
	if cursor.fetchone() is None:
		print("fjidjdifjvffjfjfjf")
	else:
		OpenReg()
	db.close()


		
def OpenReg():
	dg = Toplevel(root)
	'''dg.geometry("300x300")
	dg.title("Dialog") 
	dg.configure(bg = '#1f1f2e')
	dg.resizable(width=False, height=False)'''




	def reg_2(*args):
	    e_code = i_code.get()
	    e_name = i_name.get()
	    e_price = i_price.get()
	    db = mysql.connector.connect(user='root', password='KurwaScript',host='127.0.0.1',database='bazadate')
	    cursor = db.cursor()
	    cursor.execute("INSERT INTO users(Login, Password, UserName) VALUES(%s, %s, %s)", (e_code, e_name, e_price))
	    db.commit()
	    db.close()

	def VVVWW(event):
	    cur = db.cursor()
	    cur.execute('SELECT * FROM users;')
	    for row in cur.fetchall():
	        print(*row)

	dg= Tk()
	dg.title("Реєстрація")
	dg.geometry("300x300")
	dg.configure(bg = '#1f1f2e')
	dg.resizable(width=False, height=False)



	i_code = StringVar()
	i_name = StringVar()
	i_price = StringVar()

	reg_lbl = Label(dg, text="REGISTRATION", font=("Helvetica", 15))
	reg_lbl.place(x=85, y=10)

	login_lbl = Label(dg, text="Login", font=("Helvetica", 10))
	login_lbl.place(x=70, y=48)
	#===================================================================
	password_lbl = Label(dg, text = "Password", font = ("Helvetica", 10))
	password_lbl.place(x=44, y=73)
	#===================================================================
	user_name_lbl = Label(dg, text = "UserName", font = ("Helvetica", 10))
	user_name_lbl.place(x = 40, y = 98)

	login_edit = Entry(dg, width=15, textvariable = i_code)
	login_edit.place(x = 120, y = 50)
	#=================================
	password_edit = Entry(dg, width = 15, textvariable = i_name)
	password_edit.place(x = 120, y = 75)
	#=================================
	user_name_edit = Entry(dg, width=15, textvariable = i_price)
	user_name_edit.place(x=120, y=100)



	insert_2 = Button(dg,
	             text="Зареєструвати",
	             width=20, height=2,
	             bg="white", fg="black", command = reg_2)
	#insert.bind("<Button-1>")
	insert_2.place(x=85, y=130)


	btn_3 = Button(dg,
	             text="Вивести БД",
	             width=20, height=2,
	             bg="white", fg="black")
	btn_3.bind("<Button-1>", VVVWW)
	btn_3.place(x=85, y=180)



	button = Button(root, text='Quit', command=quit, width=42, height=1)
	button.place(x=0, y=274)
	root.mainloop()

	def quit():
	    root.destroy()

	root.mainloop()






root= Tk()
root.title("Log in")
root.geometry("300x300")
root.configure(bg = '#1f1f2e')
root.resizable(width=False, height=False)

i_code = StringVar()
i_name = StringVar()

'''def openfile():
    return filedialog.askopenfilename(Reg.py)

Open = Button(root, text="Open", command = openfile)  # <------
Open.grid(column=1, row=1)
'''



Log_lbl = Label(root, text = "Log in", font=("Helvetica", 15))
Log_lbl.place(x=125, y=10)


login_lbl = Label(root, text="Login", font=("Helvetica", 10))
login_lbl.place(x= 60, y = 62)


password_lbl = Label(root, text = "Password", font = ("Helvetica", 10))
password_lbl.place(x = 34, y = 96)


login_edit = Entry(root, width = 20, textvariable = i_code)
login_edit.place(x = 105, y = 65)


password_edit = Entry(root, width = 20, textvariable = i_name)
password_edit.place(x = 105, y = 95)


Log_in = Button(root,
             text="Log in",
             width=20, height=2,
             bg="white", fg="black", command = Log_in)
Log_in.bind("<Button-1>")
Log_in.place(x = 85, y = 130)


Reg = Button(root,
             text="Registration",
             width=10, height=1,
             bg="white", fg="black")
Reg.bind("<Button-1>")
Reg.place(x=115, y=180)


button = Button(root, text = 'Quit', command = quit, width = 42, height = 1)
button.place(x = 0, y = 274)
root.mainloop()

def quit():
    root.destroy()


root.mainloop()