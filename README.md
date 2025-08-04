# Hospital-Database-System
the Hospital System Database is developed for easily, securely, and quickly managing records about the patients, appointments, doctors, departments, and medication inside the hospital. The database is mainly used by the customer service specialists, receptionists, and nurses for smoothly operating the hospital administration and records. 

# Features

📋 View, add, update, and delete patients, doctors, appointments, treatments, and medications

🔍 View appointments by patient, medications by doctor, and total treatment costs per patient

🗂 Indexing for faster database access on key foreign keys

🧾 Enforces integrity with constraints (e.g., NOT NULL, UNIQUE, CHECK, DEFAULT, FOREIGN KEY)

🖥 Python CLI interface using prettytable for neat tabular display

# Technologies Used

Python

SQLite (file-based database)

PrettyTable for CLI tables

# Installation

Clone the repository

- git clone https://github.com/your-username/hospital-database-system.git

- cd hospital-database-system

Install dependencies

- python -m pip install -U prettytable

# Running the Application

Run Hospital project.py to run the project

# On first run, it will:

- Initialize the database (Hospital.db)

- Create indexes for better performance

# Database instructions and model

All the databases can be accessed by choosing their respective menu options in the main menu. Every
database has an option to view the table values as records. The reason to create the python
interface was to ensure that most of the areas of the database can be easily accessed, and
also because the project itself took much less effort to make without it.

At the beginning, a patient record is either created using INSERT into the patient table or
using the pre-existing records can be used, after which the appointment is created using the
patient’s ID and choosing a doctor from a pre-existing record. Then, after the appointment
is made, the treatment records are created using INSERT into treatment table. The
medication records are created at any time after the patient record.

Almost all values can be edited, except for the department and doctor information, ID
numbers, and names.

Records can also be deleted, by entering ID numbers.

All important queries are marked with comments in their designated function constructors.

![alt text](<Hospital (1).jpg>)