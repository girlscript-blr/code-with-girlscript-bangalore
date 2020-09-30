# Digital Hospital Manager - Medium

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

He has laid down a set of requirements. Please refer to the following and quickly start with the implementation before the management of the healthcare system worsens.

### Inputs

The app should be able to maintain the medical record of each patient of a hospital with the following details

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

### Operations to be performed on input

1. Depending upon the symptoms and age, map the patient to proper severity level as given in table below.

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

2. The app should be able to add new patients when prompted.
3. The app should be able to update the patient details when prompted but only the below fields should be accessible for updation.
   - Medical details/comments
   - Discharge Date
   - Discharge comment- Deceased or Cured (If Deceased, Add date and time of death as well)
4. The app should be able to fetch one patient’s details by Patient ID or Patient Name

### Output

1. The app should display an option for : **ADD PATIENT** and perform related operations.
2. The app should display an option for : **UPDATE PATIENT** DETAILS and perform related operations.
3. The app should be able to **display all** the patients data, along with the case severity as below-

| Patient ID (Autogenerate) | Patient Full Name | Phone Number | Emergency Contact Number | Age | Gender | Blood Type | Weight | Height | Symptoms | \*Severity | Medical Details | Date of Admission (Autofilled) | Date of Discharge | Discharge comments | Date and Time of Death(If Deceased) |
| ------------------------- | ----------------- | ------------ | ------------------------ | --- | ------ | ---------- | ------ | ------ | -------- | ---------- | --------------- | ------------------------------ | ----------------- | ------------------ | ----------------------------------- |
|                           |                   |              |                          |     |        |            |        |        |          |            |                 |                                |                   |                    |                                     |

#### Note

> \*Severity as **Mild or Emergency** need to be fetched from the Symptoms table based on patient symptoms

4. The app should display an option for Search Patient by ID or Name and the output should be displayed for that patient in the format shown below

| Inputs                                                                                       | Values |
| -------------------------------------------------------------------------------------------- | ------ |
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
| Medical details                                                                              |        |
| Date of admission                                                                            |        |
| Date of discharge                                                                            |        |
| Discharge comments                                                                           |        |
| Date and Time of Death(If Deceased)                                                          |        |

5. The app should be able to calculate, update and display the following statistics -
   - Total patients admitted on the current date
   - Total patients discharged on current date
   - Total number of patients in hospital at the current time

### Tables or Files Required

| Serial No. | Table/File Name | Description                                                                                                                                       |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.         | SymptomsDetails | Above mentioned severity details as per age and symptoms can be stored in a table/file                                                            |
| 2.         | PatientDetails  | Patient details need to be added/updated in a table/file to display the list of Patients or an individual Patient detail admitted to the hospital |

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

- [Easy](../../Easy/4.%20Digital%20Hospital%20Manager/README.md)
- [Hard](../../Hard/4.%20Digital%20Hospital%20Manager/README.md)
- [Bonus](../../Bonus/4.%20Digital%20Hospital%20Manager/README.md)
