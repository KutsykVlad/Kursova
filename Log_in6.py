from tkinter import *
import mysql.connector



#===============================Інфо-вікно, якщо неправильно введено або не існує=======================
def Log_in_RightWrong():
	Vikno = Toplevel()
	Vikno.title("Tak Ni")
	Vikno.geometry("250x200")
	Vikno.configure(bg='#1f1f2e')
	Vikno.resizable(width=False, height=False)

	Smth_wrong = Label(Vikno, text="Логін або пароль неправильні", font=("Helvetica", 10))
	Smth_wrong.place(x=34, y=16)

	D_U_zareg  = Label(Vikno, text="Можливо ви ще не зареєстровані", font=("Helvetica", 10))
	D_U_zareg.place(x=24, y=76)

	Wanna_zareg = Label(Vikno, text="Бажаєте це зробити?", font=("Helvetica", 10))
	Wanna_zareg.place(x=58, y=98)


	def quit():
		Vikno.destroy()


	Ni = Button(Vikno, text = 'Ні', command = quit, width = 5, height = 1)
	Ni.place(x=135, y=130)

	Tak = Button(Vikno, text="Так", width=5, height=1, command = lambda:[OpenReg(), quit()])
	Tak.place(x=75, y=130)
#=======================================================================================================




#===============================Вікно створення нового діалогу===========================================
def CreaDia():
	NewDia = Toplevel()
	NewDia.title("Create New Dialog")
	NewDia.geometry("230x150")
	NewDia.configure(bg='#1f1f2e')
	NewDia.resizable(width=False, height=False)

	def DiaReg(*args):         # Реєструє новий діалог за назвою
		e_dialog = i_dialog.get()
		NewDia = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='bazadate')
		#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
		cursor = NewDia.cursor()

		cursor.execute("INSERT INTO dialog(DialogName) VALUES(%s)", (e_dialog))
		NewDia.commit()


	Nazva_Dia = Label(NewDia, text = "Вкажіть назву діалогу", font = ("Helvetica", 10))
	Nazva_Dia.place(x = 50, y = 15)

	Dialog_enter = Entry(NewDia, width = 30, textvariable = i_dialog)
	Dialog_enter.place(x = 25, y = 45)


	def quit():
		NewDia.destroy()

	Close = Button(NewDia,   
             text=" x ",
             width=3, height=1,
             bg="white", fg="black", command = quit)
	Close.place(x=25, y=75)


	Done = Button(NewDia,  #Галочка
             text=" ✓ ",
             width=3, height=1,
             bg="white", fg="black", command = DiaReg)
	Done.place(x=180, y=75)
#========================================================================================================




