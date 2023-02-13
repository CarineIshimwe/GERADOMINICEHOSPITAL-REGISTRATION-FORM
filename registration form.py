from tkinter import *
from tkinter import *


# declare the window
window = Tk()
# set window title
window.title("GERADOMINIC E-HOSPITAL RWANDA")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='skyblue')
def getvals():
    print('registration successfuly')

Label(window,text="\tGERADOMINIC E- HOSPITAL RWANDA REGISTRATION FORM\n",font="ar 10 bold").grid(row=1,column=3)
Firstname=Label(window,text='Firstname\n',font="ar 10 bold",width=20)
Firstname.place(x=90,y=53)
Middlename=Label(window,text='Middlename\n',font="ar 10 bold",width=20)
Middlename.place(x=90,y=53)
Lastname=Label(window,text='Lastname\n',font="ar 10 bold",width=20)
Gender=Label(window,text='Gender',width=20,font='ar 10 bold')
Dateofbirth=Label(window,text='Dateofbirth\n',font="ar 10 bold",width=20)
Your_identification_number=Label(window,text='Your_identification_number\n',font="ar 12 bold",width=25)
email=Label(window,text='email\n',font="ar 10 bold",width=20)
phonenumber=Label(window,text='phonenumber\n',font="ar 10 bold",width=20)
password=Label(window,text='password\n',font="ar 10 bold",width=20)
Confirm_password=Label(window,text='Confirm_password\n',font="ar 10 bold",width=20)
province=Label(window,text='province\n',font="ar 10 bold",width=20)
Sector=Label(window,text='Sector\n',font="ar 10 bold",width=20)
district=Label(window,text='district\n',font="ar 10 bold",width=20)
cell=Label(window,text='cell\n',font="ar 10 bold",width=20)
village=Label(window,text='village\n',font="ar 10 bold",width=20)
Id_thehead_of_family=Label(window,text='Id_thehead_of_family\n',font="ar 10 bold",width=20)
insurance_name=Label(window,text='insurance_name\n',font="ar 10 bold",width=20)
Firstname.grid(row=2,column=3)
Middlename.grid(row=3,column=3)
Lastname.grid(row=4,column=3)
Gender.grid(row=5,column=3)
Dateofbirth.grid(row=6,column=3)
Your_identification_number.grid(row=7,column=3)
email.grid(row=8,column=3)
phonenumber.grid(row=9,column=3)
password.grid(row=10,column=3)
Confirm_password.grid(row=11,column=3)
province.grid(row=12,column=3)
Sector.grid(row=13,column=3)
district.grid(row=14,column=3)
cell.grid(row=15,column=3)
village.grid(row=16,column=3)
Id_thehead_of_family.grid(row=17,column=3)
insurance_name.grid(row=18,column=3)
Firstnamevalue=StringVar
Middlenamevalue=StringVar
Lastnamevalue=StringVar
Dateofbirthvalue=StringVar
Your_identification_numbervalue=StringVar
emailvalue=StringVar
phonenumbervalue=StringVar
passwordvalue=StringVar
Confirm_passwordvalue=StringVar
provincevalue=StringVar
Sectorvalue=StringVar
districtvalue=StringVar
cellvalue=StringVar
villagevalue=StringVar
Id_thehead_of_familyvalue=StringVar
insurance_namevalue=StringVar
checkvalue=IntVar
malevalue=IntVar
femalevalue=IntVar
Firstnameentry=Entry(window,textvariable=Firstnamevalue,font="ar 20 bold")
Middlenameentry=Entry(window,textvariable=Middlenamevalue,font="ar 20 bold")
Lastnameentry=Entry(window,textvariable=Lastnamevalue,font="ar 20 bold")
maleentry=Radiobutton(window,text='Male',padx=5,variable=malevalue,value=1)
femaleentry=Radiobutton(window,text='Female',padx=20,variable=femalevalue,value=2)
Dateofbirthentry=Entry(window,textvariable=Dateofbirthvalue,font="ar 20 bold")
Your_identification_numberentry=Entry(window,textvariable=Your_identification_numbervalue,font="ar 20 bold")
emailentry=Entry(window,textvariable=emailvalue,font="ar 20 bold")
phonenumberentry=Entry(window,textvariable=phonenumbervalue,font="ar 20 bold")
passwordentry=Entry(window,textvariable=passwordvalue,font="ar 20 bold")
Confirm_passwordentry=Entry(window,textvariable=Confirm_passwordvalue,font="ar 20 bold")
provinceentry=Entry(window,textvariable=provincevalue,font="ar 20 bold")
Sectorentry=Entry(window,textvariable=Sectorvalue,font="ar 20 bold")
districtentry=Entry(window,textvariable=districtvalue,font="ar 20 bold")
cellentry=Entry(window,textvariable=cellvalue,font="ar 20 bold")
villageentry=Entry(window,textvariable=villagevalue,font="ar 20 bold")
Id_thehead_of_familyentry=Entry(window,textvariable=Id_thehead_of_familyvalue,font="ar 20 bold")
insurance_nameentry=Entry(window,textvariable=insurance_namevalue,font="ar 20 bold")
Firstnameentry.grid(row=2,column=4)
Middlenameentry.grid(row=3,column=4)
Lastnameentry.grid(row=4,column=4)
maleentry.grid(row=5,column=4)
femaleentry.grid(row=5,column=5)
Dateofbirthentry.grid(row=6,column=4)
Your_identification_numberentry.grid(row=7,column=4)
emailentry.grid(row=8,column=4)
phonenumberentry.grid(row=9,column=4)
passwordentry.grid(row=10,column=4)
Confirm_passwordentry.grid(row=11,column=4)
provinceentry.grid(row=12,column=4)
Sectorentry.grid(row=13,column=4)
districtentry.grid(row=14,column=4)
cellentry.grid(row=15,column=4)
villageentry.grid(row=16,column=4)
Id_thehead_of_familyentry.grid(row=17,column=4)
insurance_nameentry.grid(row=18,column=4)
checkbtn=Checkbutton(text='Remember Me?',variable=checkvalue,font="ar 10 bold")
checkbtn.grid(row=19,column=4)
Button(text='SUBMIT',command=getvals,font="ar 10 bold").grid(row=19,column=5)
window.mainloop()