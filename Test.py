from tkinter import *
'''
window = Tk()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text=input_get)
    input_user.set('')
    label.pack()
    return "break"

frame = Frame(window, width=300, height=300)
frame.pack_propagate(False) # prevent frame to resize to the labels size
input_field.bind("<Return>", enter_pressed)
frame.pack()

window.mainloop()


Entry(DiaWindow, text = ('['+alias+'] -  '+ input_user), width = 135)
				input_field.place(x = 150, y = 620, height= 30) 




	ggg =['5', '9', '56', '09', '67']
	yyy = 20
	for i in range(len(ggg)):
		ButEd = Button(DiaWindow,   # Стрілочка
						text = ggg[i],
						width=6, height=2,
						bg="white", fg="black")
		ButEd.place(x=549, y=yyy)
		yyy = yyy + 100


		yyy = 20
		for row in cursor.fetchall():
			d = row
			#return[d]
			for i in range(len(d)):
				ButEd = Button(DiaWindow,   # Стрілочка
							text = d[i],
							width=6, height=2,
							bg="white", fg="black")
				ButEd.place(x=549, y=yyy)
				yyy = yyy + 100


'''


 
root = Tk()
root.maxsize(900,600)

scrollderoot = Scrollbar(orient="vertical", command=root.yview)
scrollderoot.grid(column=5, row=0, sticky='ns', in_=root) #instead of number 5, set the column as the expected one for the scrollbar. Sticky ns will might be neccesary.
root.configure(yscrollcommand=scrollderoot.set)

circus()#calls the function to set up everything

root.mainloop()