#===============================Головне діалогове вікно після входу======================================
def Dialog():
	DiaWindow = Toplevel()
	DiaWindow.title("Dialog Window")
	DiaWindow.geometry("600x650")
	DiaWindow.configure(bg='#1f1f2e')
	DiaWindow.resizable(width=False, height=False)


	def DiaForm():   #Вибирає назву діалога де його ІД = 1
					e_dialog = i_dialog.get()
					db = mysql.connector.connect(user='root', password='root',
			                              host='127.0.0.1',
			                              database='bazadate')
					#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
			
					cursor = db.cursor()
					d = cursor.execute(f"SELECT DialogName FROM dialog WHERE DialogId = 1")
					for row in cursor.fetchall():
						d = row
			
					return [d]

	
	

	def CreForm():    #Створює форму діалогу при натисканні на кнопку з назвою діалогу
		[d] = DiaForm()
		d = login5_lbl = Label(DiaWindow, text=("Dialog Name: ", d), font=("Helvetica", 10))
		login5_lbl.place(x = 240, y = 10)

		TeEd = Entry(DiaWindow, width = 65)
		TeEd.place(x = 150, y = 620, height= 30)

		ButEd = Button(DiaWindow,   # Стрілочка
             text = "➔" ,
             width=6, height=2,
             bg="white", fg="black")
		ButEd.place(x=549, y=620)


	def In():   # Створює основну стуктуру діалогового вікна
		e_code = i_code.get()
		e_dialog = i_dialog.get()
		db = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='bazadate')
		#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')

		cursor = db.cursor()
		y = cursor.execute(f"SELECT UserName FROM users WHERE Login = '{e_code}'")
		for row in cursor.fetchall():
			y = row
		# print('Login: ',*row)

		t = cursor.execute(f"SELECT UserId FROM users WHERE Login = '{e_code}'")
		for row in cursor.fetchall():
			t = row
		# print('Password: ', *row)
		# print(y)

		u = cursor.execute(f"SELECT Login FROM users WHERE Login = '{e_code}'")
		for row in cursor.fetchall():
			u = row

		d = cursor.execute(f"SELECT DialogName FROM dialog WHERE DialogId = 1")
		for row in cursor.fetchall():
			d = row

		return [y, t, u, d]








	def BBB():     # Виводить основну стуктуру діалогового вікна
		[*y, t, u, d] = In()
		y = login5_lbl = Label(DiaWindow, text=("User Name: ", y), font=("Helvetica", 10))
		login5_lbl.place(x = 10, y = 10)
		t = login6_lbl = Label(DiaWindow, text=("Id: ", t, " / Login: ", u), font=("Helvetica", 10))
		login6_lbl.place(x = 10, y = 40)
		'''d = Button(DiaWindow,
									text= d,
									width=20, height=3,
									bg="white", fg="black", command = CreForm)
								d.place(x=0, y=85)'''
		Create = Button(DiaWindow,
             text=" + ",
             width=10, height=3,
             bg="white", fg="black", command = CreaDia)
		Create.place(x=522, y=0)







		e_dialog = i_dialog.get()
		db = mysql.connector.connect(user='root', password='root',
			                              host='127.0.0.1',
			                              database='bazadate')
					#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
			
		cursor = db.cursor()
		d = cursor.execute(f"SELECT DialogName FROM dialog")
		for row in cursor.fetchall():
			print(row)

			btns = [row]
			xxx = 0
			yyy = 80
			for bt in btns:
				com = lambda x=bt: logicalc(xxx)
				ass = Button(DiaWindow, text=bt, bg="#FFF", font=("Exo", 12), command=com).place(x=xxx, y=yyy,width=180,height=43)
			xxx += 117
			if xxx > 400:
				xxx = 10
				yyy += 81
			

		

	BBB()
#========================================================================================================




#===============================Інфо-вікно після успішної реєстрації=====================================
def Zareg():
	ZarWin = Toplevel()
	ZarWin.title("Зареєстровано!")
	ZarWin.geometry("300x70")
	ZarWin.configure(bg='#1f1f2e')
	ZarWin.resizable(width=False, height=False)

	Success_Mess = Label(ZarWin, text="Вітаю! Ви успішно зареєструвались!", font=("Helvetica", 10))
	Success_Mess.place(x=34, y=16)
#========================================================================================================




