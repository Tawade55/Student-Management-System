from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import ImageTk,Image
import ast
from sqlite3 import *
from tkinter.scrolledtext import *
from getpass import getpass
from pwinput import pwinput
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import *
#from firebase import firebase
from tkinter import scrolledtext


mw=Tk()
mw.title("Student Management System by Vivek")
mw.geometry("925x700+50+50")
mw.configure(bg="#fff")



canvas=Canvas(mw,width=1700,height=700)
image=ImageTk.PhotoImage(Image.open("C:\Python Program's Practice\Student Management System\\front1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


frame=Frame(mw,width=650,height=360,bg="#FFFFEF")
frame.place(x=650,y=10)

heading=Label(frame,text="Student Management System",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",24,"bold"))
heading.place(x=100,y=5)  

def f1():
	siw.deiconify()
	mw.withdraw()

def f2():
	siw.withdraw()
	mw.deiconify()

def f3():
	adw.deiconify()
	mw.withdraw()

def f4():
	adw.withdraw()
	mw.deiconify()

def f5():
	amw.deiconify()
	mw.withdraw()

def f6():
	mw.deiconify()
	amw.withdraw()
def f7():
	mw.withdraw()
	usr.deiconify()

def f8():
	simw.deiconify()
	mw.withdraw
def f9():
	simw.withdraw()
	mw.deiconify()

def f10():
	aw.deiconify()
	simw.withdraw()
def f11():
	aw.withdraw()
	mw.deiconify()

"""firebaseConfig = {
  "apiKey": "AIzaSyARdlc7M4rBuug0Iomv4TiEGOtVesDLwM0",
  "authDomain": "sms-f5a53.firebaseapp.com",
  "databaseURL": "https://sms-f5a53-default-rtdb.firebaseio.com",
  "projectId": "sms-f5a53",
  "storageBucket": "sms-f5a53.appspot.com",
  "messagingSenderId": "980251468368",
  "appId": "1:980251468368:web:6bdb2654d30e65679de755"
};


StudentMS = pyrebase.initialize_app(firebaseConfig)
db = sms.database()"""

# Set up Firebase credentials
cred = credentials.Certificate("C:\Python Program's Practice\Student Management System\StudentMSServiceKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://studentms-f5ece-default-rtdb.firebaseio.com"})
ref=db.reference('StudentMS')
def f12():
	try:
		rno = aw_roll_ent.get()
		if not rno.isdigit() and int(rno)<=0:
			raise ValueError()
		elif int(rno)<1:
			raise IndexError("Rno should be minimum one")
		
		name = aw_name_ent.get()
		if not all(x.isalpha() or x.isspace() for x in name):
			raise NameError("Name must be combination of Alphabets only")
		
		name=aw_name_ent.get()
		if len(name)==0:
			raise TypeError("Length of name must be  greater than or equal to 2")
		
		year = aw_year_ent.get()
		if not all(x.isalpha() or x.isspace() or x.isdigit() for x in year):
			raise TabError("Year should contain either alphabets or digits and should not be Null")
		if len(year)==0:
			raise AttributeError(" Year should not be blank")
		
		department = aw_dept_ent.get()
		if not all(x.isalpha() or x.isspace() for x in department):
			raise ReferenceError("Department should contain only alphabets and should not be Null")
	 	#elif len(department)==0:
			#raise SpaceError("Department Should not be Null")	


		if rno in ref.get():
			messagebox.showwarning("Warning","Roll no Already Exists")
		else:
			data = {'Name': name, 'Roll No': rno, 'Year':year, 'Department':department}
			ref.child(rno).set(data)
			messagebox.showinfo("Success","Data added successfully!")
			
			aw_roll_ent.delete(0,END)
			aw_name_ent.delete(0,END)
			aw_year_ent.delete(0,END)
			aw_dept_ent.delete(0,END)
			aw_roll_ent.focus()	
	except ValueError as e:	
		showerror("Issue","Rno should be integer only and not blank")
		aw_roll_ent.delete(0,END)
	except IndexError as e:
		showerror("Issue","Rno should be minimum one")
		aw_roll_ent.delete(0,END)
	except NameError as e:
		showerror("Issue","Name must be combination of Alphabets only")
		aw_name_ent.delete(0,END)
	except TypeError as e:
		showerror("Issue","Length of name must be  greater than or equal to 2")
		aw_name_ent.delete(0,END)
	except TabError as e:
		showerror("Issue","Year should contain either alphabets or digits and should not be Null")
		aw_year_ent.delete(0,END)
	except AttributeError as e:
		showerror("Issue","Year should not be blank")
		aw_year_ent.delete(0,END)
	except ReferenceError as e:
		showerror("issue","Department should contain only alphabets and should not be Null")
		aw_dept_ent.delete(0,END)
	#except SpaceError as e:
		#showerror("issue","Department Should not be Null")
	
	#except Exception as e:
		#showerror("Issue","Rno Already Exists")
	"""finally:
		
		aw_roll_ent.delete(0,END)
		aw_name_ent.delete(0,END)
		aw_year_ent.delete(0,END)
		aw_dept_ent.delete(0,END)
		aw_roll_ent.focus()"""	


	
def view_data():
	amw.withdraw()
	vw.deiconify()
	
	data = ref.get()

	if data:
		for key, value in data.items():
			text_widget.insert(tk.END, f"Roll No: {key}\n")
			text_widget.insert(tk.END, f"Data: {value}\n")
			text_widget.insert(tk.END, "\n")
	else:
		text_widget.insert(tk.END, "No data available")
		
		
		
def f14():
	vw.withdraw()
	amw.deiconify()


# Set up Firebase credentials
#cred = credentials.Certificate("C:\Python Program's Practice\Student Management System\StudentMSServiceKey.json")
#firebase_admin.initialize_app(cred, {'databaseURL': "https://studentms-f5ece-default-rtdb.firebaseio.com"})

def f15():

	try:
		rno = uw_roll_ent.get()
		if not rno.isdigit() and int(rno)<=0:
			raise ValueError()
		elif int(rno)<1:
			raise IndexError("Rno should be minimum one")
		
		name = uw_name_ent.get()
		if not all(x.isalpha() or x.isspace() for x in name):
			raise NameError("Name must be combination of Alphabets only")
		
		name=uw_name_ent.get()
		if len(name)==0:
			raise TypeError("Length of name must be  greater than or equal to 2")
		
		year = uw_year_ent.get()
		if not all(x.isalpha() or x.isspace() or x.isdigit() for x in year):
			raise TabError("Year should contain either alphabets or digits and should not be Null")
		if len(year)==0:
			raise AttributeError(" Year should not be blank")
		
		department = uw_dept_ent.get()
		if not all(x.isalpha() or x.isspace() for x in department):
			raise ReferenceError("Department should contain only alphabets and should not be Null")
	 	#if len(department)==2:
			#raise ReferenceError("Department Should not be Null")	

		if rno in ref.get():
			data = {'Name': name, 'Roll No': rno, 'Year': year, 'Department':department}
			ref.child(rno).update(data)
			messagebox.showinfo("Success","Data updated successfully!")
			
			uw_roll_ent.delete(0,END)
			uw_name_ent.delete(0,END)
			uw_year_ent.delete(0,END)
			uw_dept_ent.delete(0,END)
			uw_roll_ent.focus()	
		else:
			messagebox.showwarning("Warning","Record does not exists")

	except ValueError as e:	
		showerror("Issue","Rno should be integer only and not blank")
		uw_roll_ent.delete(0, END)
	except IndexError as e:
		showerror("Issue","Rno should be minimum one")
		uw_roll_ent.delete(0, END)
	except NameError as e:
		showerror("Issue","Name must be combination of Alphabets only")
		uw_name_ent.delete(0, END)
	except TypeError as e:
		showerror("Issue","Length of name must be  greater than or equal to 2")
		uw_name_ent.delete(0, END)
	except TabError as e:
		showerror("Issue","Year should contain either alphabets or digits and should not be Null")
		uw_year_ent.delete(0, END)
	except AttributeError as e:
		showerror("Issue","Year should not be blank")
		uw_year_ent.delete(0, END)
	except ReferenceError as e:
		showerror("issue","Department should contain only alphabets and should not be Null")
		uw_dept_ent.delete(0, END)
	except Exception as e:
		showerror("Issue","Rno Already Exists")
		uw_roll_ent.delete(0,END)
	#finally:
		
		#uw_roll_ent.delete(0,END)
		#uw_name_ent.delete(0,END)
		#uw_year_ent.delete(0,END)
		#uw_dept_ent.delete(0,END)
		#uw_roll_ent.focus()	

def confirm_update():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to Update the data?")
    if result == YES:
        f15()
    else:
        # User clicked No, do nothing
        pass



def f16():
	uw.withdraw()
	amw.deiconify()
def f17():
	uw.deiconify()
	amw.withdraw()

def f18():
	dw.deiconify()
	amw.withdraw()
def f19():
	dw.withdraw()
	amw.deiconify()

def f20():
	
	try:
	
		rno = dw_roll_ent.get()
		if not rno.isdigit() and int(rno)<=0:
			raise ValueError()
		elif int(rno)<1:
			raise IndexError("Rno should be minimum one")
		if rno in ref.get():
			ref.child(rno).delete()
			messagebox.showinfo("Success","Data deleted successfully!")
		else:
			messagebox.showwarning("Warning","Data Does not Exists")	
	except ValueError as e:
		showerror("Issue","Roll no should be integer only and not blank")
	except IndexError as e:
		showerror("Issue","Rno should be minimum one")

	finally:
		dw_roll_ent.delete(0,END)
		dw_roll_ent.focus()


def confirm_delete():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to delete the data?")
    if result == YES:
        f20()
    else:
        # User clicked No, do nothing
        pass

def close_mw():
	result = messagebox.askyesno("Confirmation", "Are you sure you want to close the window?")
	if result == YES:
		mw.quit() 
	
	
		
siw=Tk()
siw.title("Sign In")
siw.geometry("925x925+300+200")
siw.configure(bg="white")



def signin():
	
	username=userl.get()
	password=codel.get()
	
	if username=="Vivek" and password=="*****":
		
		#siw=Toplevel(mw)
		simw.deiconify()
		siw.withdraw()
		
	elif username!="Vivek" and password!="*****":
		messagebox.showerror("Invalid","Invalid Username or Password")

	elif password!="*****":
		messagebox.showerror("Invalid","Invalid Password")

	elif username!="Vivek":
		messagebox.showerror("Invalid","Invalid Username")



def on_enter(e):
	userl.delete(0, "end")
def on_leave(e):
	name=userl.get()
	if name=="":
		userl.insert(0,"Username")

userl = Entry(siw,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
userl.place(x=430,y=100)
userl.insert(0,"Username")
userl.bind("<FocusIn>",on_enter)
userl.bind("<FocusOut>",on_leave)

Frame(siw,width=295,height=2,bg="black").place(x=425,y=127)
################################################################

def on_enter(e):
	codel.delete(0, "end")
def on_leave(e):
	name=codel.get()
	if name=="":
		codel.insert(0,"Password")





codel = Entry(siw,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11),show='*')
codel.place(x=430,y=170)
codel.insert(0,"Password")
codel.bind("<FocusIn>",on_enter)
codel.bind("<FocusOut>",on_leave)
Frame(siw,width=295,height=2,bg="black").place(x=425,y=197)
##############################################################
siw_lab=Label(siw,text="Sign In Here ",font=("Times New Roman",40,"bold"))
siw_lab.pack(pady=10)

siw_signin_button=Button(siw,text="Sign in",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=signin)
siw_signin_button.place(x=430,y=230)
siw_back_button=Button(siw,text="Back",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=f2) 
siw_back_button.place(x=430,y=300)
siw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#siw.wm_iconphoto(False, photo)		


simw=Toplevel(siw)
simw.title("Menu")
simw.geometry("925x925+50+50")
simw.configure(bg="#8B8B69")




simw_stu_btn=Button(simw,text="Add Student Information",font=("Times New Roman",30,"bold"),width=20,height=2,bg="#57a1f8",fg="white",command=f10)
simw_exit_btn=Button(simw,text="Exit",font=("Times New Roman",40,"bold"),bg="#57a1f8",fg="white",command=f9)
simw_stu_btn.pack(pady=10)		
simw_exit_btn.pack(pady=10)

simw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#simw.wm_iconphoto(False, photo)


aw=Toplevel(simw)
aw.title("Student Information")
aw.geometry("925x925+50+50")
aw.configure(bg="#FFFFEB")


aw_roll_lab=Label(aw,text="Enter Student Roll No",font=("Times New Roman",23,"bold"))
aw_roll_ent=Entry(aw,font=("Times New Roman",23,"bold"))
aw_name_lab=Label(aw,text="Enter Student Name",font=("Times New Roman",23,"bold"))
aw_name_ent=Entry(aw,font=("Times New Roman",23,"bold"))
aw_year_lab=Label(aw,text="Enter Current Year of Studying",font=("Times New Roman",23,"bold"))
aw_year_ent=Entry(aw,font=("Times New Roman",23,"bold"))
aw_dept_lab=Label(aw,text="Enter Student Department",font=("Times New Roman",23,"bold"))
aw_dept_ent=Entry(aw,font=("Times New Roman",23,"bold"))
aw_sub_btn=Button(aw,text="Submit",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=f12)
aw_exit_btn=Button(aw,text="Exit",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=f11)

aw_roll_lab.pack(pady=10)
aw_roll_ent.pack(pady=10)
aw_name_lab.pack(pady=10)
aw_name_ent.pack(pady=10)
aw_year_lab.pack(pady=10)
aw_year_ent.pack(pady=10)
aw_dept_lab.pack(pady=10)
aw_dept_ent.pack(pady=10)
aw_sub_btn.pack(pady=10)
aw_exit_btn.pack(pady=10)




aw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#aw.wm_iconphoto(False, photo)



######################### Admin Area #####################################


adw=Tk()
adw.title("Admin Login")
adw.geometry("925x925+300+200")
adw.configure(bg="white")
				


def admin():
	
	username=user.get()
	password=code.get()
	
	if username=="Rob" and password=="****":
		
		adw.withdraw()
		amw.deiconify()
		#adw=Toplevel(amw)
		
		
		
	elif username!="Rob" and password!="****":
		messagebox.showerror("Invalid","Invalid Username or Password")

	elif password!="****":
		messagebox.showerror("Invalid","Invalid Password")

	elif username!="Rob":
		messagebox.showerror("Invalid","Invalid Username")



def on_enter(e):
	user.delete(0, "end")
def on_leave(e):
	name=user.get()
	if name=="":
		user.insert(0,"Username")

user = Entry(adw,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=430,y=100)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(adw,width=295,height=2,bg="black").place(x=425,y=127)
################################################################

def on_enter(e):
	code.delete(0, "end")
def on_leave(e):
	name=code.get()
	if name=="":
		code.insert(0,"Password")





code = Entry(adw,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11),show='*')
code.place(x=430,y=170)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(adw,width=295,height=2,bg="black").place(x=425,y=197)





#################  Sign Up   ###################


usr=Toplevel(mw)
usr.geometry("925x925+300+200")
usr.title("Sign Up")


def signup():
	username=users.get()
	password=codes.get()
	confirm_password=confirm_code.get()
	
	if password==confirm_password:
		usr.withdraw()
		siw.deiconify()
		try:
			file=open("datasheet.txt","r+")
			d=file.read()
			r=ast.literal_eval(d)

			dict2={username:password}
			r.update(dict2)
			file.truncate(0)
			file.close()
			
			file=open("datasheet.txt","w")
			w=file.write(str(r))
			
			messagebox.showinfo("signup","Successfully Sign up")
		except:
			file=open("datasheet.txt","w")
			pp=str({"Username":"password"})
			file.write(pp)
			file.close()
		else:
			messagebox.showerror("Invalid","Both Password should match")



def on_enter(e):
	users.delete(0, "end")
def on_leave(e):
	if users.get()=="":
		users.insert(0,"Username")




users=Entry(usr,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
users.place(x=430,y=100)
users.insert(0, "Username")
users.bind("<FocusIn>",on_enter)
users.bind("<FocusOut>",on_leave)

Frame(usr,width=295,height=2,bg="black").place(x=425,y=127)
############################################################

def on_enter(e):
	codes.delete(0, "end")
def on_leave(e):
	if code.get()=="":
		codes.insert(0,"Username")




codes=Entry(usr,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11),show='*')
codes.place(x=430,y=170)
codes.insert(0, "Password")
codes.bind("<FocusIn>",on_enter)
codes.bind("<FocusOut>",on_leave)

Frame(usr,width=295,height=2,bg="black").place(x=425,y=197)
###########################################################

def on_enter(e):
	confirm_code.delete(0, "end")
def on_leave(e):
	if confirm_code.get()=="":
		confirm_code.insert(0,"Confirm Password")




confirm_code=Entry(usr,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11),show='*')
confirm_code.place(x=430,y=240)
confirm_code.insert(0, "Confirm Password")
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)

