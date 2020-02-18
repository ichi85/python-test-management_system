from tkinter import*
from tkinter import ttk
import pymysql.cursors
from tkinter import messagebox

class Member:
    def __init__(self, root):
        self.root=root
        self.root.title("メンバー管理リスト")
        self.root.geometry("1350x700+0+0")


        title=Label(self.root, text="メンバー管理リスト", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg="Black", fg="blue")
        title.pack(side=TOP, fill=X)

        #---------- All Values --------------------#

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.DOB_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #---------- Manage Frame--------------------#

        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title=Label(Manage_Frame, text="メンバー情報", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll=Label(Manage_Frame, text="番号", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll=Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name=Label(Manage_Frame, text="名前", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email=Label(Manage_Frame, text="メール", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email=Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx="20", sticky="w")

        lbl_Gender=Label(Manage_Frame, text="性別", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['value']=("男性", "女性", "その他")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact=Label(Manage_Frame, text="コンタクト", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact=Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx="20", sticky="w")

        lbl_DOB=Label(Manage_Frame, text="生年月日", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB=Entry(Manage_Frame, textvariable=self.DOB_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address=Label(Manage_Frame, text="住所", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address=Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #---------- Button ---------------#

        btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn=Button(btn_Frame, text="登録", width=10, command=self.add_members)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)

        updatebtn=Button(btn_Frame, text="編集", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn=Button(btn_Frame, text="削除", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)

        clearbtn=Button(btn_Frame, text="クリア", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        #-------------- Detail Frame -------------------#

        Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=825, height=580)



        lbl_search=Label(Detail_Frame, text="検索オプション", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['value']=("roll_no", "name", "gender")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search=Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn=Button(Detail_Frame, text="検索", width=10, pady=5, command=self.search_data)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)

        showallbtn=Button(Detail_Frame, text="一覧表示", width=10, pady=5, command=self.fetch_data)
        showallbtn.grid(row=0, column=4, padx=10, pady=10)

        #------------ Table Frame -------------#

        Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=800, height=500)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Member_table=ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Member_table.xview)
        scroll_y.config(command=self.Member_table.yview)
        self.Member_table.heading("roll", text="番号")
        self.Member_table.heading("name", text="名前")
        self.Member_table.heading("email", text="メール")
        self.Member_table.heading("gender", text="性別")
        self.Member_table.heading("contact", text="コンタクト")
        self.Member_table.heading("dob", text="生年月日")
        self.Member_table.heading("Address", text="住所")
        self.Member_table["show"]="headings"
        self.Member_table.column("roll", width=50)
        self.Member_table.column("name", width=100)
        self.Member_table.column("email", width=100)
        self.Member_table.column("gender", width=100)
        self.Member_table.column("contact", width=100)
        self.Member_table.column("dob", width=100)
        self.Member_table.column("Address", width=150)
        self.Member_table.pack(fill=BOTH, expand=1)
        self.Member_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
    def add_members(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            con=pymysql.connect(host="localhost", user="root", password="arfo85", database="mem")
            cur=con.cursor()
            cur.execute("insert into members values(%s, %s, %s, %s, %s, %s, %s)", (self.Roll_No_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.DOB_var.get(),
                                                                                self.txt_Address.get('1.0', END),                                                                   
                                                                                ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="arfo85", database="mem")
        cur=con.cursor()
        cur.execute("select * from members")
        rows=cur.fetchall()
        if len(rows) != 0:
                self.Member_table.delete(*self.Member_table.get_children())
                for row in rows:
                        self.Member_table.insert('', END, values=row)
                con.commit()
        con.close()
    
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row=self.Member_table.focus()
        contents=self.Member_table.item(cursor_row)
        row=contents["values"]
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="arfo85", database="mem")
        cur=con.cursor()
        cur.execute("update members set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                               self.name_var.get(),
                                                                               self.email_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.DOB_var.get(),
                                                                               self.txt_Address.get('1.0', END),
                                                                               self.Roll_No_var.get()
                                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="arfo85", database="mem")
        cur=con.cursor()
        cur.execute("delete from members where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="arfo85", database="mem")
        cur=con.cursor()
        cur.execute("select * from members where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
                self.Member_table.delete(*self.Member_table.get_children())
                for row in rows:
                        self.Member_table.insert('', END, values=row)
                con.commit()
        con.close()

        
root=Tk()
obj=Member(root)
root.mainloop()