#===============================Вікно реєстрації=========================================================
def OpenReg():
	Lowroot = Toplevel()
	Lowroot.title("Реєстрація")
	Lowroot.geometry("300x300")
	Lowroot.configure(bg = '#1f1f2e')
	Lowroot.resizable(width=False, height=False)

	def reg(*args):  # Вводить нового користувача, виводить вікно про успішну реєстрацію і Діалогове вікно
		e_code = i_code.get()
		e_name = i_name.get()
		e_price = i_price.get()
		Lowroot = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='bazadate')
		#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
		cursor = Lowroot.cursor()

		cursor.execute("INSERT INTO users(Login, Password, UserName) VALUES(%s, %s, %s)", (e_code, e_name, e_price))
		Lowroot.commit()
		Zareg()
		Dialog()


	def VVV():  # Виводить усю таблицю Юзерів
		db = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='bazadate')
		#mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
		cur = db.cursor()
		cur.execute('SELECT * FROM users;')
		for row in cur.fetchall():
			print(*row)
	

	i_code = StringVar()
	i_name = StringVar()
	i_price = StringVar()


	#====================== Елементи вікна реєстрації ===========================
	reg_lbl = Label(Lowroot, text="REGISTRATION", font=("Helvetica", 15))
	reg_lbl.place(x=85, y=10)

	login_lbl = Label(Lowroot, text="Login", font=("Helvetica", 10))
	login_lbl.place(x=70, y=48)

	password_lbl = Label(Lowroot, text = "Password", font = ("Helvetica", 10))
	password_lbl.place(x=44, y=73)

	user_name_lbl = Label(Lowroot, text = "UserName", font = ("Helvetica", 10))
	user_name_lbl.place(x = 40, y = 98)

	login_edit = Entry(Lowroot, width=15, textvariable = i_code)
	login_edit.place(x = 120, y = 50)

	password_edit = Entry(Lowroot, width = 15, textvariable = i_name)
	password_edit.place(x = 120, y = 75)

	user_name_edit = Entry(Lowroot, width=15, textvariable = i_price)
	user_name_edit.place(x=120, y=100)
	

	insert = Button(Lowroot, text="Зареєструвати", width=20, height=2, bg="white", fg="black", command = lambda:[reg(), quit()])
	#insert.bind("<Button-1>")
	insert.place(x=85, y=130)


	btn_3 = Button(Lowroot,
	             text="Вивести БД",
	             width=20, height=2,
	             bg="white", fg="black", command = VVV)
	#btn_3.bind("<Button-1>")
	btn_3.place(x=85, y=180)
	#==============================================================================


	def quit():
		Lowroot.destroy()

	b = Button(Lowroot, text = 'Quit', command = quit, width = 42, height = 1)
	b.place(x=0, y=274)
#========================================================================================================








'''#=============================FWindows======================================================================
def FWindows():
	FWin = Toplevel()
	FWin.title("Log in")									
	FWin.geometry("300x300")						
	FWin.configure(bg = '#1f1f2e')	
	FWin.resizable(width = False, height = False)

	

	i_code = StringVar()
	i_name = StringVar()
#========================================================================================================'''



#===============================Функція здійснення входу?================================================
def Log_in(*args):
	e_code = i_code.get()
	e_name = i_name.get()
	db = mysql.connector.connect(user='root', password='root',
	                              host='127.0.0.1',
	                              database='bazadate')
	# mysql.connector.connect('127.0.0.1', 'root', 'root', 'bazadate')
	cursor = db.cursor()

	cursor.execute(f"SELECT Login, Password FROM users WHERE Login = '{e_code}' AND Password = '{e_name}'")
	if cursor.fetchone() is None:
		Log_in_RightWrong()
	else:
		Dialog()
	db.close()
#========================================================================================================






#======================= Основне вікно ==========================
root= Tk()														#
root.title("Log in")											#
root.geometry("300x300")											#
root.configure(bg = '#1f1f2e')									#
root.resizable(width = False, height = False)
#================================================================

i_dialog = StringVar()
i_code = StringVar()
i_name = StringVar()

#====================== Елементи основного вікна ==============================================
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
		width=20,
		height=2,
		bg="white", fg="black", command = Log_in)
Log_in.bind("<Button-1>")
Log_in.place(x = 85, y = 130)


Reg = Button(root,
		text="Registration",
		width=10, height=1,
		bg="white", fg="black", command = OpenReg)
Reg.place(x=115, y=180)
#=================================================================================================


def quit(): # Функція виходу з основного вікна
	root.destroy()


'''class Main(Frame):
		def __init__(self, wind):
			super(Main, self).__init__(wind)
			self.build()

		def build(self):
	        
	                        btns = [
	                        "C", "DEL", "*", "=",
	                        "1", "2", "3", "/",
	                        "4", "5", "6", "+",
	                        "7", "8", "9", "-",
	                        "(", "0", ")", "X^2"]
	                        x = 10
	                        y = 140
	                        for bt in btns:
	                        	com = lambda x=bt: self.logicalc(x)
	                        	Button(text=bt, bg="#FFF",
	                        		font=("Times New Roman", 15),
	                        		command=com).place(x=x, y=y,
	                        		width=115, height=79)
	                        	x += 117
	                        	if x > 400:
	                        		x = 10
	                        		y += 81'''


button = Button(root, text = 'Quit', command = quit, width = 42, height = 1)
button.place(x = 0, y = 274)
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