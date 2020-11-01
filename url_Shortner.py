__author__ = "red ant"

# imports ..
# ---------- tkinter libraries ------------
from tkinter import*
from tkinter.messagebox import askyesno
# ----------- other important libraries ---
from copypaste import copy, paste
from pyshorteners import Shortener
# ------------------------------------------

# create object
app = Tk()
# -------- configurations ----
app.geometry("560x330")
app.title("Url Shortener")
app.configure(background="#97DBAE")
# -------- shorten object ---------
short = Shortener()
# ----- Frames ----
frame1_for_title = Frame(app, bg="#CDE4AD")
frame1_for_title.pack(side=TOP, pady=5)

# ------
app_title = Label(frame1_for_title, text="URL SHORTENER", fg="#fff", bg="#CDE4AD", font=("courier", 30, "bold"))
app_title.grid()
# ------

frame2_input_and_paste = Frame(app, bg="#97DBAE")
frame2_input_and_paste.pack(side=TOP, pady=5)

frame3_shorten_btn = Frame(app, bg="#97DBAE")
frame3_shorten_btn.pack(side=TOP, pady=5)

frame4_text_field = Frame(app, bd=2, bg="#97DBAE", relief=SUNKEN)
frame4_text_field.pack(side=TOP, pady=5)

# ----- Functions --------

def shortener():
	global short
	show_shortened_text_field.delete("1.0", END)
	url_pasted = url_input_entry_field.get()
	url_short = short.tinyurl.short(url_pasted)
	show_shortened_text_field.insert("1.0", url_short)

def pasted():
	copyed = paste()
	url_input_entry_field.insert(0, copyed)

def delete():
	url_input_entry_field.delete(0, END)

def exit():
	iExit = askyesno("Attention", "Do You Wanna Quit")
	if iExit > 0:
		app.destroy()

def copyed():
	geted = show_shortened_text_field.get("1.0", END)
	copyed = copy(geted)

# -------- main widgets ----
url_input_entry_field = Entry(frame2_input_and_paste, width=50)
url_input_entry_field.grid(row=0, column=1, ipady=6)
# ---------- buttons --------
paste_btn = Button(frame2_input_and_paste, text="paste", width=10, height=2, command=pasted)
paste_btn.grid(row=0, column=0, padx=2)
# -----------
shorten_btn = Button(frame3_shorten_btn, text="Shorten", width=15, height=2, command=shortener)
shorten_btn.grid(row=0, column=0, padx=2)
# ---------
clear_btn = Button(frame3_shorten_btn, text="Delete", width=15, height=2, command=delete)
clear_btn.grid(row=0, column=1, padx=2)
# ---------
quit_btn = Button(frame3_shorten_btn, text="Quit", width=15, height=2, command=exit)
quit_btn.grid(row=0, column=2, padx=2)
# ---------- text field -----
show_shortened_text_field = Text(frame4_text_field, width=50, height=7)
show_shortened_text_field.grid(row=0, column=0)
# -----
copy_shortened_btn = Button(frame4_text_field, text="Copy", width=15, height=2, command=copyed)
copy_shortened_btn.grid(row=1, column=0, pady=5)
# ---------------------------
app.mainloop()