Frame(usr,width=295,height=2,bg="black").place(x=425,y=267)
###############################################################
usr_lab=Label(usr,text="Hey Champ Sign Up Here ",font=("Times New Roman",40,"bold"))
usr_lab.pack(pady=10)
usr_btn=Button(usr,width=39,pady=7,text="Sign Up",bg="#57a1f8",fg="white",border=0,command=signup)
usr_btn.place(x=425,y=300)


usr.withdraw()



#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#usr.wm_iconphoto(False, photo)























adw_lab=Label(adw,text="Admin Login ",font=("Times New Roman",40,"bold"))
adw_lab.pack(pady=10)

adw_admin_button=Button(adw,text="Sign in",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=admin)
adw_admin_button.place(x=430,y=230)
adw_back_button=Button(adw,text="Back",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command=f4) 
adw_back_button.place(x=430,y=300)
adw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#adw.wm_iconphoto(False, photo)

amw=Tk()
amw.title("Menu")
amw.geometry("925x925+50+50")
amw.configure(bg="#EEEED5")


amw_vw_btn=Button(amw,text="View Student Information",font=("Times New Roman",23,"bold"),width=20,height=2,bg="#57a1f8",fg="white",command=view_data)
amw_uw_btn=Button(amw,text="Update Student Information",font=("Times New Roman",23,"bold"),width=20,height=2,bg="#57a1f8",fg="white",command=f17)
amw_dw_btn=Button(amw,text="Delete Student Information",font=("Times New Roman",23,"bold"),width=20,height=2,bg="#57a1f8",fg="white",command=f18)
#amw_save_btn=Button(amw,text="Save",font=("Times New Roman",23,"bold"),width=20,height=2)
amw_back_btn=Button(amw,text="Back",font=("Times New Roman",23,"bold"),width=20,height=2,bg="#57a1f8",fg="white",command=f6)

