from flask import Flask, render_template, request
from database import registerPatient, fetchDetails, fetchDetailsById, updateData, register_hospital_data, fetch_hospital_details, fetch_hospital_availability, get_hospital_statistics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/patientPortal')
def patient_portal():
    return render_template('patientHome.html')

@app.route('/hospitalSearch', methods=["GET", "POST"])
def search_hospital():
    if request.method.lower() == 'post':
        search_key = request.form.get('psearch')
        data = fetch_hospital_availability(search_key)
        if(len(data) >= 1):
            return render_template('hospitalSearch.html', data=data, visibility=True)
        else:
            return render_template('notAvailable.html')
    return render_template('hospitalSearch.html', visibility=False)

# Hospital Statistics
@app.route('/HospitalStatistics', methods=['GET', 'POST'])
def hospital_stats():
    if request.method.lower() == 'post':
        search_key = request.form.get('hospitalSearch')
        admissions, discharge, total, status = get_hospital_statistics(search_key)

        if status:
            return render_template('hospitalStatistics.html', admissions=admissions, discharge=discharge, total=total, visibility=True)
        else:
            return render_template('hospitalNotFound.html')

    return render_template('hospitalStatistics.html', visibility=False)

@app.route('/HospitalRegistration',methods=["GET", "POST"])
def register_hospital():
    if request.method.lower() == 'post':
        name = request.form.get('hname')
        area = request.form.get('harea')
        city = request.form.get('hcity')
        state = request.form.get('hstate')
        country = request.form.get('hcountry')
        pincode = int(request.form.get('hpincode'))
        bed_capacity = int(request.form.get('hbedcapacity'))

        register_hospital_data(name, area, city, state, country, pincode, bed_capacity)

        return render_template('sucesses.html')
    else:
        return render_template('hospitalRegistration.html')


