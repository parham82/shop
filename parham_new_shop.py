  ###### PARHAM KHOSRAVI ############

import tkinter
import sqlite3
import datetime
from tkinter import messagebox
#--------------------- connection
cnt=sqlite3.connect("myshop.db")
print("connection to database")
#--------------------- table username
# query='''create table info
# (id integer primary key,
#   user char(20) not null,
#   psw char(30) not null,
#   addr char(40)not null,
#   date char(45) not null,
#   buy char(30) not null)'''
# cnt.execute(query)
# cnt.close


#--------------------- inser into username
time=datetime.datetime.now()

# query='''insert into info(user,psw,addr,date,buy)
# values("admin","123456789","rasht",?,0)'''
# cnt.execute(query,(time,))
# cnt.commit()
# cnt.close()


#---------------------- table product
# query='''create table product
# (id integer primary key,
#   name char(20) not null,
#   price int not null,
#   qnt int not null,
#   comment text)'''
# cnt.execute(query)
# cnt.close()


#----------------------- inser into
# query='''insert into product(name,price,qnt)
# values("hat","123000","0")'''
# cnt.execute(query)
# cnt.commit()
# cnt.close()

#---------------------- table buy
# query='''create table buy
# (id integer primary key,
#   name char(20) not null,
#   time int not null,
#   qnt1 ynt not null)'''
# cnt.execute(query)
# cnt.close()
#----------------------- inser into
# query='''insert into buy(name,time,qnt1)
# values("hat",?,0)'''
# cnt.execute(query,(time,))
# cnt.commit()
# cnt.close()

#----------------------- login
def login():
    global user
    user=txt_user.get()
    psw=txt_psw.get()
    
    if len(user)==0 or len(psw)==0:
        lbl_msg.configure(text="pleas fill input",font="arial",fg="red")
        return
    query='''select user,psw from info where user=? and psw=?'''
    result=cnt.execute(query,(user,psw))
    rows=result.fetchall()
    
    if len(rows)==0:
        lbl_msg.configure(text="not found",fg="red",font="Corbel")
        return
    else:
        lbl_msg.configure(text="welcome to your account",fg="green",font="Corbel")
        txt_user.delete(0,"end")
        txt_psw.delete(0,"end")
        btn_login.configure(state="disable")
        btn_logout.configure(state="active")
        btn_shop.configure(state="active")
        if user=="admin":
            btn_admin.configure(state="active")

#-------------------------------------------------------
def logout():
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")    
    lbl_msg.configure(text="logout done!!",fg="green",font="Corbel")
#-------------------------------------------------------
def submit_finali():
    global user
    user=txt_user1.get()
    psw=txt_psw1.get()
    addr=txt_addr1.get()
    
    if len(user)==0 or len(psw)==0 or len(addr)==0:
        lbl_msg1.configure(text="pleas fill input",font="arial",fg="red")
        return
    if len(psw)<8:
        lbl_msg1.configure(text="password is too short!!",font="arial",fg="red")
        return
    query='''select user,psw from info where user=? and psw=?'''
    result=cnt.execute(query,(user,psw))
    rows=result.fetchall()
    if len(rows)!=0:
        lbl_msg1.configure(text="username already exist",font="arial",fg="red")
        return
    else:
        query='''insert into info(user,psw,addr,date,buy)
        values(?,?,?,?,?)'''
        cnt.execute(query,(user,psw,addr,time,0))
        cnt.commit()
        lbl_msg1.configure(text="submit done",font="Corbel",fg="green")
        txt_user1.delete(0,"end")
        txt_psw1.delete(0,"end")
        txt_addr1.delete(0,"end")
