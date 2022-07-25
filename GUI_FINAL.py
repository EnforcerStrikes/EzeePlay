from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import datetime   
format_str = '%Y-%m-%d' 

root = Tk()
booking_frame = Frame(root)
resident_frame = Frame(root)
sports_frame = Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.title("Sports Club Booking")

def show_frame(frame):
    frame.tkraise()
    
    
for frame in (booking_frame, resident_frame, sports_frame):
    frame.grid(row=0, column=0, sticky="nsew")




#-------------------- BOOKING FRAME --------------------------

booking_heading = Label(booking_frame, text="BOOKING", font=('bold', 40), pady=20)
booking_heading.grid(row=0, column=0, columnspan=7)

sep_b1 = ttk.Separator(booking_frame, orient="horizontal")
sep_b1.grid(column=0, row=1, columnspan=7, sticky="ew")
sep_b2 = ttk.Separator(booking_frame, orient="horizontal")
sep_b2.grid(column=0, row=9, columnspan=2, sticky="ew")
sep_b3 = ttk.Separator(booking_frame, orient="horizontal")
sep_b3.grid(column=0, row=14, columnspan=2, sticky="ew")
sep_b4 = ttk.Separator(booking_frame, orient="horizontal")
sep_b4.grid(column=0, row=18, columnspan=7, sticky="ew")
sep_b5 = ttk.Separator(booking_frame, orient="vertical")
sep_b5.grid(column=2, row=1, rowspan=17, sticky="ns")
sep_b6 = ttk.Separator(booking_frame, orient="vertical")
sep_b6.grid(column=8, row=1, rowspan=17, sticky="ns")

booking_status= Label(booking_frame)
booking_status.grid(row=7, column=1)
delete_status= Label(booking_frame)
delete_status.grid(row=12, column=1)

# Submit Function
def submit():
    flat_e= flat.get()
    sport_e= sport.get()
    date_e= date.get()        
    time_slot_e= time_slot.get()
    
    if flat_e:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()

            date_str = date_e 
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
            values = (flat_e, sport_e, datetime_obj, time_slot_e) 
            c.execute(query, values)

            db.commit()
            db.close()

            # Clear Text boxes
            flat.delete(0, END)
            sport.delete(0, END)
            date.delete(0, END)
            time_slot.delete(0, END)

            bstat1 = "BOOKED SUCCESSFULLY !!"
            booking_status.config(text= bstat1)   

        except:
            bstat2 = "ERROR, PLEASE TRY AGAIN !!"
            booking_status.config(text= bstat2) 
          
    
# Display function
def display_default():

    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM BOOKING")
    rows = c.fetchall()

    tv.delete(*tv.get_children())

    for i in rows:
        tv.insert('', 'end', values=i)

    db.commit()
    db.close()


# Sort By Flat
def sort_flat():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM BOOKING ORDER BY FLAT")
    rows = c.fetchall()

    tv.delete(*tv.get_children())

    for i in rows:
        tv.insert('', 'end', values=i)

    db.commit()
    db.close()


# Sort By Sport
def sort_sport():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM BOOKING ORDER BY SPORT")
    rows = c.fetchall()

    tv.delete(*tv.get_children())

    for i in rows:
        tv.insert('', 'end', values=i)

    db.commit()
    db.close()


# Sort By Date
def sort_date():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM BOOKING ORDER BY DATE")
    rows = c.fetchall()

    tv.delete(*tv.get_children())

    for i in rows:
        tv.insert('', 'end', values=i)

    db.commit()
    db.close()


# Delete Function
def delete():

    delete1_e = delete1.get()

    if delete1_e:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()

            c.execute("DELETE FROM BOOKING WHERE ID = " + delete1_e)
            rows = c.rowcount

            db.commit()
            db.close()
            delete1.delete(0, END)

            dstat1 = str(rows) + " ENTRY DELETED"
            delete_status.config(text= dstat1)

        except:
            dstat2 = "ERROR, PLEASE TRY AGAIN !!"
            delete_status.config(text= dstat2)
        

# Search Function
def search_flat():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()
    search_val= search.get()

    if search_val:
        c.execute("SELECT * FROM BOOKING WHERE FLAT REGEXP %s", (search_val,))
        rows = c.fetchall()

        tv.delete(*tv.get_children())

        for i in rows:
            tv.insert('', 'end', values=i)



    db.commit()
    db.close()
    search.delete(0, END)