@app.route('/patientAdmitForm', methods=['GET', 'POST'])
def patientForm():

    if request.method.lower() == 'get':
        data = fetch_hospital_details()
        return render_template('patientRegistration.html', data=data)
    elif request.method.lower() == 'post':
        hospital_name = request.form.get('phospitalname')
        patient_name = request.form.get('pname')
        patient_phone = request.form.get('pphone')
        patient_emergency = request.form.get('pemg')
        patient_age = int(request.form.get('page'))
        patient_gender = request.form.get('pgender')
        patient_blood_group = request.form.get('pbloodgroup')
        patient_weight = request.form.get('pweight')
        patient_height = request.form.get('pheight')

        symptoms = list()

        # Fever 
        patient_fever = request.form.get('feverRadio')
        if(patient_age >= 0 and patient_age <= 45 and patient_fever.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_fever.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Fever')

        # Head Ache
        patient_head_ache = request.form.get('headAcheRadio')
        if(patient_age >= 0 and patient_age <= 45 and patient_head_ache.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_head_ache.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Head Ache')

        # Fatigue, Weakness
        patient_fatigue = request.form.get('fatigue')
        patient_head_ache = request.form.get('fatigue')
        if(patient_age >= 0 and patient_age <= 45 and patient_fatigue.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_fatigue.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Fatigue or Weakness')

        # Stuffy or Runny Nose
        patient_stuffy = request.form.get('stuffy')
        if(patient_age >= 0 and patient_age <= 45 and patient_stuffy.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_stuffy.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Stuffy or Runny Nose')

        # Sneezing
        patient_sneezing = request.form.get('sneezing')
        if(patient_age >= 0 and patient_age <= 45 and patient_sneezing.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_sneezing.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Stuffy or Runny Nose')

        # Sore Throat
        patient_sore = request.form.get('sore')
        if(patient_age >= 0 and patient_age <= 45 and patient_sore.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_sore.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Sore')

        # Cough
        patient_cough = request.form.get('cough')
        if(patient_age >= 0 and patient_age <= 45 and patient_cough.lower() == "yes"):
            symptoms.append('Mild')
        elif(patient_age >= 46 and patient_cough.lower() == 'yes'):
            symptoms.append('Emergency')
        else:
            symptoms.append('No Cough')

        # Shortness of Breath
        patient_breath = request.form.get('breath')
        if(patient_age >= 0 and patient_breath.lower() == "yes"):
            symptoms.append("Emergency")
        else:
            symptoms.append('No Shortness of Breath')

        # Bluish Lips 
        patient_blusih = request.form.get('bluish')
        if(patient_age >= 0 and patient_blusih.lower() == "yes"):
            symptoms.append("Emergency")
        else:
            symptoms.append('No Blusih Lips or face')

        # Chest Pain
        patient_chest_pain = request.form.get('chestpain')
        if(patient_age >= 0 and patient_chest_pain.lower() == "yes"):
            symptoms.append("Emergency")
        else:
            symptoms.append('No Chest Pain')

        # Medical Comments
        patient_medical_comments = request.form.get('medicalDetails')

        registerPatient(patient_name, patient_phone, patient_emergency, patient_age, patient_gender, patient_blood_group, patient_weight, patient_height, symptoms, patient_medical_comments, hospital_name)


    return render_template('patientRegistrationSucesses.html')

@app.route('/patientDetails')
def getPatientDetails():
    data, hospital_data = fetchDetails()

    symptomsList = list()
    severityList = list()

    for row in data:
        symptom = list()
        severity = list()

        if('No' not in row[9]):
            symptom.append("Fever")
            severity.append(row[9])
        if('No' not in row[10]):
            symptom.append("Headache")
            severity.append(row[10])
        if('No' not in row[11]):
            symptom.append("Stuffy/runny nose")
            severity.append(row[11])
        if('No' not in row[12]):
            symptom.append("Fatigue, weakness")
            severity.append(row[12])
        if('No' not in row[13]):
            symptom.append("Sneezing")
            severity.append(row[13])
        if('No' not in row[14]):
            symptom.append("Sore Throat")
            severity.append(row[14])
        if('No' not in row[15]):
            symptom.append("Cough")
            severity.append(row[15])
        if('No' not in row[16]):
            symptom.append("Shortness of breath")
            severity.append(row[16])
        if('No' not in row[17]):
            symptom.append("Bluish lips or face")
            severity.append(row[17])
        if('No' not in row[18]):
            symptom.append("Constant pain or pressure in your chest")
            severity.append(row[18])
        
        severityList.append(severity)
        symptomsList.append(symptom)   

    # print(severityList)
    # print(symptomsList)     

    return render_template('allPatients.html', data=data, symptoms=symptomsList, severity=severityList, records=len(data), hospital_data=hospital_data)
# Getting the Patient Data for Patients
@app.route('/PatientData', methods=['GET'])
def fetchPatientsData():
    if request.method.lower() == 'get':
        patientId = request.args['pid']

        data, hospital_data = fetchDetailsById(request.args['pid'])

        if(len(data) <= 0):
            return render_template('recordNotFound.html', recordId=patientId)
        elif(len(data) > 0):
            symptomsList = list()
            severityList = list()

            for row in data:
                symptom = list()
                severity = list()

                if('No' not in row[9]):
                    symptom.append("Fever")
                    severity.append(row[9])
                if('No' not in row[10]):
                    symptom.append("Headache")
                    severity.append(row[10])
                if('No' not in row[11]):
                    symptom.append("Stuffy/runny nose")
                    severity.append(row[11])
                if('No' not in row[12]):
                    symptom.append("Fatigue, weakness")
                    severity.append(row[12])
                if('No' not in row[13]):
                    symptom.append("Sneezing")
                    severity.append(row[13])
                if('No' not in row[14]):
                    symptom.append("Sore Throat")
                    severity.append(row[14])
                if('No' not in row[15]):
                    symptom.append("Cough")
                    severity.append(row[15])
                if('No' not in row[16]):
                    symptom.append("Shortness of breath")
                    severity.append(row[16])
                if('No' not in row[17]):
                    symptom.append("Bluish lips or face")
                    severity.append(row[17])
                if('No' not in row[18]):
                    symptom.append("Constant pain or pressure in your chest")
                    severity.append(row[18])
                
                severityList.append(severity)
                symptomsList.append(symptom)      

            return render_template('patientData.html', data=data, symptoms=symptomsList, severity=severityList, records=len(data))
# Getting Patients Data for admin
@app.route('/PatientData', methods=['GET'])
def fetchPatientDataById():
    if request.method.lower() == 'get':
        patientId = request.args['pid']

        data, hospital_data = fetchDetailsById(request.args['pid'])

        if(len(data) <= 0):
            return render_template('recordNotFound.html', recordId=patientId)
        elif(len(data) > 0):
            symptomsList = list()
            severityList = list()

            for row in data:
                symptom = list()
                severity = list()

                if('No' not in row[9]):
                    symptom.append("Fever")
                    severity.append(row[9])
                if('No' not in row[10]):
                    symptom.append("Headache")
                    severity.append(row[10])
                if('No' not in row[11]):
                    symptom.append("Stuffy/runny nose")
                    severity.append(row[11])
                if('No' not in row[12]):
                    symptom.append("Fatigue, weakness")
                    severity.append(row[12])
                if('No' not in row[13]):
                    symptom.append("Sneezing")
                    severity.append(row[13])
                if('No' not in row[14]):
                    symptom.append("Sore Throat")
                    severity.append(row[14])
                if('No' not in row[15]):
                    symptom.append("Cough")
                    severity.append(row[15])
                if('No' not in row[16]):
                    symptom.append("Shortness of breath")
                    severity.append(row[16])
                if('No' not in row[17]):
                    symptom.append("Bluish lips or face")
                    severity.append(row[17])
                if('No' not in row[18]):
                    symptom.append("Constant pain or pressure in your chest")
                    severity.append(row[18])
                
                severityList.append(severity)
                symptomsList.append(symptom)      

            return render_template('allPatients.html', data=data, symptoms=symptomsList, severity=severityList, records=len(data), hospital_data=hospital_data)

@app.route('/PatientDataUpdation', methods=['GET', 'POST'])
def patientDataUpdation():
    if request.method.lower() == 'post':
        patient_id = request.form.get('patient_id')
        medicalDetails = request.form.get('patient_medical')
        dischargeDate = request.form.get('dischargeDate')
        dischargeComments = None
        discharge_data = request.form.get('recoveryId')
        deadthDate =  request.form.get('deadthDate')
        deadthTime = request.form.get('deadthTime')


        if(discharge_data == 'Yes'):
            dischargeComments = "Dead"
        elif(discharge_data == 'No'):
            dischargeComments = 'Cured'
        
        if not deadthDate:
            deadthDate = "Not Applicable"
        if not deadthTime:
            deadthTime = "Not Applicable"
        else:
            deadthDate = str(deadthDate) + " " + str(deadthTime)

        print(patient_id)
        print(medicalDetails)
        print(dischargeDate)
        print(dischargeComments)
        print(deadthDate)

        if(updateData(patient_id, medicalDetails, dischargeDate, dischargeComments, deadthDate)):
            return render_template('recordUpdationSucesses.html')
        else:
            return render_template('recordNotFound.html', recordId=patient_id)

    return render_template('update.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)