amw_vw_btn.pack(pady=10)
amw_uw_btn.pack(pady=10)
amw_dw_btn.pack(pady=10)
#amw_save_btn.pack(pady=10)
amw_back_btn.pack(pady=10)
amw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#amw.wm_iconphoto(False, photo)

vw=Toplevel(amw)
vw.title("View Data")
vw.geometry("925x925+50+50")
vw.configure(bg="#7F7FFF")

text_widget = scrolledtext.ScrolledText(vw)
text_widget.pack(fill=tk.BOTH, expand=False)


#vw_lab=Label(vw,text="data_with_newlines",justify="left",font=("Times New Roman",25,"bold"))
#vw_st_data=ScrolledText(vw,width=200,height=8,font=("Times New Roman",20,"bold","italic"))
vw_btn_back=Button(vw,text="Back",font=("Times New Roman",20,"bold"),bg="#57a1f8",fg="white",command=f14)
# Initialize Tkinter
#root = Tk()



#vw_lab.pack(pady=10)
#vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
#data_label.pack()

vw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#vw.wm_iconphoto(False, photo)


uw=Toplevel(amw)
uw.title("Update Data")
uw.geometry("925x925+50+50")
uw.configure(bg="#EEEEE8")


uw_lab=Label(uw,text="Update Student Information",font=("Times New Roman",25,"bold"))
uw_roll_lab=Label(uw,text="Enter Student Roll No",font=("Times New Roman",23,"bold"))
uw_roll_ent=Entry(uw,font=("Times New Roman",23,"bold"))
uw_name_lab=Label(uw,text="Enter Name to be Updated",font=("Times New Roman",23,"bold"))
uw_name_ent=Entry(uw,font=("Times New Roman",23,"bold"))
uw_year_lab=Label(uw,text="Enter the year to be Updated",font=("Times New Roman",23,"bold"))
uw_year_ent=Entry(uw,font=("Times New Roman",23,"bold"))
uw_dept_lab=Label(uw,text="Enter Department name to be Updated",font=("Times New Roman",23,"bold"))
uw_dept_ent=Entry(uw,font=("Times New Roman",23,"bold"))
uw_save_btn=Button(uw,text="Save",font=("Times New Roman",23,"bold"),bg="#57a1f8",fg="white",command= confirm_update)
#vw_st_data=ScrolledText(vw,width=200,height=8,font=("Times New Roman",20,"bold","italic"))
uw_btn_back=Button(uw,text="Back",font=("Times New Roman",20,"bold"),bg="#57a1f8",fg="white",command=f16)

