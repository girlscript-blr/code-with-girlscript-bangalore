import sqlite3
from random import randint

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

def registerPatient(name, phone, emergency, age, gender, blood, weight, height, symptoms, medicalComments):
        with sqlite3.connect('database.db') as conn:
            
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS patients
              ( patient_id TEXT PRIMARY KEY, 
                patient_name TEXT NOT NULL,
                patient_phone TEXT NOT NULL,
                patient_emergency TEXT NOT NULL,
                patient_age INTEGER NOT NULL,
                patient_gender TEXT NOT NULL,
                patient_blood_group TEXT NOT NULL,
                patient_weight REAL NOT NULL,
                patient_height REAL NOT NULL,
                fever TEXT NOT NULL,
                headache TEXT  NOT NULL,
                fatigue TEXT NOT NULL,
                stuffy TEXT NOT NULL,
                sneezing TEXT NOT NULL,
                sore TEXT  NOT NULL,
                cough TEXT NOT NULL,
                breadth TEXT NOT NULL,
                bluish TEXT  NOT NULL,
                chest_pain TEXT NOT NULL,
                medical_details TEXT NOT NULL,
                date_of_admission REAL NOT NULL,
                date_of_discharge TEXT NOT NULL,
                discharge_comments TEXT NOT NULL,
                time_of_death TEXT NOT NULL)''')

            patient_id = 'PTCOVID' + str(randint(1242323343, 9998675688))
            
            cursor.execute('''INSERT INTO patients 
            (patient_id,
            patient_name,
            patient_phone,
            patient_emergency,
            patient_age,
            patient_gender,
            patient_blood_group,
            patient_weight,
            patient_height,
            fever,
            headache,
            fatigue,
            stuffy,
            sneezing,
            sore,
            cough,
            breadth,
            bluish,
            chest_pain,
            medical_details,
            date_of_admission,
            date_of_discharge,
            discharge_comments,
            time_of_death) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, date('now'), 'NA', 'NA', 'NA')
            ''', 
            (patient_id,name, phone, emergency, age, gender, blood, weight, height, symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6], symptoms[7], symptoms[8], symptoms[9], medicalComments))

            conn.commit()

def fetchDetails():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        details = cursor.execute('SELECT * FROM patients').fetchall()
        return details

def fetchDetailsById(pid): 
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        details = cursor.execute('SELECT * FROM patients WHERE patient_id=?', (pid, )).fetchall()
        print(details)
        return details

def updateData(patient_id, medical_comments, discharge_date, discharge_comments, deadDate):
    
    updationStatus = True
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM patients WHERE patient_id=?', (patient_id, )).fetchall()
        if(len(result) >= 1):
            cursor.execute('''UPDATE patients SET medical_details=?, date_of_discharge=?,
            discharge_comments=?,
            time_of_death=? 
            WHERE
            patient_id=?
            ''', (medical_comments, discharge_date, discharge_comments, deadDate, patient_id))
        else:
            updationStatus = False
    return updationStatus

    
    

      

# class App:

#     def __init__(self):
#         print("Method Called")
#         self.conn = sqlite3.connect('database.db')
#         self.cursor = self.conn.cursor()
    
#     def registerPatient(self, name, phone, emergency, age, gender, blood, weight, height, symptoms, medicalComments):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS patients
#         (   patient_id TEXT PRIMARY KEY NOT NULL, 
#             patient_name TEXT NOT NULL,
#             patient_phone TEXT NOT NULL,
#             patient_emergency TEXT NOT NULL,
#             patient_age INTEGER NOT NULL,
#             patient_gender TEXT NOT NULL,
#             patient_blood_group TEXT NOT NULL,
#             patient_weight REAL NOT NULL,
#             patient_height REAL NOT NULL,
#             fever TEXT DEFAULT 'Not Applicable' NOT NULL,
#             headache TEXT DEFAULT 'Not Applicable' NOT NULL,
#             fatigue TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             stuffy TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             sneezing TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             sore TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             cough TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             breadth TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             bluish TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             chest_pain TEXT DEFAULT 'NOT APPLICABLE' NOT NULL,
#             medical_details TEXT NOT NULL,
#             date_of_admission REAL NOT NULL,
#             date_of_discharge REAL DEFAULT date('now') NOT NULL,
#             discharge_comments TEXT DEFAULT 'Not Applicable' NOT NULL,
#             time_of_death TEXT DEFAULT "NA" NOT NULL
#         )''')

#         patient_id = 'PTCOVID' + str(randint(1242323343, 9998675688))
#         self.cursor.execute('''INSERT INTO patients 
#         (patient_id,
#         patient_name,
#         patient_phone,
#         patient_emergency,
#         patient_age,
#         patient_gender,
#         patient_blood_group,
#         patient_weight,
#         patient_height,
#         fever,
#         headache,
#         fatigue,
#         stuffy,
#         sneezing,
#         sore,
#         cough,
#         breadth,
#         bluish,
#         chest_pain,
#         medical_details,
#         date_of_admission) VALUES
#         (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, date('now'))
#         ''', 
#         (patient_id,name, phone, emergency, age, gender, blood, weight, height, symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6], symptoms[7], symptoms[8], symptoms[9], medicalComments))

#         self.conn.commit()

#     def __del__(self):
#         self.cursor.close()
#         self.conn.close()