# Text boxes 
flat = Entry(booking_frame, width=30)
flat.grid(row=3, column=1, padx= 20, pady=5)
sport = Entry(booking_frame, width=30)
sport.grid(row=4, column=1, pady=5)
date = Entry(booking_frame, width=30)
date.grid(row=5, column=1, pady=5)
time_slot = Entry(booking_frame, width=30)
time_slot.grid(row=6, column=1, pady=5)
delete1 = Entry(booking_frame, width=30)
delete1.grid(row=11, column=1)
search = Entry(booking_frame, width=30)
search.grid(row=16, column=1)

# Labels
heading_label_entry = Label(booking_frame, text="ENTER DETAILS", font=('bold', 12), pady=20)
heading_label_entry.grid(row=2, column=0, columnspan=2)
heading_label_display = Label(booking_frame, text="DISPLAY", font=('bold', 12), pady=20)
heading_label_display.grid(row=2, column=3, columnspan=4)
heading_label_delete = Label(booking_frame, text="CANCEL BOOKING", font=('bold', 12), pady=20)
heading_label_delete.grid(row=10, column=0, columnspan=2)
heading_label_search = Label(booking_frame, text="SEARCH", font=('bold', 12), pady=20)
heading_label_search.grid(row=15, column=0, columnspan=2)
flat_label = Label(booking_frame, text="FLAT")
flat_label.grid(row=3, column=0, padx=20)
sport_label = Label(booking_frame, text="SPORT")
sport_label.grid(row=4, column=0)
date_label = Label(booking_frame, text="DATE")
date_label.grid(row=5, column=0)
time_slot_label = Label(booking_frame, text="TIME SLOT")
time_slot_label.grid(row=6, column=0)
delete1_label = Label(booking_frame, text="ID")
delete1_label.grid(row=11, column=0)
booking_status_label= Label(booking_frame, text="STATUS")
booking_status_label.grid(row=7, column=0, pady=5)
delete_status_label= Label(booking_frame, text="STATUS")
delete_status_label.grid(row=12, column=0, pady=5)
search_label = Label(booking_frame, text="FLAT")
search_label.grid(row=16, column=0, padx=20)

