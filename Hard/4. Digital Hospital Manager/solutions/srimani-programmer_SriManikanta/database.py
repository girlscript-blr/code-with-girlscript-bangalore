import sqlite3
from random import randint

def registerPatient(name, phone, emergency, age, gender, blood, weight, height, symptoms, medicalComments, hname):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS patients
              ( patient_id TEXT PRIMARY KEY NOT NULL, 
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
                hospital_name TEXT NOT NULL,
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
            hospital_name,
            date_of_admission,
            date_of_discharge,
            discharge_comments,
            time_of_death) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, date('now'), 'NA', 'NA', 'NA')
            ''', 
            (patient_id, name, phone, emergency, age, gender, blood, weight, height, symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6], symptoms[7], symptoms[8], symptoms[9], medicalComments, hname))
            # Getting Total Number of Berths
            total_capacity = cursor.execute('SELECT hospital_capacity FROM hospital WHERE hospital_name=?', (hname, )).fetchone()
            total_capacity = int(total_capacity[0])
            total_capacity -= 1
            # Updating the Remaining Number of Berths
            cursor.execute('UPDATE hospital SET hospital_capacity=? WHERE hospital_name=?', (total_capacity, hname))
            conn.commit()

def fetchDetails():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        details = cursor.execute('SELECT * FROM patients').fetchall()
        hospital_details = cursor.execute('SELECT hospital_name, hospital_id FROM hospital').fetchall()

        return details, hospital_details

def fetchDetailsById(pid): 
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        details = cursor.execute('SELECT * FROM patients WHERE patient_id=? OR patient_name=?', (pid, pid)).fetchall()
        hospital_details = cursor.execute('SELECT hospital_name, hospital_id FROM hospital').fetchall()
        return details, hospital_details

def updateData(patient_id, medical_comments, discharge_date, discharge_comments, deadDate):
    updationStatus = True
    already_date = 'NA'
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM patients WHERE patient_id=?', (patient_id, )).fetchall()
        if(len(result) >= 1):
            already_date = cursor.execute('SELECT date_of_discharge FROM patients WHERE patient_id=?', (patient_id, )).fetchone()
            already_date = already_date[0]
            cursor.execute('''UPDATE patients SET medical_details=?, date_of_discharge=?,
            discharge_comments=?,
            time_of_death=? 
            WHERE
            patient_id=?
            ''', (medical_comments, discharge_date, discharge_comments, deadDate, patient_id))
            conn.commit()
        else:
            updationStatus = False
    if updationStatus and already_date == 'NA':
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            hospital_name = cursor.execute('SELECT hospital_name FROM patients WHERE patient_id=?', (patient_id, )).fetchone()
            hospital_name = hospital_name[0]
            print(hospital_name)
            capacity = cursor.execute('SELECT hospital_capacity FROM hospital WHERE hospital_name=?', (hospital_name, )).fetchone()
            print(capacity)
            capacity = int(capacity[0])
            capacity += 1
            cursor.execute('UPDATE hospital SET hospital_capacity=? WHERE hospital_name=?', (capacity, hospital_name))
            conn.commit()

    return updationStatus

# Hospital Registration
def register_hospital_data(hname, harea, hcity, hstate, hcountry, hpin, hcapacity):

    with sqlite3.connect('database.db') as conn:
        
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS hospital( 
        hospital_id TEXT PRIMARY KEY NOT NULL,
        hospital_name TEXT NOT NULL,
        hospital_area TEXT NOT NULL,
        hospital_city TEXT NOT NULL,
        hospital_state TEXT NOT NULL,
        hospital_country TEXT NOT NULL,
        hospital_pin INTEGER NOT NULL,
        hospital_capacity INTEGER NOT NULL)''')

        hospital_id = '20' + hname.upper()[0:3] + 'HCSC' + str(randint(1435435, 9845439)) 
        
        cursor.execute('''INSERT INTO hospital
        (hospital_id, hospital_name, hospital_area, hospital_city, hospital_state, hospital_country, hospital_pin, hospital_capacity)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (hospital_id, hname, harea, hcity, hstate, hcountry, hpin, hcapacity))

        conn.commit()
# Fetching the Hospital Results
def fetch_hospital_details():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        data = cursor.execute('SELECT hospital_name, hospital_capacity FROM hospital').fetchall()
        return data

# Fetching the Hospital Details
def fetch_hospital_availability(search_key):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        data = cursor.execute('SELECT * FROM hospital WHERE hospital_name=? OR hospital_area=? OR hospital_city=?', (search_key, search_key, search_key)).fetchall()
        return data

# Hospital Statistics
def get_hospital_statistics(search):

    with sqlite3.connect('database.db') as conn:
        status = True
        cursor = conn.cursor()
        admissions = cursor.execute('''SELECT * FROM patients WHERE hospital_name=? AND date_of_admission=date('now')''', (search, )).fetchall()
        discharge = cursor.execute('''SELECT * FROM patients WHERE hospital_name=? AND date_of_discharge=date('now')''', (search, )).fetchall()
        total_count = cursor.execute('''SELECT * FROM patients WHERE hospital_name=? AND date_of_admission <= date('now') AND date_of_discharge='NA' ''', (search, )).fetchall()
        item = cursor.execute('''SELECT * FROM patients WHERE hospital_name=?''', (search, )).fetchall()
       
        if len(item) == 0:
            status = False

        if len(admissions) == 0:
            admissions = 0
        else:
            admissions = len(admissions)
        
        if len(discharge) == 0:
            discharge = 0
        else:
            discharge = len(discharge)
        
        if(len(total_count) == 0):
            total_count = 0
        else:
            total_count = len(total_count)

        total_number_of_patients = total_count

        return admissions, discharge, total_number_of_patients, status