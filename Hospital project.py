

'''To make the select query results look structured and presentable, 
one of the Python libraries (PrettyTable) was used, 
and it can easily be installed using the following code 
at least in the windows powershell: ‘ python -m pip install -U prettytable ’
It is quite easy to find the installation instructions online for other operating systems as well.'''

######## Do not touch this ############
import sqlite3
from prettytable import PrettyTable

db = sqlite3.connect('Hospital.db')
cur = db.cursor()
def initializeDB():
    try:
        f = open("sqlcommands.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization") 

######## Main Menu Functions ############
def main():
    initializeDB()
    userInput = -1
    while(userInput != "0"):
        print("\nWelcome to the Hospital Management System")
        print("1: Appointments menu")
        print("2: Patients menu")
        print("3: Doctors menu")
        print("4: medications menu of a patient")
        print("5: Treatments menu")
        print("0: Exit the System")
        userInput = input("What do you want to do?: ")
        print(userInput)
        if userInput == "1":
            appointmentMenu()
        elif userInput == "2":
            patientMenu()
        elif userInput == "3":
            doctorMenu()
        elif userInput == "4":
            medicationMenu()
        elif userInput == "5":
            treatmentMenu()
        elif userInput == "0":
            print("Ending software...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    db.close()       
    return


######## Appointment Menu Functions ############
def appointmentMenu():
    inputUser = -1
    while(inputUser != "0"):
        print("\nAppointment menu")
        print("1: View all appointments")
        print("2: Add a new appointment")
        print("3: Reschedule an appointment")
        print("4: Cancel an appointment")
        print("0: Go back to main menu")
        inputUser = input("What do you want to do?: ")
        print(inputUser)
        if inputUser == "1":
            viewAppointments()
        elif inputUser == "2":
            addAppointment()
        elif inputUser == "3":
            changeAppointment()
        elif inputUser == "4":
            cancelAppointment()
        elif inputUser == "0":
            print("Going back to main menu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
    return

def viewAppointments():
    table = PrettyTable()
    table.field_names = ["Appointment ID","Appointment Date", "Patient Name", "Doctor Name", "Status", "Notes"]
    # SELECT query
    cur.execute("SELECT a.appointmentID, a.appointment_date, p.patientName, d.doctorName, a.status, a.notes FROM appointment a INNER JOIN patient p ON a.patientID = p.patientID INNER JOIN doctor d ON a.doctorID = d.doctorID;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return

def addAppointment():
    try:
        appointmentID = int(input("*Enter appointment ID: "))
    except ValueError:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    if appointmentID <= 0:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    cur.execute("SELECT appointmentID FROM appointment WHERE appointmentID = ?", (appointmentID,))
    if cur.fetchone():
        print("Appointment ID already exists. Please enter a unique ID.")
        return
    patientName = input("*Enter patient's name: ")
    doctorName = input("*Enter doctor's name: ")
    appointment_date = input("*Enter appointment date (YYYY-MM-DD): ")
    if not appointmentID or not patientName or not doctorName or not appointment_date:
        print("All * fields are required.")
        return
    status = input("Enter appointment status ('scheduled', 'completed', or 'cancelled'): ")
    notes = input("Enter any notes for the appointment: ")
    if status not in ['scheduled', 'completed', 'cancelled']:
        print("Invalid status. Please enter 'scheduled', 'completed', or 'cancelled'.")
        return
    if not notes:
        notes = "None"
    cur.execute("SELECT patientID FROM patient WHERE patientName = ?", (patientName,))
    patientID_result = cur.fetchone()
    cur.execute("SELECT doctorID FROM doctor WHERE doctorName = ?", (doctorName,))
    doctorID_result = cur.fetchone()
    
    if not patientID_result:
        print("Patient not found. Please enter a valid patient name.")
        return
    if not doctorID_result:
        print("Doctor not found. Please enter a valid doctor name.")
        return
    
    patientID = patientID_result[0]
    doctorID = doctorID_result[0]
    
    # INSERT query
    cur.execute("INSERT INTO appointment (appointmentID, appointment_date, patientID, doctorID, status, notes) VALUES (?, ?, ?, ?, ?, ?)",
                (appointmentID, appointment_date, patientID, doctorID, status, notes))
    db.commit()
    print("Appointment added successfully.")
    return

def changeAppointment():
    try:
        appointmentID = int(input("*Enter appointment ID: "))
    except ValueError:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    if appointmentID <= 0:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    new_date = input("Enter the new appointment date (YYYY-MM-DD): ")
    if not new_date or not appointmentID:
        print("Appointment date and ID cannot be empty.")
        return
    
    #UPDATE query
    cur.execute("UPDATE appointment SET appointment_date = ? WHERE appointmentID = ?",
                (new_date, appointmentID))
    db.commit()
    print("Appointment rescheduled successfully.")
    return

def cancelAppointment():
    appointmentID = int(input("Enter the appointment ID to cancel: "))
    if not appointmentID or appointmentID <= 0 or type(appointmentID) != int:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    
    # DELETE query
    cur.execute("DELETE FROM appointment WHERE appointmentID = ?", (appointmentID,))
    # Also deleting related treament records 
    cur.execute("DELETE FROM treatment WHERE appointmentID = ?", (appointmentID,)) 
    db.commit()
    print("Appointment cancelled successfully.")
    return



######## Patient Menu Functions ############
def patientMenu():
    inputUser = -1
    while(inputUser != "0"):
        print("\nPatient menu")
        print("1: View all patients")
        print("2: Add a new patient")
        print("3: Update patient information")
        print("4: Delete a patient")
        print("0: Go back to main menu")
        inputUser = input("What do you want to do?: ")
        print(inputUser)
        if inputUser == "1":
            viewPatients()
        elif inputUser == "2":
            addPatient()
        elif inputUser == "3":
            updatePatient()
        elif inputUser == "4":
            deletePatient()
        elif inputUser == "0":
            print("Going back to main menu...")
            break  
        else:
            print("Invalid choice. Please select a valid option.")    
    return

def viewPatients():
    table = PrettyTable()
    table.field_names = ["Patient ID", "Patient Name","Birth Date","Email","Gender"]
    
    # SELECT query
    cur.execute("SELECT p.patientID, p.patientName, p.birthdate, p.email, p.gender FROM patient p;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return

def addPatient():
    try:
        patientID = int(input("*Enter patient ID: "))
    except ValueError:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    if patientID <= 0:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    cur.execute("SELECT patientID FROM patient WHERE patientID = ?", (patientID,))
    if cur.fetchone():
        print("Patient ID already exists. Please enter a unique ID.")
        return
    patientName = input("*Enter patient's name: ")
    if not patientID or not patientName:
        print("Patient ID and name are required.")
        return
    birthdate = input("Enter patient's birth date (YYYY-MM-DD): ")
    email = input("Enter patient's email: ")
    gender = input("Enter patient's gender (M/F/Other): ")
    if not birthdate: 
        birthdate = "NULL"
    if not email:
        email = "NULL"
    if not gender:
        gender = "NULL"

    # INSERT query
    cur.execute("INSERT INTO patient (patientID, patientName, birthdate, email, gender) VALUES (?, ?, ?, ?, ?)",
                (patientID, patientName, birthdate, email, gender))
    db.commit()
    print("Patient added successfully.")
    return

def updatePatient():
    try:
        patientID = int(input("*Enter patient ID: "))
    except ValueError:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    if patientID <= 0:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    if not patientID:
        print("Patient ID cannot be empty.")
        return
    cur.execute("SELECT * FROM patient WHERE patientID = ?", (patientID,))
    row = cur.fetchone()
    print(row)
    print("What do you want to update?")
    print("1: Name \n 2: Birth Date \n 3: Email \n 4: Gender")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        new_name = input("Enter the new name for the patient: ")
        if not new_name:
            print("Entering a value is required.")
            return
        # UPDATE query
        cur.execute("UPDATE patient SET patientName = ? WHERE patientID = ?", (new_name, patientID))
    if choice == "2":
        new_birthdate = input("Enter the new birth date (YYYY-MM-DD): ")
        if not new_birthdate:
            # UPDATE query
            cur.execute("UPDATE patient SET birthdate = NULL WHERE patientID = ?", (patientID,))
            return
        # UPDATE query
        cur.execute("UPDATE patient SET birthdate = ? WHERE patientID = ?", (new_birthdate, patientID))
    if choice == "3":
        new_email = input("Enter the new email: ")
        if not new_email:
            # UPDATE query
            cur.execute("UPDATE patient SET email = NULL WHERE patientID = ?", (patientID,))
            return
        # UPDATE query
        cur.execute("UPDATE patient SET email = ? WHERE patientID = ?", (new_email, patientID))
    if choice == "4":
        new_gender = input("Enter the new gender (M/F/Other): ")
        if not new_gender:
            # UPDATE query
            cur.execute("UPDATE patient SET gender = NULL WHERE patientID = ?", (patientID,))
            return
        # UPDATE query
        cur.execute("UPDATE patient SET gender = ? WHERE patientID = ?", (new_gender, patientID))
    db.commit()
    print("Patient information updated successfully.")
    return

def deletePatient():
    try:
        patientID = int(input("*Enter patient ID: "))
    except ValueError:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    if patientID <= 0:
        print("Invalid patient ID. Please enter a positive integer.")
        return
    if not patientID:
        print("Patient ID cannot be empty.")
        return
    
    # DELETE query for all tables related to patient
    cur.execute("DELETE FROM patient WHERE patientID = ?", (patientID,))
    cur.execute("DELETE FROM treatment WHERE appointmentID IN (SELECT appointmentID FROM appointment WHERE patientID = ?)", (patientID,))  # Also delete related treatments
    cur.execute("DELETE FROM appointment WHERE patientID = ?", (patientID,))  
    cur.execute("DELETE FROM medication WHERE patientID = ?", (patientID,)) 

    db.commit()
    print("Patient deleted successfully.")
    return
    


######## Doctor Menu Functions ############    
def doctorMenu():
    inputUser = -1
    while(inputUser != "0"):
        print("\nDoctor menu")
        print("1: View all doctors")
        print("0: Go back to main menu")
        inputUser = input("What do you want to do?: ")
        print(inputUser)
        if inputUser == "1":
            viewDoctors()
        elif inputUser == "0":
            print("Going back to main menu...")
            break      
    return

def viewDoctors():
    table = PrettyTable()
    table.field_names = ["Doctor ID", "Doctor Name", "Department", "Floor", "Email"]
    
    # SELECT query using INNER JOIN
    cur.execute("SELECT do.doctorID, do.doctorName, de.departmentName, de.floor, do.email FROM doctorDepartment d INNER JOIN doctor do ON d.doctorID = do.doctorID INNER JOIN department de ON d.departmentID = de.departmentID;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return



######## Medication Menu Functions ############
def medicationMenu():
    inputUser = -1
    while(inputUser != "0"):
        print("\nMedication menu")
        print("1: View all medications")
        print("2: Add a new medication")
        print("3: Update medication information")
        print("4: Delete a medication")
        print("0: Go back to main menu")
        inputUser = input("What do you want to do?: ")
        print(inputUser)
        if inputUser == "1":
            viewMedications()
        elif inputUser == "2":
            addMedication()
        elif inputUser == "3":
            updateMedication()
        elif inputUser == "4":
            deleteMedication()
        elif inputUser == "0":
            print("Going back to main menu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")      
    return

def viewMedications():
    table = PrettyTable()
    table.field_names = ["Medication ID", "Medication Name", "Dosage", "Patient Name", "Prescribing Doctor"]
    
    # SELECT query
    cur.execute("SELECT m.medicationID, m.name, m.dosage, p.patientName, d.doctorName FROM medication m INNER JOIN patient p ON m.patientID = p.patientID INNER JOIN doctor d ON m.doctorID = d.doctorID;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return

def addMedication():
    try:
        medicationID = int(input("*Enter medication ID: "))
    except ValueError:
        print("Invalid medication ID. Please enter a positive integer.")
        return
    if medicationID <= 0:
        print("Invalid medication ID. Please enter a positive integer.")
        return
    cur.execute("SELECT medicationID FROM medication WHERE medicationID = ?", (medicationID,))
    if cur.fetchone():
        print("Medication ID already exists. Please enter a unique ID.")
        return
    medicationName = input("*Enter medication name: ")
    dosage = input("Enter dosage: ")
    patientName = input("*Enter patient's name: ")
    doctorName = input("*Enter doctor's name: ")

    if not medicationID or not medicationName or not patientName or not doctorName:
        print("All * marked fields are required.")
        return

    cur.execute("SELECT patientID FROM patient WHERE patientName = ?", (patientName,))
    patientID_result = cur.fetchone()
    cur.execute("SELECT doctorID FROM doctor WHERE doctorName = ?", (doctorName,))
    doctorID_result = cur.fetchone()
    
    if not patientID_result:
        print("Patient not found. Please enter a valid patient name.")
        return
    if not doctorID_result:
        print("Doctor not found. Please enter a valid doctor name.")
        return
    
    patientID = patientID_result[0]
    doctorID = doctorID_result[0]
    
    # INSERT query
    cur.execute("INSERT INTO medication (medicationID, name, dosage, patientID, doctorID) VALUES (?, ?, ?, ?, ?)",
                (medicationID, medicationName, dosage, patientID, doctorID))
    db.commit()
    print("Medication added successfully.")
    return

def updateMedication():
    try:
        medicationID = int(input("*Enter medication ID: "))
    except ValueError:
        print("Invalid medication ID. Please enter a positive integer.")
        return
    if medicationID <= 0:
        print("Invalid medication ID. Please enter a positive integer.")
        return
    
    if not medicationID:
        print("Medication ID cannot be empty.")
        return
    cur.execute("SELECT * FROM medication WHERE medicationID = ?", (medicationID,))
    row = cur.fetchone()
    print(row)
    print("1: Dosage \n 2: Patient's name \n 3: Doctor's name")
    choice = input("What do you want to update?(1-3): ")
    if choice == "1":
        new_dosage = input("Enter the new dosage: ")
        if not new_dosage:
            cur.execute("UPDATE medication SET dosage = NULL WHERE medicationID = ?", (medicationID,))
            return
        cur.execute("UPDATE medication SET dosage = ? WHERE medicationID = ?", (new_dosage, medicationID))
    if choice == "2":
        new_patientName = input("Enter the new patient's name: ")
        if not new_patientName:
            print("Entering a value is required.")
            return
        cur.execute("SELECT patientID FROM patient WHERE patientName = ?", (new_patientName,))
        patientID_result = cur.fetchone()
        if not patientID_result:
            print("Patient not found. Please enter a valid patient name.")
            return
        patientID = patientID_result[0]
        cur.execute("UPDATE medication SET patientID = ? WHERE medicationID = ?", (patientID, medicationID))
    if choice == "3":
        new_doctorName = input("Enter the new doctor's name: ")
        if not new_doctorName:
            print("Entering a value is required.")
            return
        cur.execute("SELECT doctorID FROM doctor WHERE doctorName = ?", (new_doctorName,))
        doctorID_result = cur.fetchone()
        if not doctorID_result:
            print("Doctor not found. Please enter a valid doctor name.")
            return
        doctorID = doctorID_result[0]
        cur.execute("UPDATE medication SET doctorID = ? WHERE medicationID = ?", (doctorID, medicationID))
    else:
        print("Invalid choice. Please select a valid option.")
        return
    db.commit()
    print("Medication information updated successfully.")

def deleteMedication():
    medicationName = input("Enter the medication name to delete: ")
    
    # SELECT query using WHERE clause
    cur.execute("SELECT medicationID FROM medication WHERE name = ?", (medicationName,))
    medicationID_result = cur.fetchone()
    if not medicationID_result:
        print("Medication not found.")
        return
    
    medicationID = medicationID_result[0]
    
    # DELETE query
    cur.execute("DELETE FROM medication WHERE medicationID = ?", (medicationID,))
    db.commit()
    print("Medication deleted successfully.")
    return



######## Treatment Menu Functions ############
def treatmentMenu():
    inputUser = -1
    while(inputUser != "0"):
        print("\nTreatment menu")
        print("1: View patient treatment costs")
        print("2: View all treatments")
        print("3: Add a new treatment")
        print("4: Remove a treatment")
        print("0: Go back to main menu")
        inputUser = input("What do you want to do?: ")
        print(inputUser)
        if inputUser == "1":
            viewTreatmentCost()
        elif inputUser == "2":
            viewTreatments()   
        elif inputUser == "3":
            addTreatment()
        elif inputUser == "4":
            deleteTreatment()
        elif inputUser == "0":
            print("Going back to main menu...")
            break      
        else:
            print("Invalid choice. Please select a valid option.")
    return

def viewTreatmentCost():
    table = PrettyTable()
    table.field_names = ["Patient", "Total Cost"]
    
    # SELECT query using SUM() and INNER JOIN
    cur.execute("SELECT p.patientName, SUM(t.cost) AS total_cost FROM appointment a INNER JOIN patient p ON a.patientID = p.patientID INNER JOIN treatment t ON a.appointmentID = t.appointmentID GROUP BY p.patientID;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return

def viewTreatments():
    table = PrettyTable()
    table.field_names = ["Treatment ID", "Appointment ID", "Treatment Type", "Cost", "Description"]
    
    # SELECT query
    cur.execute("SELECT treatmentID, appointmentID, treatment_type, cost, description FROM treatment;")
    rows = cur.fetchall()
    for row in rows:
        table.add_row(row)
    print(table)
    return

def addTreatment():
    try:
        treatmentID = int(input("*Enter treatment ID: "))
    except ValueError:
        print("Invalid treatment ID. Please enter a positive integer.")
        return
    if treatmentID <= 0:
        print("Invalid treatment ID. Please enter a positive integer.")
        return
    cur.execute("SELECT treatmentID FROM treatment WHERE treatmentID = ?", (treatmentID,))
    if cur.fetchone():
        print("Treatment ID already exists. Please enter a unique ID.")
        return
    try:
        appointmentID = int(input("*Enter appointment ID: "))
    except ValueError:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    if appointmentID <= 0:
        print("Invalid appointment ID. Please enter a positive integer.")
        return
    cur.execute("SELECT appointmentID FROM appointment WHERE appointmentID = ?", (appointmentID,))
    treatment_type = input("*Enter treatment type: ")
    try:
        cost = int(input("Enter treatment cost: "))
    except ValueError:
        print("Invalid treatment cost. Please enter a positive integer.")
        return
    if cost <= 0:
        print("Invalid treatment cost. Please enter a positive integer.")
        return
    description = input("Enter treatment description: ")
    
    if not treatmentID or not appointmentID or not treatment_type:
        print("All * marked fields are required.")
        return
    
    if not cost:
        cost = 0

    if not description:
        description = "NULL"
    
    # INSERT query
    cur.execute("INSERT INTO treatment (treatmentID, appointmentID, treatment_type, cost, description) VALUES (?, ?, ?, ?, ?)",
                (treatmentID, appointmentID, treatment_type, cost, description))
    db.commit()
    print("Treatment added successfully.")
    return

def deleteTreatment():
    try:
        treatmentID = int(input("*Enter treatment ID: "))
    except ValueError:
        print("Invalid treatment ID. Please enter a positive integer.")
        return
    if treatmentID <= 0:
        print("Invalid treatment ID. Please enter a positive integer.")
        return
    if not treatmentID:
        print("Treatment ID cannot be empty.")
        return
    
    # DELETE query
    cur.execute("DELETE FROM treatment WHERE treatmentID = ?", (treatmentID,))
    db.commit()
    print("Treatment deleted successfully.")
    return

main()