def submit():
    global txt_user1,txt_psw1,txt_addr1,lbl_msg1
    #----------------------- main
    win1=tkinter.Tk()
    win1.title("submit")
    win1.geometry("500x600")
    #----------------------- lable
    lbl_user1=tkinter.Label(win1,padx=10,bg="red",text="USERNAME")
    lbl_user1.pack()

    txt_user1=tkinter.Entry(win1,width=25)
    txt_user1.pack()

    lbl_psw1=tkinter.Label(win1,padx=10,bg="blue",text="PASSWORD")
    lbl_psw1.pack()

    txt_psw1=tkinter.Entry(win1,width=25)
    txt_psw1.pack()
    
    lbl_addr1=tkinter.Label(win1,padx=20,bg="green",text="ADDRES")
    lbl_addr1.pack()
    
    txt_addr1=tkinter.Entry(win1,width=25)
    txt_addr1.pack()

    lbl_msg1=tkinter.Label(win1,text="")
    lbl_msg1.pack()
    #---------------------- butten

    btn_submit1=tkinter.Button(win1,text="SUBMIT FINALI",bg="black",fg="white",command=submit_finali)
    btn_submit1.pack()

    win1.mainloop()
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
def shop():
    global txt_buy,lbl_msg_buy
    win2=tkinter.Toplevel(win)
    win2.title("SHOP")
    win2.geometry("500x500")
    
    lst_box=tkinter.Listbox(win2,width=40,height=12)
    lst_box.pack()
    
    query='''select * from product'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for items in rows:
        mystr=f"id: {items[0]}  name: {items[1]}  price: {items[2]}  qnt: {items[3]} "
        lst_box.insert(0, mystr)
    
    lbl_buy=tkinter.Label(win2,text="ENTER NAME PRODUCT")
    lbl_buy.pack()
    
    txt_buy=tkinter.Entry(win2,width=25)
    txt_buy.pack()
    
    btn_buy=tkinter.Button(win2,text="BUY",fg="brown",command=buy)
    btn_buy.pack()
    
    
    lbl_msg_buy=tkinter.Label(win2,text="")
    lbl_msg_buy.pack()
    
    win2.mainloop()
#############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def buy():
    global user
    markt=txt_buy.get()
    
    if len(markt)==0:
        lbl_msg_buy.configure(text="plese fill input",font="arial",fg="red")
        return

    
    
    query='''select * from product where name=?'''
    result=cnt.execute(query,(markt,))
    rows=result.fetchall()
    
    if len(rows)==0:
        lbl_msg_buy.configure(text="product not exist",fg="red")
        return
    
    query='''select qnt from product where name=?'''
    result=cnt.execute(query,(markt,))
    rows=result.fetchall()
    
    for items in rows:
        if 0 in items:
            lbl_msg_buy.configure(text="finish product",fg='red')
            return
    else:
        query='''update product set qnt=qnt-1 where name=?'''
        cnt.execute(query,(markt,))
        cnt.commit()
        
        # query='''update info set buy=buy+1 where user=?'''
        # cnt.execute(query,(user,))
        # cnt.commit()

        query='''update info set buy=buy+1'''
        cnt.execute(query)
        cnt.commit()
        
        # query='''update buy set qnt1=qnt1+1 where time=? and name=?'''
        # cnt.execute(query,(time,markt))
        # cnt.commit()
        
        query='''insert into buy(name,time,qnt1)
        values(?,?,0)'''
        cnt.execute(query,(markt,time))
        cnt.commit()
        
        query='''update buy set qnt1=qnt1+1 where name=?'''
        cnt.execute(query,(markt,))
        cnt.commit()
                
        lbl_msg_buy.configure(text="buy don",fg='green')
        txt_buy.delete(0,"end")
    

        
        

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
############################################################################
#///////////////////////////////////////////////////////////////////////////    
def lst_user():
    win_lstu=tkinter.Toplevel(win_admin)
    win_lstu.title("username list")
    win_lstu.geometry("450x450")
    
    lst1_box=tkinter.Listbox(win_lstu,width=40,height=15)
    lst1_box.pack()

    
    query='''select user,date from info'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for items in rows:
        # time=items[1]
        lst1_box.insert(0,items)
    win_lstu.mainloop()
#############################################################################    
def lst_product():
    win_lstp=tkinter.Toplevel(win_admin)
    win_lstp.title("product list")
    win_lstp.geometry("450x450")
    
    lst2_box=tkinter.Listbox(win_lstp,width=40,height=15)
    lst2_box.pack()
    
    query='''select name,qnt from product'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for items in rows:
        if len(items)!=0:
            lst2_box.insert(0,items)
    win_lstp.mainloop()
#############################################################################        
def lst_fproduct():
    win_lstf=tkinter.Toplevel(win_admin)
    win_lstf.title("product list")
    win_lstf.geometry("450x450")
    
    lst3_box=tkinter.Listbox(win_lstf,width=40,height=15)
    lst3_box.pack()
    
    query='''select * from product'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for items in rows:
        # name=items[1]
        qnt=items[3]
        if int(qnt)==0:
            lst3_box.insert(0,items)
    win_lstf.mainloop()
