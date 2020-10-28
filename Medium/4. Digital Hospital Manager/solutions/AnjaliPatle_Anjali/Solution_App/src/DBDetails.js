import React from 'react'


export default function DBDetails(props) {
    let admit=0,discharge=0,total=0;
    for(let i=0;i<props.patientDatabase.length;i++){
        if(props.patientDatabase[i].AdmissionDate==props.currDate){
            admit++;
            if(props.patientDatabase[i].DischargeDate==""||props.patientDatabase[i].DischargeDate==null)
            total++;
        }
        if(props.patientDatabase[i].DischargeDate==props.currDate){
            discharge++;
        }
    }
    return (
        <div>
            <h1>Total Patients admitted on current date: {admit}</h1>
            <h1>Total Patients discharged on current date: {discharge}</h1>
            <h1>Total number of patients in hospital at the current time: {total}</h1>
        </div>
    )
}
