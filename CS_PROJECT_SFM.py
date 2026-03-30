import mysql.connector as c
mydb=c.connect(host="localhost",user="root",password="root")
cr=mydb.cursor()
cr.execute("create database if not exists hospital")
cr.execute("use hospital")

def registration():
    print("""=======================================================================
                    PLEASE REGISTER YOURSELF
=======================================================================\n""")
    u=input("ENTER YOUR PREFERRED USERNAME:")
    p=input("ENTER YOUR PREFERRED PASSWORD:")
    cr.execute("insert into user_data values(%s,%s)",(u,p))
    mydb.commit()
    print("""=======================================================================
                     REGISTERED SUCCESSFULLY
=======================================================================\n""")

def administration():
    ch=1
    while ch!=5:
        print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!! {( ADMINISTRATION )} !!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                         1. SHOW DETAILS
                         2. ADD NEW MEMBER
                         3. DELETE EXISTING ONE
                         4. UPDATE RECORDS
                         5. EXIT\n""")
        b=int(input("ENTER YOUR CHOICE:"))
        if b==1:
            while True:
                print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!! {( SHOW RECORDS )} !!!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                            1. DOCTOR DETAILS
                            2. NURSE DETAILS
                            3. OTHER WORKERS
                            4. EXIT\n""")
                c=int(input("ENTER YOUR CHOICE:"))
                if c==1:
                    cr.execute("select * from doctor_details")
                    rows=cr.fetchall()
                    if len(rows)==0:
                        print("\n                    NO RECORDS PRESENT!!\n")
                    else:
                        print("ID\tNAME\tSPECIALISATION\tAGE\tADDRESS\t\tCONTACT\t\tFEES\tSALARY")
                        for i in rows:
                            for n in range(len(i)):
                                print(i[n],end="\t")
                            print()
                elif c==2:
                    cr.execute("select * from nurse_details")
                    rows=cr.fetchall()
                    if len(rows)==0:
                        print("\n                    NO RECORDS PRESENT!!\n")
                    else:
                        print("ID\tNAME\tAGE\tADDRESS\t\tCONTACT\t\tSALARY")
                        for i in rows:
                            for n in range(len(i)):
                                print(i[n],end="\t")
                            print()
                elif c==3:
                    cr.execute("select * from workers_details")
                    rows=cr.fetchall()
                    if len(rows)==0:
                        print("\n                    NO RECORDS PRESENT!!\n")
                    else:
                        print("ID\tNAME\tAGE\tADDRESS\t\tCONTACT\t\tSALARY")
                        for i in rows:
                            for n in range(len(i)):
                                print(i[n],end="\t")
                            print()
                elif c==4:
                    break
                else:
                    print("\n                    INVALID CHOICE!!!\n")

        elif b==2:
            while True:
                print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!!!! {( ADD RECORDS )} !!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                            1. DOCTOR DETAILS
                            2. NURSE DETAILS
                            3. OTHER WORKERS
                            4. EXIT\n""")
                ch=int(input("ENTER YOUR CHOICE:"))
                if ch==1:
                    did=int(input("ENTER ID:"))
                    n=input("ENTER NAME:")
                    s=input("ENTER SPECIALISATION:")
                    a=int(input("ENTER AGE:"))
                    ad=input("ENTER ADDRESS:")
                    c=int(input("ENTER CONTACT NO:"))
                    f=int(input("ENTER FEES:"))
                    ms=int(input("ENTER MONTHLY SALARY:"))
                    t=(did,n,s,a,ad,c,f,ms)
                    cr.execute("INSERT INTO DOCTOR_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",t)
                    mydb.commit()
                    print("\n                    SUCCESSFULLY ADDED!!\n")
                elif ch==2:
                    nid=int(input("ENTER ID:"))
                    n=input("ENTER NAME:")
                    a=int(input("ENTER AGE:"))
                    ad=input("ENTER ADDRESS:")
                    c=int(input("ENTER CONTACT NO:"))
                    ms=int(input("ENTER MONTHLY SALARY:"))
                    t=(nid,n,a,ad,c,ms)
                    cr.execute("INSERT INTO NURSE_DETAILS VALUES(%s,%s,%s,%s,%s,%s)",t)
                    mydb.commit()
                    print("\n                    SUCCESSFULLY ADDED!!\n")
                elif ch==3:
                    wid=int(input("ENTER ID:"))
                    n=input("ENTER NAME:")
                    a=int(input("ENTER AGE:"))
                    ad=input("ENTER ADDRESS:")
                    c=int(input("ENTER CONTACT NO:"))
                    ms=int(input("ENTER MONTHLY SALARY:"))
                    t=(wid,n,a,ad,c,ms)
                    cr.execute("INSERT INTO WORKERS_DETAILS VALUES(%s,%s,%s,%s,%s,%s)",t)
                    mydb.commit()
                    print("\n                    SUCCESSFULLY ADDED!!\n")
                elif ch==4:
                    break
                else:
                    print("\n                    INVALID CHOICE!!\n")
        elif b==3:
            while True:
                print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!! {( DELETE RECORDS )} !!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                         1. DOCTOR DETAILS
                         2. NURSE DETAILS
                         3. OTHER WORKERS
                         4. EXIT\n""")
                ch=int(input("ENTER YOUR CHOICE:"))
                if ch==1:
                    did=int(input("ENTER ID TO DELETE:"))
                    cr.execute("select * from doctor_details where did=%s",(did,))
                    rows=cr.fetchall()
                    if len(rows)!=0:
                        print(rows)
                        c=input("DO YOU WANT TO DELETE THIS RECORD Y/N:")
                        if c.lower()=="y":
                            cr.execute("delete from doctor_details where did=%s",(did,))
                            print("\n                    RECORD DELETED\n")
                        else:
                            print("\n                    NOT DELETED\n")
                    else:
                        print("\n                    NO RECORD PRESENT!!\n")    
                    mydb.commit()
                elif ch==2:
                    nid=int(input("ENTER ID TO DELETE:"))
                    cr.execute("select * from nurse_details where nid=%s",(nid,))
                    rows=cr.fetchall()
                    if len(rows)!=0:
                        print(rows)
                        c=input("DO YOU WANT TO DELETE THIS RECORD Y/N:")
                        if c.lower()=="y":
                            cr.execute("delete from nurse_details where nid=%s",(nid,))
                            print("\n                    RECORD DELETED\n")
                        else:
                            print("\n                    NOT DELETED\n")
                    else:
                        print("\n                    NO RECORD PRESENT!!\n")    
                    mydb.commit()
                elif ch==3:
                    wid=int(input("ENTER ID TO DELETE:"))
                    cr.execute("select * from workers_details where wid=%s",(wid,))
                    rows=cr.fetchall()
                    if len(rows)!=0:
                        print(rows)
                        c=input("DO YOU WANT TO DELETE THIS RECORD Y/N:")
                        if c.lower()=="y":
                            cr.execute("delete from workers_details where wid=%s",(wid,))
                            print("\n                    RECORD DELETED\n")
                        else:
                            print("\n                    NOT DELETED\n")
                    else:
                        print("\n                    NO RECORD PRESENT!!\n")    
                    mydb.commit()
                elif ch==4:
                    break
        elif b==4:
            while True:
                print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!! {( UPDATE RECORDS )} !!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                         1. DOCTOR DETAILS
                         2. NURSE DETAILS
                         3. OTHER WORKERS
                         4. EXIT\n""")
                ch=int(input("ENTER YOUR CHOICE:"))
                if ch==1:
                    did=int(input("ENTER ID TO UPDATE:"))
                    cr.execute("select * from doctor_details where did=%s",(did,))
                    row=cr.fetchall()
                    if len(row)!=0:
                        print(row)
                        o=input("DO YOU WANT UPDATE THIS RECORD Y/N:")
                        if o=="y":
                            n=input("ENTER NAME:")
                            s=input("ENTER SPECIALISATION:")
                            a=int(input("ENTER AGE:"))
                            ad=input("ENTER ADDRESS:")
                            c=int(input("ENTER CONTACT NO:"))
                            f=int(input("ENTER FEES:"))
                            ms=int(input("ENTER MONTHLY SALARY:"))
                            t=(n,s,a,ad,c,f,ms,did)
                            cr.execute("""UPDATE DOCTOR_DETAILS SET NAME=%s,SPECIALISATION=%s,
                                       AGE=%s,ADDRESS=%s,CONTACT=%s,FEES=%s,MONTHLY_SALARY=%s
                                       WHERE DID=%s""",t)
                            mydb.commit()
                            print("\n                    SUCCESSFULLY UPDATED!!\n")
                        else:
                            print("\n                    NOT UPDATED\n")
                    else:
                        print("\n                    RECORD NOT PRESENT\n")
                elif ch==2:
                    nid=int(input("ENTER ID TO UPDATE:"))
                    cr.execute("select * from nurse_details where nid=%s",(nid,))
                    row=cr.fetchall()
                    if len(row)!=0:
                        print(row)
                        o=input("DO YOU WANT UPDATE THIS RECORD Y/N:")
                        if o=="y":
                            n=input("ENTER NAME:")
                            a=int(input("ENTER AGE:"))
                            ad=input("ENTER ADDRESS:")
                            c=int(input("ENTER CONTACT NO:"))
                            ms=int(input("ENTER MONTHLY SALARY:"))
                            t=(n,a,ad,c,ms,nid)
                            cr.execute("""UPDATE NURSE_DETAILS SET NAME=%s,AGE=%s,
                                        ADDRESS=%s,CONTACT=%s,MONTHLY_SALARY=%s
                                        WHERE NID=%s""",t)
                            mydb.commit()
                            print("\n                    SUCCESSFULLY UPDATED!!\n")
                        else:
                            print("\n                    NOT UPDATED\n")
                    else:
                        print("\n                    RECORD NOT PRESENT\n")
                elif ch==3:
                    wid=int(input("ENTER ID TO UPDATE:"))
                    cr.execute("select * from workers_details where wid=%s",(wid,))
                    row=cr.fetchall()
                    if len(row)!=0:
                        print(row)
                        o=input("DO YOU WANT UPDATE THIS RECORD Y/N:")
                        if o=="y":
                            n=input("ENTER NAME:")
                            a=int(input("ENTER AGE:"))
                            ad=input("ENTER ADDRESS:")
                            c=int(input("ENTER CONTACT NO:"))
                            ms=int(input("ENTER MONTHLY SALARY:"))
                            t=(n,a,ad,c,ms,wid)
                            cr.execute("""UPDATE WORKERS_DETAILS SET NAME=%s,AGE=%s,
                                        ADDRESS=%s,CONTACT=%s,MONTHLY_SALARY=%s
                                        WHERE WID=%s""",t)
                            mydb.commit()
                            print("\n                    SUCCESSFULLY UPDATED!!\n")
                        else:
                            print("\n                    NOT UPDATED\n")
                    else:
                        print("\n                    RECORD NOT PRESENT\n")
                elif ch==4:
                    break
                else:
                    print("\n                    INVALID CHOICE!!\n")
        elif b==5:
            break
        else:
            print("\n                    INVALID CHOICE\n")

def patient():
    while True:
        print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!! {( PATIENT )} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================
                    1. SHOW ALL PATIENT DETAILS
                    2. ADD NEW PATIENT
                    3. DISCHARGE PATIENT
                    4. SEARCH PATIENT DETAILS
                    5. EXIT\n""")

        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            cr.execute("select * from patient_details")
            rows=cr.fetchall()
            if len(rows)!=0:
                print("ID\tNAME\tSEX\tage\tADDRESS\t\tCONTACT\t\tDOCTOR\tSTATUS")
                for i in rows:
                    v=list(i)
                    if v[-1].lower()=='n':
                        v[-1]='NOT DISCHARGED'
                    else:
                        v[-1]='DISCHARGED'
                    for j in v:
                        print(j,end="\t")
                    print()
            else:
                print("\n                    NO RECORDS PRESENT\n")
                
        elif ch==2:
            pid=int(input("ENTER ID:"))
            n=input("ENTER NAME:")
            s=input("ENTER SEX:")
            a=int(input("ENTER AGE:"))
            ad=input("ENTER ADDRESS:")
            co=int(input("ENTER CONTACT NO:"))
            dr=input("ENTER DOCTOR RECOMMENDED:")
            t=(pid,n,s,a,ad,co,dr,"n")
            cr.execute("insert into patient_details values(%s,%s,%s,%s,%s,%s,%s,%s)",t)
            mydb.commit()
            print("\n                         REGISTERED SUCCESSFULLY\n")
        elif ch==3:
            pid=int(input("ENTER PATIENT ID TO DISCHARGE:"))
            cr.execute("select * from patient_details where pid=%s and paidbill=%s",(pid,"n"))
            rows=cr.fetchall()
            if len(rows)!=0:
                print(rows)
                c=input("HAS HE/SHE PAID ALL BILLS Y/N:")
                if c.lower()=="y":
                    cr.execute("update patient_details set paidbill=%s where pid=%s",("y",pid))
                    mydb.commit()
                    print("\n                    PATIENT DISCHARGED SUCESSFULLY\n")
                else:
                    print("\n                    PATIENT NOT DISCHARGED\n")
            else:
                print("\n     RECORD DOES NOT EXISTS OR PATIENT HAS BEEN DISCHARGED ALREADY!!\n")

        elif ch==4:
            pid=input("ENTER PATIENT ID:")
            cr.execute("select * from patient_details where pid=%s",(pid,))
            rows=cr.fetchall()
            if len(rows)>0:
                for i in rows:
                    v=list(i)
                    if v[-1].lower()=='n':
                        v[-1]='NOT DISCHARGED'
                    else:
                        v[-1]='DISCHARGED'
                    print("ID\tNAME\tSEX\tage\tADDRESS\t\tCONTACT\t\tDOCTOR\tSTATUS")
                    for j in v:
                        print(j,end="\t")
                    print()
            else:
                print("\n                    RECORD DOES NOT EXISTS!!\n")
        elif ch==5:
            break
        else:
            print("\n                    INVALID CHOICE!!\n")

