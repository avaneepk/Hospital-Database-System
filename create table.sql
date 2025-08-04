-- PATIENT
CREATE TABLE patient (
    patientID INTEGER PRIMARY KEY,
    patientName Varchar(50) NOT NULL,
    birthdate Varchar(30),
    email Varchar(30) UNIQUE,
    gender Varchar(10) CHECK (gender IN ('M', 'F', 'Other'))
);

-- DOCTOR
CREATE TABLE doctor (
    doctorID INTEGER PRIMARY KEY,
    doctorName Varchar(50) NOT NULL,
    email Varchar(30) UNIQUE
);

-- DEPARTMENT
CREATE TABLE department (
    departmentID INTEGER PRIMARY KEY,
    departmentName Varchar(50) NOT NULL UNIQUE,
    floor INTEGER DEFAULT 1
);

-- N:M: DOCTOR ⇄ DEPARTMENT
CREATE TABLE doctorDepartment (
    doctorID INTEGER,
    departmentID INTEGER,
    PRIMARY KEY (doctorID, departmentID),
    FOREIGN KEY (doctorID) REFERENCES doctor(doctorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (departmentID) REFERENCES department(departmentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- APPOINTMENT
CREATE TABLE appointment (
    appointmentID INTEGER PRIMARY KEY,
    patientID INTEGER,
    doctorID INTEGER,
    appointment_date Varchar(30) NOT NULL,
    status Varchar(30) CHECK (status IN ('scheduled', 'completed', 'cancelled')),
    notes Varchar(30),
    FOREIGN KEY (patientID) REFERENCES patient(patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES doctor(doctorID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- TREATMENT
CREATE TABLE treatment (
    treatmentID INTEGER PRIMARY KEY,
    appointmentID INTEGER,
    treatment_type Varchar(50) NOT NULL,
    cost INTEGER DEFAULT 0,
    description Varchar(100),
    FOREIGN KEY (appointmentID) REFERENCES appointment(appointmentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- MEDICATION
CREATE TABLE medication (
    medicationID INTEGER PRIMARY KEY,
    name Varchar(50) NOT NULL,
    dosage Varchar(30),
    patientID INTEGER,
    doctorID INTEGER,
    FOREIGN KEY (patientID) REFERENCES patient(patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES doctor(doctorID) ON DELETE CASCADE ON UPDATE CASCADE
);



