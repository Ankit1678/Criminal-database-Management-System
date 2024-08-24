from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox



class Criminal:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variables
    
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_Criminal_name=StringVar()
        self.var_nick_name=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_fathername=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()




        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM  SOFTWARE',font=('times new roman',35,'bold'),bg='black',fg='white')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #logo
        img_logo=Image.open('images/img logo.jpg')
        img_logo=img_logo.resize((60,60),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=60,y=0,width=60,height=70)

        # img_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1=Image.open('images/banners.jpg')
        img1=img1.resize((500,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=500,height=160)

        #2nd img
        img2=Image.open('images/gun.jpg')
        img2=img2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=500,y=0,width=520,height=160)

        #3rd img
        img3=Image.open('images/crime.jpg')
        img3=img3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        #main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal information',font=('times new roman',15,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1450,height=270)
        
        #labels enrty


        #case id
        caseid=Label(upper_frame,text='Case ID:',font=('times new roman',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #no.

        lbl_criminal_no=Label(upper_frame,text='Criminal no:',font=('times new roman',11,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        txt_crinimal=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_crinimal.grid(row=0,column=3,padx=2,pady=7)

        #name

        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('times new roman',11,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_Criminal_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7)

        #nickname

        lbl_NickName=Label(upper_frame,text='NickName:',font=('times new roman',11,'bold'),bg='white')
        lbl_NickName.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_NickName=ttk.Entry(upper_frame,textvariable=self.var_nick_name,width=22,font=('arial',11,'bold'))
        txt_NickName.grid(row=1,column=3,padx=2,pady=7)

        #arrest date

        lbl_ArrestDate=Label(upper_frame,text='Arrest Date:',font=('times new roman',11,'bold'),bg='white')
        lbl_ArrestDate.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_ArrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        txt_ArrestDate.grid(row=2,column=1,padx=2,pady=7)

        #date

        lbl_crimedate=Label(upper_frame,text='Crime date:',font=('times new roman',11,'bold'),bg='white')
        lbl_crimedate.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_crimedate=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        txt_crimedate.grid(row=2,column=3,padx=2,pady=7)

        #Address

        lbl_Address=Label(upper_frame,text='Address:',font=('times new roman',11,'bold'),bg='white')
        lbl_Address.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_Address.grid(row=3,column=1,padx=2,pady=7)

        #Occupation

        lbl_occupation=Label(upper_frame,text='Occupation:',font=('times new roman',11,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        #age

        lbl_age=Label(upper_frame,text='Criminal Age:' ,font=('times new roman',11,'bold'),bg='white')
        lbl_age.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        #Birth mark

        lbl_birth=Label(upper_frame,text='Birth mark:',font=('times new roman',11,'bold'),bg='white')
        lbl_birth.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        txt_birth=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('arial',11,'bold'))
        txt_birth.grid(row=4,column=3,padx=2,pady=7)

        #Crime Type

        lbl_type=Label(upper_frame,text='Crime Type:',font=('times new roman',11,'bold'),bg='white')
        lbl_type.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_type=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        txt_type.grid(row=0,column=5,padx=2,pady=7)

        #father's name

        lbl_fathersname=Label(upper_frame,text='Fathername:',font=('times new roman',11,'bold'),bg='white')
        lbl_fathersname.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        lbl_fathersname=ttk.Entry(upper_frame,textvariable=self.var_fathername,width=22,font=('arial',11,'bold'))
        lbl_fathersname.grid(row=1,column=5,padx=2,pady=7)
        

        #gender

        lbl_gender=Label(upper_frame,text='Gender:',font=('times new roman', 11,'bold'),bg='white')
        lbl_gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)

       #Most Wanted

        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('times new roman',11,'bold'),bg='white')
        lbl_wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)

        txt_wanted=ttk.Entry(upper_frame,textvariable=self.var_wanted,width=22,font=('arial',11,'bold'))
        txt_wanted.grid(row=3,column=5,padx=2,pady=7)


       #Rdio Button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=680,y=80,width=150,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",10,"bold"),bg='white')
        male.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='female',value='female',font=("arial",10,"bold"),bg='white')
        female.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        # add button

        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #update button

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        # delete button

        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #clear button

        btn_clear=Button(button_frame,command=self.clear_data,text='clear',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

















        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal information Table',font=('times new roman',15,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1450,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal information',font=('times new roman',15,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1440,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()

        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=0,sticky=W,padx=5)

        self.var_search=StringVar()

        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Clear',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",20,"bold"),text="NATIONAL CRIME AGENCY",fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=10,pady=0)


        #Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1440,height=170)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='caseId')
        self.criminal_table.heading('2',text='crimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='Date of crime')
        self.criminal_table.heading('8',text='Address')
        self.criminal_table.heading('7',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime type')
        self.criminal_table.heading('12',text='father name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')
        
        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=90)
        self.criminal_table.column("2",width=90)
        self.criminal_table.column("3",width=90)
        self.criminal_table.column("4",width=90)
        self.criminal_table.column("5",width=90)
        self.criminal_table.column("6",width=90)
        self.criminal_table.column("7",width=90)
        self.criminal_table.column("8",width=90)
        self.criminal_table.column("9",width=90)
        self.criminal_table.column("10",width=90)
        self.criminal_table.column("11",width=90)
        self.criminal_table.column("12",width=90)
        self.criminal_table.column("13",width=90)
        self.criminal_table.column("14",width=90)



        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    #add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields Are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Ankit@1234',database='criminals')
                my_cursor=conn.cursor()
                my_cursor.execute('insert  into criminal_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',( 
                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_Criminal_name.get(),
                                                                                                            self.var_nick_name.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_birthMark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_fathername.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()

                                                                                                           ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')



    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Ankit@1234',database='criminals')
        my_cursor=conn.cursor()
        my_cursor.execute('select*from criminal_data')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_Criminal_name.set(data[2])
        self.var_nick_name.set(data[3])
        self.var_arrest_date.set(data[5])
        self.var_date_of_crime.set(data[6])
        self.var_address.set(data[7])
        self.var_age.set(data[8])
        self.var_occupation.set(data[9])
        self.var_birthMark.set(data[10])
        self.var_crime_type.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])


    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Ankit@1234',database='criminals')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal_data set Criminal_no=%s,Criminal_Name=%s,Nick_name=%s,Arrest_date=%s,date_of_crime=%s,Address=%s,Age=%s,occupation=%s,Birthmark=%s,CrimeType=%s,Fathername=%s,Gender=%s,Wanted=%s where Case_id=%s',(
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    self.var_criminal_no.get(),
                                                                                                                                                                                                                                    self.var_Criminal_name.get(),
                                                                                                                                                                                                                                    self.var_nick_name.get(),
                                                                                                                                                                                                                                    self.var_arrest_date.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_age.get(),
                                                                                                                                                                                                                                    self.var_occupation.get(),
                                                                                                                                                                                                                                    self.var_date_of_crime.get(),
                                                                                                                                                                                                                                    self.var_birthMark.get(),
                                                                                                                                                                                                                                    self.var_crime_type.get(),
                                                                                                                                                                                                                                    self.var_fathername.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_wanted.get(),
                                                                                                                                                                                                                                    self.var_case_id.get()

                                                                                                                                                                                                                                     ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record succesfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # delete

    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure Delete this criminal record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Ankit@1234',database='criminals')
                    my_cursor=conn.cursor()  
                    sql='delete from criminal_data where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','Criminal record succesfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    # clear

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_Criminal_name.set("")
        self.var_nick_name.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search

    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','kuch to garbad h')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Ankit@1234',database='criminals')
                my_cursor=conn.cursor()
                my_cursor.execute('select*from criminal_data where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')















if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()