# Digital Hospital Manager - Bonus

> Date : 1st October 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.
- Array filtering.
- Basic calculation.
- Reading and writing data to permanent storage. (files, database, etc) Refer [this](http://www.cplusplus.com/doc/tutorial/files/) for using files in C++.
- Complex user interface for implementing different modes and features.

## Problem Statement

Dr. Stephen Strange is the head of The Medical Association of Belgaum and is responsible to ensure the smooth functioning of the hospitals across the city. During COVID-19 crisis, the number of patients has surged significantly in one of the areas of the Belgaum, which has led to a shortage of isolation beds in that areas’ hospitals. The patients are shifted to hospitals in other areas, but it takes time to check the availability of beds based on the other conditions of the patients (like age, other illnesses, budget for stay, etc.). This in turn creates panic among the patients and their family.

Dr. Strange realised the real reason is the absence of a generalised management system with hospitals following their own different protocols in the city. This leads to delay in updating information of all hospitals and patients in an ordered way at one common space. Taking this as an improvement opportunity, Dr. Strange is looking to get help from you to design an application which can help digitize such healthcare related maintenance issues.

Dr. Strange has laid down a set of requirement for the app keeping in mind three type of end users - **Hospital Admin, Patient and Doctors**. Please refer to the following and quickly start with the implementation before the management of the healthcare system worsens.

### Inputs

1. The app should be able to record the hospitals’ details through Registration Form with following fields as input

   - Hospital Name
   - Address
     - Area
     - City
     - State
     - Country
     - PIN
   - Total Capacity- Number of Beds

2. The app should be able to maintain the medical record of each patient of a hospital with the following details

   - Hospital Name(Select from a list of registered hospitals)
   - Patient Full Name
   - Phone Number
   - Emergency Contact Number
   - Age
   - Gender
   - Blood Type
   - Weight
   - Height
   - Symptoms
     - Fever - Yes/No
     - Headache - Yes/No
     - Fatigue, weakness - Yes/No
     - Stuffy/runny nose - Yes/No
     - Sneezing - Yes/No
     - Sore Throat - Yes/No
     - Cough - Yes/No
     - Shortness of breath- Yes/No
     - Bluish lips or face- Yes/No
     - Constant pain or pressure in your chest - Yes/No
   - Medical Details/comments

3. The app should let the Doctors register themselves with the following details -

- Name
- Qualification
- Specialization
- Experience(in years)

### Operations to be performed on input

#### End User : HOSPITAL ADMIN

1. Depending upon the **symptoms and age**, map the patient to proper severity level as given in table below.

| Symptom                                 | Age Group      | Severity Level |
| --------------------------------------- | -------------- | -------------- |
| Fever                                   | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Headache                                | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Fatigue, weakness                       | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Stuffy/runny nose                       | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Sneezing                                | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Sore Throat                             | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Cough                                   | 0 to 16 years  | Mild           |
|                                         | 16 to 45 years | Mild           |
|                                         | 46 and above   | Emergency      |
| Shortness of breath                     | 0 to 16 years  | Emergency      |
|                                         | 16 to 45 years | Emergency      |
|                                         | 46 and above   | Emergency      |
| Bluish lips or face                     | 0 to 16 years  | Emergency      |
|                                         | 16 to 45 years | Emergency      |
|                                         | 46 and above   | Emergency      |
| Constant pain or pressure in your chest | 0 to 16 years  | Emergency      |
|                                         | 16 to 45 years | Emergency      |
|                                         | 46 and above   | Emergency      |

2. Admin can register/add his/her hospital over the portal.
3. Admin can select his/her hospital from the list of registered hospitals and perform the following operations

   - Admin should be able to add new patients (according to details described in input).
   - Admin should be able to update the patient details when prompted but only the below fields should be
     - Assign a Doctor from list of Doctors registered to the Hospital
     - Medical details/comments
     - Discharge Date
     - Discharge comment- Deceased or Cured (If Deceased, Add date and time of death as well)

4. Admin can get a list of **all** patients in the hospital (Display all patients) as given in the below table

| Hospital ID (Autogenerate) | Patient ID (Autogenerate) | Patient Full Name | Phone Number | Emergency Contact Number | Age | Gender | Blood Type | Weight | Height | Symptoms | \*Severity | Doctor Assigned (Name) | Medical Details | Date of Admission (Autofilled) | Date of Discharge | Discharge comments | Date and Time of Death(If Deceased) |
| -------------------------- | ------------------------- | ----------------- | ------------ | ------------------------ | --- | ------ | ---------- | ------ | ------ | -------- | ---------- | ---------------------- | --------------- | ------------------------------ | ----------------- | ------------------ | ----------------------------------- |
|                            |                           |                   |              |                          |     |        |            |        |        |          |            |                        |                 |                                |                   |                    |                                     |

#### Note

> \*Severity as **Mild or Emergency** need to be fetched from the Symptoms table based on patient symptoms

5. Admin should be able to **Search Patient by ID or Name** as per selected hospital and fetch that one patient’s record in the format shown below

| Inputs                                                                                       | Values |
| -------------------------------------------------------------------------------------------- | ------ |
| Hospital Name                                                                                |        |
| Patient ID                                                                                   |        |
| Patient Full Name                                                                            |        |
| Phone Number                                                                                 |        |
| Emergency Contact Number                                                                     |        |
| Age                                                                                          |        |
| Gender                                                                                       |        |
| Blood Type                                                                                   |        |
| Weight                                                                                       |        |
| Height                                                                                       |        |
| Symptoms                                                                                     |        |
| Severity(Mild or Emergency)- To be fetched from the Symptoms table based on patient symptoms |        |
| Doctor Assigned (Name)                                                                       |        |
| Medical details                                                                              |        |
| Date of admission                                                                            |        |
| Date of discharge                                                                            |        |
| Discharge comments                                                                           |        |
| Date and Time of Death(If Deceased)                                                          |        |

6. The app should be able to calculate, update and display the following statistics -
   - Total patients admitted on the current date
   - Total patients discharged on current date
   - Total number of patients in hospital at the current time

#### End User : PATIENT

1. The patient should be able to fetch **all the hospitals** as per beds available based on the filters `(Filters : Name , Area name , City)` selected in the following format

| Hospital Name | Address(Area, City, State, Country, PIN) | Number of Available Beds |
| ------------- | ---------------------------------------- | ------------------------ |
|               |                                          |                          |

2. If a patient is admitted to a hospital, he/she should be able to fetch personal medical record in the following format by entering his/her **Patient ID**

| Inputs                                                                                       | Values |
| -------------------------------------------------------------------------------------------- | ------ |
| Hospital Name                                                                                |        |
| Patient ID                                                                                   |        |
| Patient Full Name                                                                            |        |
| Phone Number                                                                                 |        |
| Emergency Contact Number                                                                     |        |
| Age                                                                                          |        |
| Gender                                                                                       |        |
| Blood Type                                                                                   |        |
| Weight                                                                                       |        |
| Height                                                                                       |        |
| Symptoms                                                                                     |        |
| Severity(Mild or Emergency)- To be fetched from the Symptoms table based on patient symptoms |        |
| Doctor Assigned (Name)                                                                       |        |
| Medical details                                                                              |        |
| Date of admission                                                                            |        |
| Date of discharge                                                                            |        |
| Discharge comments                                                                           |        |
| Date and Time of Death(If Deceased)                                                          |        |

#### End User : DOCTOR

1. The doctor should be able to register himself/herself with the details described in the Input section.
2. The doctor can choose to serve any number of hospitals among the list of hospitals displayed by the app. Therefore, the app should give an option to the doctor to add the hospital to his associated hospitals’ list.
3. The app should give an option to delete a hospital among the list of associated hospitals.
4. The doctor should be able to view the list of hospitals which he/she is associated with currently in the following format.

| Hospital Name | Address(Area, City, State, Country, PIN) | Number of Patients Assigned |
| ------------- | ---------------------------------------- | --------------------------- |
|               |                                          |                             |

5. The doctor should be able to fetch the records of the patients that are assigned to him/her in the following format

| Hospital ID (Autogenerate) | Patient ID (Autogenerate) | Patient Full Name | Phone Number | Emergency Contact Number | Age | Gender | Blood Type | Weight | Height | Symptoms | Severity | Medical Details | Date of Admission (Autofilled) | Date of Discharge | Discharge comments | Date and Time of Death(If Deceased) |
| -------------------------- | ------------------------- | ----------------- | ------------ | ------------------------ | --- | ------ | ---------- | ------ | ------ | -------- | -------- | --------------- | ------------------------------ | ----------------- | ------------------ | ----------------------------------- |
|                            |                           |                   |              |                          |     |        |            |        |        |          |          |                 |                                |                   |                    |                                     |

### Tables or Files Required

| Serial No. | Table/File Name      | Description                                                                                                                                         |
| ---------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.         | SymptomsDetails      | Above mentioned severity details as per age and symptoms can be stored in a table/file                                                              |
| 2.         | HospitalDetails      | Hospital's details like name, address and number of beds avaliable should be stored in a table/file                                                 |
| 3.         | PatientDetails       | Patient's details need to be added/updated in a table/file to display the list of Patients or an individual Patient detail admitted to the hospital |
| 4.         | DoctorDetails        | Doctor's details like Name, Qualification, Specialization and Experience(in years) should be stored in a table/file                                 |
| 5.         | HospitalDoctorMapper | This table/file to map multiple doctors to multiple hospitals                                                                                       |

> Added here are the minimum required Tables/Files. These are just for your reference. You are free to use more tables/files or columns/fields depending upon the need and the approach you take..

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `31st October 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.
- [RSVP here](https://tinyurl.com/gsblr-hacktoberfest2020) to win\* a limited edition Hacktoberfest 👕Tee-shirt or a 🎍plant.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Easy](../../Easy/4.%20Digital%20Hospital%20Manager%20/README.md)
- [Medium](../../Medium/4.%20Digital%20Hospital%20Manager%20/README.md)
- [Hard](../../Hard/4.%20Digital%20Hospital%20Manager/README.md)
