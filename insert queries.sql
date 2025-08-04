
-- Values were created using AI --

INSERT INTO patient VALUES (1001, 'Alice Smith', '1990-05-12', 'alice@example.com', 'F'),
(1002, 'Bob Johnson', '1985-09-22', 'bob@example.com', 'M'),
(1003, 'Carol Davis', '1978-11-02', 'carol@example.com', 'F'),
(1004, 'David Lee', '1992-06-18', 'david@example.com', 'M'),
(1005, 'Eva White', '2000-03-25', 'eva@example.com', 'F'),
(1006, 'Frank Black', '1982-12-01', 'frank@example.com', 'M'),
(1007, 'Grace Hill', '1995-07-30', 'grace@example.com', 'F'),
(1008, 'Henry King', '1988-08-15', 'henry@example.com', 'M'),
(1009, 'Isla Green', '1999-02-10', 'isla@example.com', 'F'),
(1010, 'Jake Adams', '1993-04-27', 'jake@example.com', 'M');

INSERT INTO doctor VALUES (4001, 'Dr. Thomas Gray', 'gray@example.com'),
(4002, 'Dr. Linda Blue',  'blue@example.com'),
(4003, 'Dr. Sarah Stone', 'stone@example.com'),
(4004, 'Dr. Mark Wood', 'wood@example.com'),
(4005, 'Dr. Emily Rose', 'rose@example.com'),
(4006, 'Dr. James Silver', 'silver@example.com'),
(4007, 'Dr. Olivia Moon', 'moon@example.com'),
(4008, 'Dr. Robert Snow', 'snow@example.com'),
(4009, 'Dr. Amanda Pearl', 'pearl@example.com'),
(4010, 'Dr. Daniel Brooks', 'brooks@example.com');

INSERT INTO department VALUES (3001, 'Cardiology', 2),
(3002, 'Neurology', 3),
(3003, 'Pediatrics', 1),
(3004, 'Orthopedics', 2),
(3005, 'Dermatology', 4),
(3006, 'Oncology', 5),
(3007, 'Emergency', 1),
(3008, 'Psychiatry', 3),
(3009, 'Radiology', 4),
(3010, 'General Medicine', 1);

INSERT INTO doctorDepartment VALUES (4001, 3001),
(4002, 3002),
(4003, 3003),
(4004, 3004),
(4005, 3005),
(4006, 3006),
(4007, 3007),
(4008, 3008),
(4009, 3009),
(4010, 3010);

INSERT INTO appointment VALUES (7001, 1001, 4001, '2025-08-01', 'scheduled', 'Initial check'),
(7002, 1002, 4002, '2025-08-02', 'completed', 'Follow-up'),
(7003, 1003, 4003, '2025-08-03', 'scheduled', 'Vaccination'),
(7004, 1004, 4004, '2025-08-04', 'cancelled', 'Consultation'),
(7005, 1005, 4005, '2025-08-05', 'scheduled', 'Skin exam'),
(7006, 1006, 4006, '2025-08-06', 'completed', 'Cancer screening'),
(7007, 1007, 4007, '2025-08-07', 'scheduled', 'Emergency'),
(7008, 1008, 4008, '2025-08-08', 'scheduled', 'Therapy'),
(7009, 1009, 4009, '2025-08-09', 'completed', 'Imaging'),
(7010, 1010, 4010, '2025-08-10', 'scheduled', 'Annual checkup');

INSERT INTO treatment VALUES (6001, 7001, 'ECG', 120, 'Heart test'),
(6002, 7002, 'MRI', 300, 'Brain scan'),
(6003, 7003, 'Vaccine', 60, 'Flu shot'),
(6004, 7004, 'X-ray', 100, 'Fracture check'),
(6005, 7005, 'Skin biopsy', 250, 'Sample collection'),
(6006, 7006, 'Chemotherapy', 1000, 'Cancer treatment'),
(6007, 7007, 'Stitches', 150, 'Wound care'),
(6008, 7008, 'Therapy session', 200, 'Counseling'),
(6009, 7009, 'CT Scan', 400, 'Imaging'),
(6010, 7010, 'Blood Test', 80, 'Routine test');

INSERT INTO medication VALUES (5001, 'Aspirin', '100mg', 1001, 4001),
(5002, 'Ibuprofen', '200mg', 1002, 4002),
(5003, 'Paracetamol', '500mg', 1003, 4003),
(5004, 'Amoxicillin', '250mg', 1004, 4004),
(5005, 'Metformin', '500mg', 1005, 4005),
(5006, 'Atorvastatin', '10mg', 1006, 4006),
(5007, 'Lisinopril', '20mg', 1007, 4007),
(5008, 'Sertraline', '50mg', 1008, 4008),
(5009, 'Omeprazole', '20mg', 1009, 4009),
(5010, 'Insulin', '5 units', 1010, 4010);

