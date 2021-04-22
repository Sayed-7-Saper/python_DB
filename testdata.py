import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox
fnt='tahoma 25 bold'
fg='white'
bg='navy'
pad=5

##########################################
def opentop(name):
    frm=None
    if name == 'emp': frm = employee()
    if name =='dept': frm = department()
    if name =='item': frm = item()
    return frm
   # frm.grab_set()



######################################################
def mainform():
    frm_main = Tk()
    frm_main.title('Company Program ::')
    frm_main.geometry('700x550+400+150')
    Label(frm_main,text='Company Program  :: ',font=fnt).pack(pady=pad)
    Label(frm_main,text='_____________________________________').pack(pady=pad)
    Button(frm_main,text='Employee',font=fnt,command=lambda:opentop('emp')).pack(pady=pad)
    Button(frm_main,text='Department',font=fnt,command=lambda:opentop('dept')).pack(pady=pad)
    Button(frm_main,text='Item',font=fnt,command=lambda:opentop('item')).pack(pady=pad)
    Button(frm_main,text='Exit',font=fnt,command=frm_main.destroy).pack(pady=pad)
    Label(frm_main,text='_____________________________________').pack(pady=pad)
    
    return frm_main
##############################################################



def num_only(text):
    if str.isdigit(text):
        return True
    elif text is '':
        return True
    else:
        return False

#reg_fun = f1.register(num_only)
reg_fun = mainform().register(num_only) 
#reg_fun = frm_main.register(num_only)             


############################################################################
def employee():
    frm_emp = Toplevel()
    frm_emp.title('Employee Form ::')
    frm_emp.geometry('700x550+400+150')
    Label(frm_emp,text='Employee Data Form :: ',font=fnt).pack(pady=pad)
    f1=Frame(frm_emp)
    f1.pack(pady=pad)
    f2=Frame(frm_emp)
    f2.pack(pady=pad)
    vnum=StringVar()
    vname=StringVar()
    vcity=StringVar()
    vphone=StringVar()
    vemail=StringVar()
    Label(f1,text='Number : ',font=fnt).grid(row=0,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vnum,validate='key',validatecommand=(reg_fun,'%P')).grid(row=0,column=1,pady=pad)
    Label(f1,text='Name : ',font=fnt).grid(row=1,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vname).grid(row=1,column=1,pady=pad)
    Label(f1,text='City : ',font=fnt).grid(row=2,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vcity).grid(row=2,column=1,pady=pad)
    Label(f1,text='Phone : ',font=fnt).grid(row=3,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vphone,validate='key',validatecommand=(reg_fun,'%P')).grid(row=3,column=1,pady=pad)
    Label(f1,text='Email : ',font=fnt).grid(row=4,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vemail).grid(row=4,column=1,pady=pad)
    def showdata():
        messagebox.showinfo('Print Data :  ',[vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()])
        
    Button(f2,text='Add',command=showdata,font=fnt).grid(row=0,column=0,pady=pad,padx=pad)
    Button(f2,text='Edit',command=showdata,font=fnt).grid(row=0,column=1,pady=pad,padx=pad)
    Button(f2,text='Delete',command=showdata,font=fnt).grid(row=0,column=2,pady=pad,padx=pad)
    Button(f2,text='Find',command=showdata,font=fnt).grid(row=0,column=3,pady=pad,padx=pad)
    Button(f2,text='Close',command=frm_emp.destroy,font=fnt).grid(row=1,column=0,columnspan=4,pady=pad,padx=pad)
    return frm_emp
###############################################################################
def department ():
    frm_dept = Toplevel()
    frm_dept.title('Department Form ::')
    frm_dept.geometry('700x550+400+150')
    Label(frm_dept,text='Department Data Form :: ',font=fnt).pack(pady=pad)
    f1=Frame(frm_dept)
    f1.pack(pady=pad)
    f2=Frame(frm_dept)
    f2.pack(pady=pad)
    vnum=StringVar()
    vname=StringVar()
    vloc=StringVar()
    Label(f1,text=' Department Number : ',font=fnt).grid(row=0,column=0,pady=pad)
    txt1=ttk.Entry(f1,font='None 20 bold',textvariable=vnum,validate='key',validatecommand=(reg_fun,'%P')).grid(row=0,column=1,pady=pad)
    Label(f1,text='Department Name : ',font=fnt).grid(row=1,column=0,pady=pad)
    txt1=ttk.Entry(f1,font='None 20 bold',textvariable=vname).grid(row=1,column=1,pady=pad)
    Label(f1,text=' Department Location : ',font=fnt).grid(row=2,column=0,pady=pad)
    txt1=ttk.Entry(f1,font='None 20 bold',textvariable=vloc).grid(row=2,column=1,pady=pad)
    def showdata():
        messagebox.showinfo('Print Data :  ',[vnum.get(),vname.get(),vloc.get()])
        
    Button(f2,text='Save',command=showdata,font=fnt).grid(row=0,column=0,pady=pad,padx=pad)
    Button(f2,text='Find',command=showdata,font=fnt).grid(row=0,column=1,pady=pad,padx=pad)
    Button(f2,text='Delete',command=showdata,font=fnt).grid(row=0,column=2,pady=pad,padx=pad)
    Button(f2,text='Close',command=frm_dept.destroy,font=fnt).grid(row=1,column=0,columnspan=3,pady=pad,padx=pad)
    return frm_dept
##############################################################
def item ():
    frm_item = Toplevel()
    frm_item.title('Item Form ::')
    frm_item.geometry('700x550+400+150')
    Label(frm_item,text='Item Data Form :: ',font=fnt).pack(pady=pad)
    f1=Frame(frm_item)
    f1.pack(pady=pad)
    f2=Frame(frm_item)
    f2.pack(pady=pad)
    vnum=StringVar()
    vname=StringVar()
    vprice=StringVar()
    Label(f1,text=' Item Number : ',font=fnt).grid(row=0,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vnum,validate='key',validatecommand=(reg_fun,'%P')).grid(row=0,column=1,pady=pad)
    Label(f1,text='Item Name : ',font=fnt).grid(row=1,column=0,pady=pad)
    txt1=ttk.Entry(f1,font=fnt,textvariable=vname).grid(row=1,column=1,pady=pad)
    Label(f1,text=' Item Price : ',font=fnt).grid(row=2,column=0,pady=pad)#####
    txt1=ttk.Entry(f1,font=fnt,textvariable=vprice).grid(row=2,column=1,pady=pad)
    def showdata():
        messagebox.showinfo('Print Data :  ',[vnum.get(),vname.get(),vprice.get()])
        
    Button(f2,text='Save',command=showdata,font=fnt).grid(row=0,column=0,pady=pad,padx=pad)
    Button(f2,text='Find',command=showdata,font=fnt).grid(row=0,column=1,pady=pad,padx=pad)
    Button(f2,text='Delete',command=showdata,font=fnt).grid(row=0,column=2,pady=pad,padx=pad)
    Button(f2,text='Close',command=frm_item.destroy,font=fnt).grid(row=1,column=0,columnspan=3,pady=pad,padx=pad)
    return frm_item
#################################################################################
    
    

    


    
    
    