while True:
    print("""=======================================================================
                        WELCOME TO HOSPITAL
=======================================================================""")
    cr.execute("""create table if not exists patient_details(pid int(10) primary key,
                name varchar(30) not null,sex varchar(10),age int(3),address
                varchar(50),contact varchar(15),doctor_recommended varchar(30),PaidBill CHAR(1))""")
    cr.execute("""create table if not exists doctor_details(did int(10) primary key,
                name varchar(30),specialisation varchar(40),age int(2),address
                varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))""")
    cr.execute("""create table if not exists nurse_details(nid int(10) primary key,
               name varchar(30),age int(2),address varchar(30),contact
               varchar(15),monthly_salary int(10))""")
    cr.execute("""create table if not exists workers_details(wid int(10) primary key,
               name varchar(30),age int(2),address varchar(30),contact varchar(15),
               monthly_salary int(10))""")
    cr.execute("""create table if not exists user_data(username varchar(30) primary key,
               password varchar(30))""")
    while True:
        print("""=======================================================================
                              LOGIN
=======================================================================
                        1: SIGN IN (LOGIN)
                        2: SIGN UP (REGISTER)
                        3: CLOSE THE PROGRAM
                    """)
        r=int(input("ENTER YOUR CHOICE:"))
        if r==3:
            break
        elif r==2:
            registration()
        elif r==1:
            print("""=======================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!!!! {{SIGN IN }} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=======================================================================\n""")

            n=input("ENTER USERNAME:")
            p=input("ENTER PASSWORD:")
            cr.execute("select password from user_data where username=%s",(n,))
            users=cr.fetchall()
            for i in users:
                if i[0]==p:
                    print("\n                        SIGN IN SUCCESSFULL\n")
                    while True:
                        print("""=======================================================================
                             MAIN MENU
=======================================================================
                        1.ADMINISTRATION
                        2.PATIENT (ADMISSION AND DISCHARGE PROCESS)
                        3.SIGN OUT\n""")
                        ch=int(input("ENTER CHOICE:"))
                        if ch==1:
                            administration()
                        elif ch==2:
                            patient()
                        elif ch==3:
                            break
                else:
                        print("\n                    YOU HAVE ENTERED THE WRONG PASSWORD!!\n")
            if len(users)==0:
                print("\n                    USERNAME DOES NOT EXIST!!\n")
    break
print("\n                    THANK YOU FOR USING THE PROGRAM")