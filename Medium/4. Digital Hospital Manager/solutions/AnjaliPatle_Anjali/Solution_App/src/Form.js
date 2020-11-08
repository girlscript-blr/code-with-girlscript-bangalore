import React from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

let symptomObject={
              "Fever":"No",
              "Headache":"No",
              "Fatigue, weakness":"No",
              "Stuffy/runny nose":"No",
              "Sneezing":"No",
              "Sore Throat":"No",
              "Cough":"No",
              "Shortness of breath":"No",
              "Bluish lips or face":"No",
              "Constant pain or pressure in your chest":"No"}
let InitialValue={
    ID:'',
    Name:'',
    Phone:'',
    EmgPhone:'',
    Age:'',
    Gender:'',
    Blood:'',
    Weight:'',
    Height:'',
    Symptoms:{
              "Fever":"No",
              "Headache":"No",
              "Fatigue, weakness":"No",
              "Stuffy/runny nose":"No",
              "Sneezing":"No",
              "Sore Throat":"No",
              "Cough":"No",
              "Shortness of breath":"No",
              "Bluish lips or face":"No",
              "Constant pain or pressure in your chest":"No"},
    Severity:'',
    Comment:'',
    AdmissionDate:'',
    DischargeComment:'',
    DischargeDate:'',
    DeathTime:'',
    DeathDate:''
}
export default function AddForm(props) {
    InitialValue.AdmissionDate=props.currDate;
    const [patientData,setPatientData]=React.useState(InitialValue);
    const [patientDB,setPatientDB]=React.useState([]);
    const [disableSubmit,setDisableSubmit]=React.useState(true)
    
    const SymptomsList=["Fever","Headache","Fatigue, weakness","Stuffy/runny nose","Sneezing","Sore Throat","Cough","Shortness of breath","Bluish lips or face","Constant pain or pressure in your chest"]
    
    React.useEffect(() => {
        setPatientData({...patientData,ID:props.patientDatabase.length+1})
    }, [patientDB])

    React.useEffect(() => {
        if(patientData.Name!=""&&patientData.Age!=""&&patientData.Phone!=""&&patientData.Blood!=""&&patientData.Gender!=""&&patientData.EmgPhone!=""&&patientData.Weight!=""&&patientData.Height!="")
        setDisableSubmit(false)
    }, [patientData])

    const editSymptom=(symptom)=>{
        const res={...patientData}
        if(res.Symptoms[symptom]=="No"){
            res.Symptoms[symptom]="Yes"
        }
        else res.Symptoms[symptom]="No"
        console.log("p",res)
        setPatientData(res)
    }
    const addPatient=(e)=>{
        e.preventDefault();
        setPatientDB([...patientDB,patientData]);
        props.sendInfo([...props.patientDatabase,patientData]);
        InitialValue.Symptoms=symptomObject
        setPatientData(InitialValue);
        window.alert("Added Succesfully! View it in the database");
        props.showDB("details")
    }
    return (
        <div>
            <h4>Patient Id: {props.patientDatabase.length+1}</h4>
            <Form>
                    <Form.Label>Full Name</Form.Label>
                    <Form.Control placeholder="Enter Name" required value={patientData.Name} onChange={(event)=>setPatientData({...patientData,Name:event.target.value})} />
                    <Form.Label>Phone Number</Form.Label>
                    <Form.Control value={patientData.Phone} onChange={(event)=>setPatientData({...patientData,Phone:event.target.value})} />
                    <Form.Label>Emergency Contact</Form.Label>
                    <Form.Control value={patientData.EmgPhone} onChange={(event)=>setPatientData({...patientData,EmgPhone:event.target.value})} />
                    <Form.Label>Age</Form.Label>
                    <Form.Control type="number" value={patientData.Age} onChange={(event)=>setPatientData({...patientData,Age:event.target.value})} />
                    <Form.Label>Select Gender</Form.Label>
                        <Form.Control as="select" value={patientData.Gender} onChange={(event)=>setPatientData({...patientData,Gender:event.target.value})} >
                        <option></option>
                        <option>Male</option>
                        <option>Female</option>
                        <option>Other</option>
                        </Form.Control>
                    <Form.Label>Select Blood Type</Form.Label>
                        <Form.Control as="select" value={patientData.Blood} onChange={(event)=>setPatientData({...patientData,Blood:event.target.value})} >
                        <option></option>
                        <option>A+</option>
                        <option>A-</option>
                        <option>B+</option>
                        <option>B-</option>
                        <option>O+</option>
                        <option>O-</option>
                        <option>AB+</option>
                        <option>AB-</option>
                    </Form.Control>
                    <Form.Label>Weight (in Kg)</Form.Label>
                    <Form.Control type="number" value={patientData.Weight} onChange={(event)=>setPatientData({...patientData,Weight:event.target.value})} />
                    
                    <Form.Label>Height(in cm)</Form.Label>
                    <Form.Control type="number" value={patientData.Height} onChange={(event)=>setPatientData({...patientData,Height:event.target.value})} />
                    <Form.Label>Select Symptoms</Form.Label>
                    {
                        SymptomsList.map((item,index)=>
                            <Form.Group>
                                <Form.Check
                                label={item}
                                value={patientData.Symptoms[item]=="Yes"?true:false}
                                onChange={()=>editSymptom(SymptomsList[index])}
                                />
                            </Form.Group>
                        )
                    }
                    <Form.Group controlId="exampleForm.ControlTextarea1">
                        <Form.Label>Comments/ Medical Details</Form.Label>
                        <Form.Control as="textarea" rows={3} value={patientData.Comment} onChange={(event)=>setPatientData({...patientData,Comment:event.target.value})} />
                    </Form.Group>
                
                <Button variant="primary" type="submit" onClick={(e)=>addPatient(e)} disabled={disableSubmit}>
                    Submit
                </Button>
            </Form>
        </div>
    )
}