#############################################################################   
def lst_eproduct():
    win_lste=tkinter.Toplevel(win_admin)
    win_lste.title("product list")
    win_lste.geometry("450x450")
    
    lst4_box=tkinter.Listbox(win_lste,width=40,height=15)
    lst4_box.pack()
    
    query='''select * from product'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for items in rows:
        # name=items[1]
        qnt=items[3]
        if int(qnt)!=0:
            lst4_box.insert(0,items)
    win_lste.mainloop()

#############################################################################
def lst_fACproduct():
    winf_lste=tkinter.Toplevel(win_admin)
    winf_lste.title("product list")
    winf_lste.geometry("450x450")
    
    lst5_box=tkinter.Listbox(winf_lste,width=40,height=15)
    lst5_box.pack()
    
    query='''select name from buy order by qnt1'''
    result=cnt.execute(query)
    rows=result.fetchall()
    bp=rows[1]
    lst5_box.insert(0,bp)
    winf_lste.mainloop()       
    
#############################################################################
def lst_worproduct():
    winw_lste=tkinter.Toplevel(win_admin)
    winw_lste.title("product list")
    winw_lste.geometry("450x450")
    
    lst6_box=tkinter.Listbox(winw_lste,width=40,height=15)
    lst6_box.pack()
    
    query='''select name from buy order by qnt1 desc'''
    result=cnt.execute(query)
    rows=result.fetchall()
    wp=rows[1]    
    lst6_box.insert(0,wp)
    winw_lste.mainloop()
    
#############################################################################
def lst_customer():
    win_cu=tkinter.Toplevel(win_admin)
    win_cu.title("product list")
    win_cu.geometry("450x450")
    
    lst7_box=tkinter.Listbox(win_cu,width=40,height=15)
    lst7_box.pack()
    
    query='''select user from info order by buy'''
    result=cnt.execute(query)
    rows=result.fetchall()
    user=rows[1]
    lst7_box.insert(0,user)
    
    win_cu.mainloop()
    
#############################################################################
def connect():
    messagebox.askquestion("connect with me","NAME: PARHAM KHOSRAVI \n JOB: computer engineering/programmer ID:@parham_khosravi")
    
#############################################################################
def admin():
    global win_admin
    win_admin=tkinter.Toplevel(win)
    win_admin.title("admin plan")
    win_admin.geometry("150x340")
    
    lbl_admin=tkinter.Label(win_admin,bg="orange",text="REPORT")
    lbl_admin.pack()
    
    #---------------- scroll
    
    # lstt_box=tkinter.Listbox(win_admin,width=20,height=6, selectmode= "multiple")
    # lstt_box.pack()
    
    # sc=tkinter.Scrollbar(win_admin,command=lstt_box.yview, orient="vertical")
    # sc.pack()
    
    # btn_lstu=tkinter.Button(win_admin,text="USER SUBMIT",command=lst_user)
    # btn_lstu.pack()

    # lstt_box.configure(yscrollcommand=sc.set)
    
    btn_product=tkinter.Button(win_admin,text=" ALL PRODUCT",command=lst_product)
    btn_product.pack()
    
    btn_exist_product=tkinter.Button(win_admin,text=" EXIST PRODUCT",command=lst_eproduct)
    btn_exist_product.pack()
    
    btn_finish_product=tkinter.Button(win_admin,text=" FINISHE PRODUCT",command=lst_fproduct)
    btn_finish_product.pack()
    
    btn_favourite_product=tkinter.Button(win_admin,text="FAVOURITE PRODUCT",command=lst_fACproduct)
    btn_favourite_product.pack()
    
    btn_worst_product=tkinter.Button(win_admin,text="WORST PRODUCT",command=lst_worproduct)
    btn_worst_product.pack()
    
    btn_customer=tkinter.Button(win_admin,text="BEST CUSTOMER",command=lst_customer)
    btn_customer.pack()
    

    
    win_admin.mainloop()
#----------------------- main
win=tkinter.Tk()
win.title("login project")
win.geometry("600x700")
#----------------------- lable
lbl_user=tkinter.Label(win,padx=10,bg="red",text="USERNAME")
# lbl_user.grid(row=0)
lbl_user.pack()

txt_user=tkinter.Entry(win,width=25)
# txt_user.grid(row=0,column=1)
txt_user.pack()

lbl_psw=tkinter.Label(win,padx=10,bg="blue",text="PASSWORD")
lbl_psw.pack()

txt_psw=tkinter.Entry(win,width=25)
txt_psw.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()
#---------------------- butten
btn_login=tkinter.Button(win,text="LOGIN",bg="black",fg="white",command=login)
btn_login.pack()

btn_logout=tkinter.Button(win,text="LOGOUT",bg="white",fg="black",state="disabled",command=logout)
btn_logout.pack()
    
btn_submit=tkinter.Button(win,text="SUBMIT",bg="black",fg="white",command=submit)
btn_submit.pack()

btn_shop=tkinter.Button(win,text="SHOP",bg="white",fg="black",state="disabled",command=shop)
btn_shop.pack()

btn_admin=tkinter.Button(win,text="ADMIN PLAN",bg="black",fg="white",state="disabled",command=admin)
btn_admin.pack()


lbl_about=tkinter.Label(win,text="connect us: ",fg="blue")
lbl_about.pack()
    
btn_connect=tkinter.Button(win,text="CONNECT US",command=connect)
btn_connect.pack()


win.mainloop()
































































































