import mysql.connector

#main code begins from here
def beginning():
    user=input("are you a doctor or a patient: ")

    #patient's database table
    if (user=="patient" or user=="Patient"):

        #the main menu for patient
        def hospdb():
                    print("press 1 to add record")
                    print("press 2 to modify record")
                    print("press 3 to display record")
                    print("press 4 to delete record")
                    print("press 5 to either return back or to exit")
                    choice=int(input("enter your choice: "))
                    if (choice==1):
                        adddata()
                    elif (choice==2):
                        modify()
                    elif (choice==3):
                        display()
                    elif (choice==4):
                        delete()
                    elif(choice==5):
                        returnback()
                    else:
                        print("Please enter only integers between 1-5 \n")
                        hospdb()

        #adding data to the doctor's database
        def adddata():
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                try:
                    p_name=input("enter name of the patient: ")
                    id_no=input("create an ID number for the patient: ")
                    cont_no=int(input("enter contact number: "))
                    address=input("enter address: ")
                    proff=input("enter proffesion: ")
                    age=int(input("enter age: "))
                    allergies=input("enter allergies if there are any otherwise write none: ")
                    illness=input("enter illness if there are any otherwise write none: ")
                    disability=input("enter disabilities if there are any otherwise write none: ")
                    ins_name=input("enter the name of the insurance company: ")
                    ins_no=input("enter the contact number of the insurance company: ")
                except ValueError as v:
                    print(v)
                    adddata()

                sqrt= "INSERT INTO patient(patient_Name,ID_no,contact_no,address,proffesion,patient_age,allergies,illness,disability,insurance_company,insurance_comp_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(p_name,id_no,cont_no,address,proff,age,allergies,illness,disability,ins_name,ins_no)
                mycursor.execute(sqrt, (p_name,id_no,cont_no,address,proff,age,allergies,illness,disability,ins_name,ins_no,))
                mydb.commit()
                print("your entry has been added \n")
                
                returnback()

        #modify patient's information
        def modify():
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                mod_record=input("enter the Id number of the record which you want to change: ")
                mod_id=int(input("enter 1 for changing the name, 2 for contact number, 3 for address, 4 for proffesion, 5 fo patient's age, 6 for patient's allergies, 7 for illness, 8 for disabilities, 9 for insurance company's name, 10 for insurance company's number: "))
                mod_val=input("enter the new value: ")
                if (mod_id==1):
                    sqrt="UPDATE patient SET patient_Name = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==2):
                    sqrt="UPDATE patient SET contact_no = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==3):
                    sqrt="UPDATE patient SET address = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==4):
                    sqrt="UPDATE patient SET proffesion = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==5):
                    sqrt="UPDATE patient SET patient_age = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==6):
                    sqrt="UPDATE patient SET allergies = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==7):
                    sqrt="UPDATE patient SET illness = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==8):
                    sqrt="UPDATE patient SET disability = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==9):
                    sqrt="UPDATE patient SET insurance_company = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                elif (mod_id==10):
                    sqrt="UPDATE patient SET insurance_comp_no = %s WHERE ID_no = %s"
                    inp=(mod_val,mod_record)
                    mycursor.execute(sqrt,inp)
                    mydb.commit()
                    print("your record has been updated \n")
                else:
                    print("wrong input. try again\n")
                    modify()

                returnback()

        #displaying info of either the doctor or the patient
        #common function for doctor and patient user
        def display():
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()


                display_var=(input("Do you want the doctor's details or the patient's?: "))

                #displaying doctor's information
                if(display_var=="doctor"):
                        D_id=(input("enter the contact number of the doctor whose records you want to check: "))

                        D_name = "select Doctor_Name from doctor where contact_no = %s"
                        mycursor.execute(D_name,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("name of the doctor: ",i)

                        D_age = "select age from doctor where contact_no = %s"
                        mycursor.execute(D_age,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("age of the doctor: ",i)

                        D_spec = "select speciality from doctor where contact_no = %s"
                        mycursor.execute(D_spec,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("specialist in: ",i)

                        D_j_yrs = "select years_in_service from doctor where contact_no = %s"
                        mycursor.execute(D_j_yrs,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("number of years the doctor has been working since graduation: ",i)

                        D_qual = "select qualification from doctor where contact_no = %s"
                        mycursor.execute(D_qual,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("qualifications of the doctor: ",i)

                        D_inst = "select institute from doctor where contact_no = %s"
                        mycursor.execute(D_inst,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("the institute from where the doctor earned their degree: ",i)

                        D_cont = "select contact_no from doctor where contact_no = %s"
                        mycursor.execute(D_cont,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("contact number of the doctor: ",i)

                        D_email = "select email from doctor where contact_no = %s"
                        mycursor.execute(D_email,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("email of the doctor: ",i)

                        D_work = "select workplace_name from doctor where contact_no = %s"
                        mycursor.execute(D_work,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("hospital or clinic of the doctor: ",i)

                        D_work_no = "select workplace_no from doctor where contact_no = %s"
                        mycursor.execute(D_work_no,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("contact number of the hospital or clinic: ",i)

                        D_work_addr = "select workplace_address from doctor where contact_no = %s"
                        mycursor.execute(D_work_addr,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("address of the hospital or clinic: ",i,"\n")

                        returnback()


                #displaying patient's information
                elif(display_var=="patient"):
                        D_id=(input("enter the ID number of the patient whose records you want to check: "))
                        D_Name = "select patient_Name from patient where ID_no = %s"
                        mycursor.execute(D_Name,(D_id,))
                        myrecords=mycursor.fetchall()
                        for j in myrecords:
                            result= []
                            result.extend(j)
                            for i in result:
                                print("name of the patient: ",i)

                        D_ID_no = "select ID_no from patient where ID_no = %s"
                        mycursor.execute(D_ID_no,(D_id,))
                        myrecords=mycursor.fetchall()
                        for h in myrecords:
                            result= []
                            result.extend(h)
                            for i in result:
                                print("ID number of the patient: ",i)

                        D_cont = "select contact_no from patient where ID_no = %s"
                        mycursor.execute(D_cont,(D_id,))
                        myrecords=mycursor.fetchall()
                        for l in myrecords:
                            result= []
                            result.extend(l)
                            for i in result:
                                print("contact number of the patient: ",i)

                        D_addr = "select address from patient where ID_no = %s"
                        mycursor.execute(D_addr,(D_id,))
                        myrecords=mycursor.fetchall()
                        for k in myrecords:
                            result= []
                            result.extend(k)
                            for i in result:
                                print("address of the patient: ",i)

                        D_prof = "select proffesion from patient where ID_no = %s"
                        mycursor.execute(D_prof,(D_id,))
                        myrecords=mycursor.fetchall()
                        for g in myrecords:
                            result= []
                            result.extend(g)
                            for i in result:
                                print("proffesion of the patient: ",i)

                        D_Age= "select patient_age from patient where ID_no = %s"
                        mycursor.execute(D_Age,(D_id,))
                        myrecords=mycursor.fetchall()
                        for f in myrecords:
                            result= []
                            result.extend(f)
                            for i in result:
                                print("Age of the patient: ",i)

                        D_aller = "select allergies from patient where ID_no = %s"
                        mycursor.execute(D_aller,(D_id,))
                        myrecords=mycursor.fetchall()
                        for d in myrecords:
                            result= []
                            result.extend(d)
                            for i in result:
                                print("allergies of the patient: ",i)

                        D_ill = "select illness from patient where ID_no = %s"
                        mycursor.execute(D_ill,(D_id,))
                        myrecords=mycursor.fetchall()
                        for s in myrecords:
                            result= []
                            result.extend(s)
                            for i in result:
                                print("any other illness of the patient: ",i)

                        D_disa = "select disability from patient where ID_no = %s"
                        mycursor.execute(D_disa,(D_id,))
                        myrecords=mycursor.fetchall()
                        for a in myrecords:
                            result= []
                            result.extend(a)
                            for i in result:
                                print("Disabilities of the patient: ",i)

                        D_ins = "select insurance_company from patient where ID_no = %s"
                        mycursor.execute(D_ins,(D_id,))
                        myrecords=mycursor.fetchall()
                        for p in myrecords:
                            result= []
                            result.extend(p)
                            for i in result:
                                print("name of the insurance company of the patient: ",i)

                        D_ins_no = "select insurance_comp_no from patient where ID_no = %s"
                        mycursor.execute(D_ins_no,(D_id,))
                        myrecords=mycursor.fetchall()
                        for o in myrecords:
                            result= []
                            result.extend(o)
                            for i in result:
                                print("contact number of the insurance company of the patient: ",i,"\n")

                        returnback()

                else:
                    print("only write doctor or patient. try again \n")
                    display()

        #deleting an entry from the patient's database
        def delete():
                import mysql.connector
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                delt=int(input("enter the ID number of the record which you want to remove: "))
                exe="DELETE FROM patient WHERE ID_no = %s"
                mycursor.execute(exe,(delt,))
                mydb.commit()
                print("your record has been deleted \n")
                
                returnback()

                # option to return back to main menu when user is done
                def returnback():
                    try:
                        GO_Back=(input("write back to return to the main menu or else write stop: "))
                        if(GO_Back=="back" or GO_Back=="Back"):
                            hospdb()
                        elif(GO_Back=="stop" or GO_Back=="Stop"):
                            print("thank you for using the hospital database")
                            exit()
                        else:
                            raise Exception

                    except Exception:
                        print("Please write only back or stop \n")
                        returnback()

         # option to return back to main menu when user is done
        def returnback():
                try:
                    GO_Back=(input("write back to return to the main menu or else write stop: "))
                    if(GO_Back=="back" or GO_Back=="Back"):
                        hospdb()
                    elif(GO_Back=="stop" or GO_Back=="Stop"):
                        print("thank you for using the hospital database")
                        exit()
                    else:
                        raise Exception

                except Exception:
                    print("Please write only back or stop \n")
                    returnback()

        hospdb()


    #The doctor's database table
    elif(user=="doctor" or user=="Doctor"):

        #the main menu for doctor
        def hospdb():
                    print("press 1 to add record")
                    print("press 2 to modify record")
                    print("press 3 to display record")
                    print("press 4 to delete record")
                    print("press 5 to either return back or to exit")
                    choice=int(input("enter your choice: "))
                    if (choice==1):
                        adddata()
                    elif (choice==2):
                        modify()
                    elif (choice==3):
                        display()
                    elif (choice==4):
                        delete()
                    elif(choice==5):
                        returnback()
                    else:
                        print("Please enter only integers between 1-5 \n")
                        hospdb()

        #adding data to doctor's database'
        def adddata():
                import mysql.connector
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                d_name=input("enter name of the doctor: ")
                age=input("enter the age of the doctor: ")
                special=input("enter the speciality: ")
                years=int(input("since how many years has the doctor been working: "))
                qual=input("enter the qualifications of the doctor: ")
                inst=input("enter the name of the institute from where the doctor has graduated: ")
                cont_no=int(input("enter contact number: "))
                email=input("enter the email address of the doctor: ")
                work_name=input("enter the name of the hospital or the clinic where the doctor is currently working: ")
                work_no=input("enter the contact number of the hospital or the clinic: ")
                work_address=input("enter the address of the hospital or the clinic: ")

                sqrt= "INSERT INTO doctor(Doctor_Name,age,speciality,years_in_service,qualification,institute,contact_no,email,workplace_name,workplace_no,workplace_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(d_name,age,special,years,qual,inst,cont_no,email,work_name,work_no,work_address)
                mycursor.execute(sqrt, (d_name,age,special,years,qual,inst,cont_no,email,work_name,work_no,work_address,))
                mydb.commit()
                print("your entry has been added \n")

                returnback()

        #modifying the doctor's database info
        def modify():
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                try:
                    mod_record=input("enter the contact number of the record which you want to change: ")
                    mod_id=int(input("enter 1 for changing the name, 2 for age, 3 for speciality, 4 for years_in_service, 5 for qualification, 6 for institute, 7 for email, 8 for workplace_name, 9 for workplace_no, 10 for workplace_address: "))
                    mod_val=input("enter the new value: ")
                    if (mod_id==1):
                        sqrt="UPDATE doctor SET Doctor_Name = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==2):
                        sqrt="UPDATE doctor SET age = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==3):
                        sqrt="UPDATE doctor SET speciality = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==4):
                        sqrt="UPDATE doctor SET years_in_service = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==5):
                        sqrt="UPDATE doctor SET qualification = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==6):
                        sqrt="UPDATE doctor SET institute = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==7):
                        sqrt="UPDATE doctor SET email = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==8):
                        sqrt="UPDATE doctor SET workplace_name = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==9):
                        sqrt="UPDATE doctor SET workplace_no = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    elif (mod_id==10):
                        sqrt="UPDATE doctor SET workplace_address = %s WHERE contact_no = %s"
                        inp=(mod_val,mod_record)
                        mycursor.execute(sqrt,inp)
                        mydb.commit()
                        print("your record has been updated \n")
                    else:
                        raise Exception

                except Exception:
                    print("wrong input \n")
                    modify()

                returnback()

        #displaying info of either the doctor or the patient
        #common function for doctor and patient user
        def display():
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                display_var=(input("Do you want the doctor's details or the patient's?: "))

                #displaying doctor's information
                if(display_var=="doctor"):
                    D_id=(input("enter the contact number of the doctor whose records you want to check: "))

                    D_name = "select Doctor_Name from doctor where contact_no = %s"
                    mycursor.execute(D_name,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("name of the doctor: ",i)

                    D_age = "select age from doctor where contact_no = %s"
                    mycursor.execute(D_age,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("age of the doctor: ",i)

                    D_spec = "select speciality from doctor where contact_no = %s"
                    mycursor.execute(D_spec,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("specialist in: ",i)

                    D_j_yrs = "select years_in_service from doctor where contact_no = %s"
                    mycursor.execute(D_j_yrs,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("number of years the doctor has been working since graduation: ",i)

                    D_qual = "select qualification from doctor where contact_no = %s"
                    mycursor.execute(D_qual,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("qualifications of the doctor: ",i)

                    D_inst = "select institute from doctor where contact_no = %s"
                    mycursor.execute(D_inst,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("the institute from where the doctor earned their degree: ",i)

                    D_cont = "select contact_no from doctor where contact_no = %s"
                    mycursor.execute(D_cont,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("contact number of the doctor: ",i)

                    D_email = "select email from doctor where contact_no = %s"
                    mycursor.execute(D_email,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("email of the doctor: ",i)

                    D_work = "select workplace_name from doctor where contact_no = %s"
                    mycursor.execute(D_work,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("hospital or clinic of the doctor: ",i)

                    D_work_no = "select workplace_no from doctor where contact_no = %s"
                    mycursor.execute(D_work_no,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("contact number of the hospital or clinic: ",i)

                    D_work_addr = "select workplace_address from doctor where contact_no = %s"
                    mycursor.execute(D_work_addr,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("address of the hospital or clinic: ",i,"\n")

                    returnback()


                #displaying patient's information
                elif(display_var=="patient"):
                    D_id=(input("enter the ID number of the patient whose records you want to check: "))
                    D_Name = "select patient_Name from patient where ID_no = %s"
                    mycursor.execute(D_Name,(D_id,))
                    myrecords=mycursor.fetchall()
                    for j in myrecords:
                        result= []
                        result.extend(j)
                        for i in result:
                            print("name of the patient: ",i)

                    D_ID_no = "select ID_no from patient where ID_no = %s"
                    mycursor.execute(D_ID_no,(D_id,))
                    myrecords=mycursor.fetchall()
                    for h in myrecords:
                        result= []
                        result.extend(h)
                        for i in result:
                            print("ID number of the patient: ",i)

                    D_cont = "select contact_no from patient where ID_no = %s"
                    mycursor.execute(D_cont,(D_id,))
                    myrecords=mycursor.fetchall()
                    for l in myrecords:
                        result= []
                        result.extend(l)
                        for i in result:
                            print("contact number of the patient: ",i)

                    D_addr = "select address from patient where ID_no = %s"
                    mycursor.execute(D_addr,(D_id,))
                    myrecords=mycursor.fetchall()
                    for k in myrecords:
                        result= []
                        result.extend(k)
                        for i in result:
                            print("address of the patient: ",i)

                    D_prof = "select proffesion from patient where ID_no = %s"
                    mycursor.execute(D_prof,(D_id,))
                    myrecords=mycursor.fetchall()
                    for g in myrecords:
                        result= []
                        result.extend(g)
                        for i in result:
                            print("proffesion of the patient: ",i)

                    D_Age= "select patient_age from patient where ID_no = %s"
                    mycursor.execute(D_Age,(D_id,))
                    myrecords=mycursor.fetchall()
                    for f in myrecords:
                        result= []
                        result.extend(f)
                        for i in result:
                            print("Age of the patient: ",i)

                    D_aller = "select allergies from patient where ID_no = %s"
                    mycursor.execute(D_aller,(D_id,))
                    myrecords=mycursor.fetchall()
                    for d in myrecords:
                        result= []
                        result.extend(d)
                        for i in result:
                            print("allergies of the patient: ",i)

                    D_ill = "select illness from patient where ID_no = %s"
                    mycursor.execute(D_ill,(D_id,))
                    myrecords=mycursor.fetchall()
                    for s in myrecords:
                        result= []
                        result.extend(s)
                        for i in result:
                            print("any other illness of the patient: ",i)

                    D_disa = "select disability from patient where ID_no = %s"
                    mycursor.execute(D_disa,(D_id,))
                    myrecords=mycursor.fetchall()
                    for a in myrecords:
                        result= []
                        result.extend(a)
                        for i in result:
                            print("Disabilities of the patient: ",i)

                    D_ins = "select insurance_company from patient where ID_no = %s"
                    mycursor.execute(D_ins,(D_id,))
                    myrecords=mycursor.fetchall()
                    for p in myrecords:
                        result= []
                        result.extend(p)
                        for i in result:
                            print("name of the insurance company of the patient: ",i)

                    D_ins_no = "select insurance_comp_no from patient where ID_no = %s"
                    mycursor.execute(D_ins_no,(D_id,))
                    myrecords=mycursor.fetchall()
                    for o in myrecords:
                        result= []
                        result.extend(o)
                        for i in result:
                            print("contact number of the insurance company of the patient: ",i,"\n")

                    returnback()

        #deleting an entry from the doctor's database
        def delete():
                import mysql.connector
                mydb = mysql.connector.connect(host="localhost",user="root",passwd="avaneep",database="hospital")
                mycursor = mydb.cursor()

                delt=int(input("enter the contact number of the record which you want to remove: "))
                exe="DELETE FROM doctor WHERE contact_no = %s"
                mycursor.execute(exe,(delt,))
                mydb.commit()
                print("your record has been deleted. \n")

                returnback()

        # option to return back to main menu when user is done
        def returnback():
                try:
                    GO_Back=(input("write back to return to the main menu or else write stop: "))
                    if(GO_Back=="back" or GO_Back=="Back"):
                        hospdb()
                    elif(GO_Back=="stop" or GO_Back=="Stop"):
                        print("thank you for using the hospital database")
                        exit()
                    else:
                        raise Exception

                except Exception:
                    print("Please write only back or stop \n")
                    returnback()

        #continuing the code from here
        hospdb()

    else:
        print("Please write only doctor or patient \n")
        beginning()

beginning()