uw_lab.pack(pady=10)
#uw_st_data.pack(pady=10)
uw_roll_lab.pack(pady=10)
uw_roll_ent.pack(pady=10)
uw_name_lab.pack(pady=10)
uw_name_ent.pack(pady=10)
uw_year_lab.pack(pady=10)
uw_year_ent.pack(pady=10)
uw_dept_lab.pack(pady=10)
uw_dept_ent.pack(pady=10)
uw_save_btn.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#uw.wm_iconphoto(False, photo)


dw=Toplevel(amw)
dw.geometry("925x925+50+50")
dw.title("Delete Data")
dw.configure(bg="#FFFFB9")



dw_lab=Label(dw,text="Delete Student Information",font=("Times New Roman",25,"bold"))
dw_roll_lab=Label(dw,text="Enter Student Roll no to be Deleted",font=("Times New Roman",23,"bold"))
dw_roll_ent=Entry(dw,font=("Times New Roman",23,"bold"))
dw_save_btn=Button(dw,text="save",font=("Times New Roman",25,"bold"),bg="#57a1f8",fg="white",command=confirm_delete)
dw_back_btn=Button(dw,text="Back",font=("Times New Roman",25,"bold"),bg="#57a1f8",fg="white",command=f19)

dw_lab.pack(pady=10)
dw_roll_lab.pack(pady=10)
dw_roll_ent.pack(pady=10)
dw_save_btn.pack(pady=10)
dw_back_btn.pack(pady=10)
dw.withdraw()

#ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
#photo = ImageTk.PhotoImage(ico)
#dw.wm_iconphoto(False, photo)

mw_button=Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=f1).place(x=200,y=100)
mw_button=Button(frame,width=39,pady=7,text="Admin",bg="#57a1f8",fg="white",border=0,command=f3).place(x=200,y=200)
mw_button=Button(frame,width=39,pady=7,text="Sign Up",bg="#57a1f8",fg="white",border=0,command=f7).place(x=200,y=300)
#mw.withdraw()


mw.protocol("WM_DELETE_WINDOW", close_mw)

ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\download.png')
photo = ImageTk.PhotoImage(ico)
mw.wm_iconphoto(False, photo)


mw.mainloop()