# Button
submit_btn = Button(booking_frame, text="ADD ENTRY", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
delete_btn = Button(booking_frame, text="DELETE", command=delete) 
delete_btn.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
search_btn = Button(booking_frame, text="SEARCH", command=search_flat)
search_btn.grid(row=17, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
refresh_btn = Button(booking_frame, text="REFRESH", command=display_default) 
refresh_btn.grid(row=17, column=3, padx=10, pady=10, ipadx=100)
sort_flat_btn = Button(booking_frame, text="SORT BY FLAT", command=sort_flat) 
sort_flat_btn.grid(row=17, column=4, padx=10, pady=10, ipadx=100)
sort_sport_btn = Button(booking_frame, text="SORT BY SPORT", command=sort_sport) 
sort_sport_btn.grid(row=17, column=5, padx=10, pady=10, ipadx=100)
sort_date_btn = Button(booking_frame, text="SORT BY DATE", command=sort_date) 
sort_date_btn.grid(row=17, column=6, padx=10, pady=10, ipadx=100)

# Display Treeview
tv = ttk.Treeview(booking_frame, columns=(1,2,3,4,5), show="headings", height="20")
tv.grid(row=3, column=3, rowspan=14, columnspan=4, padx=20)
tv.heading(1, text="ID")
tv.heading(2, text="FLAT")
tv.heading(3, text="SPORT")
tv.heading(4, text="DATE")
tv.heading(5, text="TIME SLOT")

show_frame(booking_frame)

resident_switch_btn = Button(booking_frame, text="SHOW RESIDENTS", command=lambda:show_frame(resident_frame))
resident_switch_btn.grid(row=19, column=0, padx=10, pady=10, ipadx=100, columnspan=2)
sports_switch_btn = Button(booking_frame, text="SHOW SPORTS", command=lambda:show_frame(sports_frame))
sports_switch_btn.grid(row=20, column=0, padx=10, pady=10, ipadx=100, columnspan=2)



#-------------------- Resident FRAME --------------------------

resident_heading = Label(resident_frame, text="RESIDENTS", font=('bold', 40), pady=20)
resident_heading.grid(row=0, column=0, columnspan=7)

sep_r1 = ttk.Separator(resident_frame, orient="horizontal")
sep_r1.grid(column=0, row=1, columnspan=9, sticky="ew")
sep_r2 = ttk.Separator(resident_frame, orient="horizontal")
sep_r2.grid(column=0, row=9, columnspan=2, sticky="ew")
sep_r3 = ttk.Separator(resident_frame, orient="horizontal")
sep_r3.grid(column=0, row=14, columnspan=2, sticky="ew")
sep_r4 = ttk.Separator(resident_frame, orient="horizontal")
sep_r4.grid(column=0, row=18, columnspan=9, sticky="ew")
sep_r5 = ttk.Separator(resident_frame, orient="vertical")
sep_r5.grid(column=2, row=1, rowspan=17, sticky="ns")  
sep_r6 = ttk.Separator(resident_frame, orient="vertical")
sep_r6.grid(column=8, row=1, rowspan=17, sticky="ns")

booking_status2 = Label(resident_frame)
booking_status2.grid(row=7, column=1)
delete_status2 = Label(resident_frame)
delete_status2.grid(row=12, column=1)


# Add resident submit 
def submit2():
    flat2_e= flat2.get()
    name2_e= name2.get()
    number2_e= number2.get()        
    building_name2_e= building_name2.get()

    if flat2_e:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()

            
            query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
            values = (flat2_e, name2_e, number2_e, building_name2_e) 
            c.execute(query, values)

            db.commit()
            db.close()

            # Clear Text boxes
            flat2.delete(0, END)
            name2.delete(0, END)
            number2.delete(0, END)
            building_name2.delete(0, END)

            rstat1 = "ADDED SUCCESSFULLY !!"
            booking_status2.config(text= rstat1)        

        except:
            rstat2 = "ERROR, PLEASE TRY AGAIN !!"
            booking_status2.config(text= rstat2) 


# Display function for resident
def display_default2():

    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM RESIDENTS")
    rows = c.fetchall()

    tv2.delete(*tv2.get_children())

    for i in rows:
        tv2.insert('', 'end', values=i)

    db.commit()
    db.close()


# Delete Function
def delete2():
    values2 = delete2_resident.get()

    if values2:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()

            query2 = "DELETE FROM RESIDENTS WHERE FLAT = %s"
            c.execute(query2, (values2,))
            rows = c.rowcount

            #c.execute("DELETE FROM RESIDENTS WHERE FLAT = " + delete2_resident.get())

            db.commit()
            db.close()
            delete2_resident.delete(0, END)

            dstat1 = str(rows) + " ENTRY DELETED"
            delete_status2.config(text= dstat1)

        except:
            dstat2 = "ERROR, PLEASE TRY AGAIN !!"
            delete_status2.config(text= dstat2)


# Search Function
def search_name2():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()
    search_val2 = search2.get()
    check_flat = len(search_val2)

    if search_val2:

        if check_flat == 5:
            c.execute("SELECT * FROM RESIDENTS WHERE FLAT REGEXP %s", (search_val2,))
            rows = c.fetchall()

            tv2.delete(*tv2.get_children())

            for i in rows:
                tv2.insert('', 'end', values=i)
            

        else:
            c.execute("SELECT * FROM RESIDENTS WHERE NAME REGEXP %s", (search_val2,))
            rows = c.fetchall()
            
            tv2.delete(*tv2.get_children())

            for i in rows:
                tv2.insert('', 'end', values=i)



    db.commit()
    db.close()
    search2.delete(0, END)


# Sort by name
def sort_name2():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM RESIDENTS ORDER BY NAME")
    rows = c.fetchall()

    tv2.delete(*tv2.get_children())

    for i in rows:
        tv2.insert('', 'end', values=i)

    db.commit()
    db.close()


# Text Boxes
flat2 = Entry(resident_frame, width=30)
flat2.grid(row=3, column=1, padx= 20, pady=5)
name2 = Entry(resident_frame, width=30)
name2.grid(row=4, column=1, padx= 20, pady=5)
number2 = Entry(resident_frame, width=30)
number2.grid(row=5, column=1, padx= 20, pady=5)
building_name2 = Entry(resident_frame, width=30)
building_name2.grid(row=6, column=1, padx= 20, pady=5)
delete2_resident = Entry(resident_frame, width=30)
delete2_resident.grid(row=11, column=1)
search2 = Entry(resident_frame, width=30)
search2.grid(row=16, column=1)

# Labels
add_resident_heading = Label(resident_frame, text="ADD RESIDENT", font=('bold', 12), pady=20)
add_resident_heading.grid(row=2, column=0, columnspan=2)
heading_label_display2 = Label(resident_frame, text="DISPLAY", font=('bold', 12), pady=20)
heading_label_display2.grid(row=2, column=3, columnspan=6)
heading_label_delete2 = Label(resident_frame, text="REMOVE RESIDENT", font=('bold', 12), pady=20)
heading_label_delete2.grid(row=10, column=0, columnspan=2)
heading_label_search2 = Label(resident_frame, text="SEARCH", font=('bold', 12), pady=20)
heading_label_search2.grid(row=15, column=0, columnspan=2)
flat2_label = Label(resident_frame, text="FLAT")
flat2_label.grid(row=3, column=0, padx=20)
name2_label = Label(resident_frame, text="NAME")
name2_label.grid(row=4, column=0, padx=20)
number2_label = Label(resident_frame, text="NUMBER")
number2_label.grid(row=5, column=0, padx=20)
building_name2_label = Label(resident_frame, text="BUILDING")
building_name2_label.grid(row=6, column=0, padx=20)
resident_status_label= Label(resident_frame, text="STATUS")
resident_status_label.grid(row=7, column=0, pady=5)
delete2_label = Label(resident_frame, text="FLAT")
delete2_label.grid(row=11, column=0)
delete2_status_label= Label(resident_frame, text="STATUS")
delete2_status_label.grid(row=12, column=0, pady=5)
search2_label = Label(resident_frame, text="NAME / FLAT")
search2_label.grid(row=16, column=0, padx=20)

# Buttons
submit2_btn = Button(resident_frame, text="ADD RESIDENT", command=submit2)
submit2_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
delete2_btn = Button(resident_frame, text="REMOVE", command=delete2) 
delete2_btn.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
search2_btn = Button(resident_frame, text="SEARCH", command=search_name2)
search2_btn.grid(row=17, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
refresh2_btn = Button(resident_frame, text="REFRESH", command=display_default2) 
refresh2_btn.grid(row=17, column=3, padx=10, pady=10, ipadx=100)
sort_name2_btn = Button(resident_frame, text="SORT BY NAME", command=sort_name2) 
sort_name2_btn.grid(row=17, column=4, padx=10, pady=10, ipadx=100)

# Display Treeview
tv2 = ttk.Treeview(resident_frame, columns=(1,2,3,4), show="headings", height="20")
tv2.grid(row=3, column=3, rowspan=14, columnspan=2, padx=100)
tv2.heading(1, text="FLAT")
tv2.heading(2, text="NAME")
tv2.heading(3, text="NUMBER")
tv2.heading(4, text="BUILDING")


booking_switch_btn = Button(resident_frame, text="SHOW BOOKINGS", command=lambda:show_frame(booking_frame))
booking_switch_btn.grid(row=19, column=0, padx=10, pady=10, ipadx=100, columnspan=2)




#-------------------- SPORTS LIST FRAME --------------------------

sports_heading = Label(sports_frame, text="SPORTS", font=('bold', 40), pady=20)
sports_heading.grid(row=0, column=0, columnspan=7)

sep_s1 = ttk.Separator(sports_frame, orient="horizontal")
sep_s1.grid(column=0, row=1, columnspan=7, sticky="ew")
sep_s2 = ttk.Separator(sports_frame, orient="horizontal")
sep_s2.grid(column=0, row=8, columnspan=2, sticky="ew")
sep_s3 = ttk.Separator(sports_frame, orient="horizontal")
sep_s3.grid(column=0, row=13, columnspan=2, sticky="ew")
sep_s4 = ttk.Separator(sports_frame, orient="horizontal")
sep_s4.grid(column=0, row=18, columnspan=7, sticky="ew")
sep_s5 = ttk.Separator(sports_frame, orient="vertical")
sep_s5.grid(column=2, row=1, rowspan=17, sticky="ns")
sep_s6 = ttk.Separator(sports_frame, orient="vertical")
sep_s6.grid(column=8, row=1, rowspan=17, sticky="ns")

sports_status= Label(sports_frame)
sports_status.grid(row=6, column=1)
delete3_status = Label (sports_frame)
delete3_status.grid(row=11, column=1)

# Submit Function
def submit():
    sport3_e= sport3.get()
    price_e= price.get()
    slots_e= slots.get()

    if sport3_e:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()
            
            query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
            values = (sport3_e, price_e, slots_e) 
            c.execute(query, values)

            db.commit()
            db.close()

            # Clear Text boxes
            sport3.delete(0, END)
            price.delete(0, END)
            slots.delete(0, END)

            sstat1 = "ADDED SUCCESSFULLY !!"
            sports_status.config(text= sstat1)   

        except:
            sstat2 = "ERROR, PLEASE TRY AGAIN !!"
            sports_status.config(text= sstat2) 


# Display function
def display_default3():

    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()

    c.execute("SELECT * FROM SPORTS_LIST")
    rows = c.fetchall()

    tv3.delete(*tv3.get_children())

    for i in rows:
        tv3.insert('', 'end', values=i)

    db.commit()
    db.close()


# Delete Functiona
def delete3_s():
    values3 = delete3.get()

    if values3:
        try:
            db = mysql.connect(
                host = "localhost",
                user = "root",  
                passwd = "", # Enter mySQL password
                db= "scb"
            )
            c = db.cursor()

            query3 = "DELETE FROM SPORTS_LIST WHERE SPORT = %s"
            c.execute(query3, (values3,))
            rows = c.rowcount

            db.commit()
            db.close()
            delete3.delete(0, END)

            sstat1 = str(rows) + " ENTRY DELETED"
            delete3_status.config(text= sstat1)

        except:
            sstat2 = "ERROR, PLEASE TRY AGAIN !!"
            delete3_status.config(text= sstat2)


# Search Function
def search_sport3():
    db = mysql.connect(
        host = "localhost",
        user = "root",  
        passwd = "", # Enter mySQL password
        db= "scb"
    )
    c = db.cursor()
    search_val3 = search3.get()

    if search_val3:
        c.execute("SELECT * FROM SPORTS_LIST WHERE SPORT REGEXP %s", (search_val3,))
        rows = c.fetchall()
        
        tv3.delete(*tv3.get_children())

        for i in rows:
            tv3.insert('', 'end', values=i)

    db.commit()
    db.close()
    search3.delete(0, END)


# Text boxes 
sport3 = Entry(sports_frame, width=30)
sport3.grid(row=3, column=1, padx= 20, pady=5)
price = Entry(sports_frame, width=30)
price.grid(row=4, column=1, padx= 20, pady=5)
slots = Entry(sports_frame, width=30)
slots.grid(row=5, column=1, padx= 20, pady=5)
delete3 = Entry(sports_frame, width=30)
delete3.grid(row=10, column=1, padx= 20, pady=5)
search3 = Entry(sports_frame, width=30)
search3.grid(row=15, column=1)

# Labels
sports_label_entry = Label(sports_frame, text="ADD SPORT", font=('bold', 12), pady=20)
sports_label_entry.grid(row=2, column=0, columnspan=2)
heading_label_display3 = Label(sports_frame, text="DISPLAY", font=('bold', 12), pady=20)
heading_label_display3.grid(row=2, column=3, columnspan=4)
sport3_label = Label(sports_frame, text="SPORT")
sport3_label.grid(row=3, column=0, padx=20)
price_label = Label(sports_frame, text="PRICE")
price_label.grid(row=4, column=0, padx=20)
slots_label = Label(sports_frame, text="SLOTS")
slots_label.grid(row=5, column=0, padx=20)
sport_status_label= Label(sports_frame, text="STATUS")
sport_status_label.grid(row=6, column=0, pady=5)
heading_label_delete3 = Label(sports_frame, text="REMOVE SPORT", font=('bold', 12), pady=20)
heading_label_delete3.grid(row=9, column=0, columnspan=2)
delete3_label = Label(sports_frame, text="SPORT")
delete3_label.grid(row=10, column=0, padx=20)
delete3_status_label = Label(sports_frame, text="STATUS")
delete3_status_label.grid(row=11, column=0, padx=20)
heading_label_search3 = Label(sports_frame, text="SEARCH", font=('bold', 12), pady=20)
heading_label_search3.grid(row=14, column=0, columnspan=2)
search3_label = Label(sports_frame, text="SPORT")
search3_label.grid(row=15, column=0, padx=20)

# Button
submit3_btn = Button(sports_frame, text="ADD SPORT", command=submit)
submit3_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
delete3_btn = Button(sports_frame, text="REMOVE SPORT", command=delete3_s)
delete3_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
search3_btn = Button(sports_frame, text="SEARCH", command=search_sport3)
search3_btn.grid(row=16, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
refresh3_btn = Button(sports_frame, text="REFRESH", command=display_default3) 
refresh3_btn.grid(row=17, column=3, padx=10, pady=10, ipadx=100)

# Display Treeview
tv3 = ttk.Treeview(sports_frame, columns=(1,2,3), show="headings", height="20")
tv3.grid(row=3, column=3, rowspan=14, padx=100)
tv3.heading(1, text="SPORT")
tv3.heading(2, text="PRICE")
tv3.heading(3, text="SLOTS")

booking_switch_btn2 = Button(sports_frame, text="SHOW BOOKINGS", command=lambda:show_frame(booking_frame))
booking_switch_btn2.grid(row=19, column=0, padx=10, pady=10, ipadx=100, columnspan=2)

root.mainloop()

