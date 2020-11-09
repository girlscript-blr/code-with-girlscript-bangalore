import React from 'react'
import Table from 'react-bootstrap/Table'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Modal from 'react-bootstrap/Modal'

export default function PatientDB(props) {
    const [show, setShow] = React.useState(false);
    const [editIndex,setEditIndex]=React.useState(0);
    const [pDB,setpDB]=React.useState(props.patientDatabase[0])
    const [deathTime,setDeathTime]=React.useState('');
    const [deathDate,setDeathDate]=React.useState('');
    const [comment,setComment]=React.useState('');
    const [dischargeComment,setDischargeComment]=React.useState(props.currDate);
    const [dischargeDate,setDischargeDate]=React.useState('');

    const handleClose = () => {
        if(new Date(pDB.DischargeDate)<new Date(props.currDate)){
            window.alert("Invalid Date. Please choose a date after admission date.")
            return;
        }
        else if(new Date(pDB.DeathDate)>new Date(pDB.DischargeDate)){
            window.alert("Invalid Date. Please choose a date before discharge date.")
            return;
        }
        else if(new Date(pDB.DeathDate)<new Date(props.currDate)){
            window.alert("Invalid Date. Please choose a date after admission date.")
            return;
        }
         const res=[...props.patientDatabase];
         res[editIndex]=pDB
         res[editIndex]=pDB
         props.sendInfo(res)
        setShow(false);
    }
    const openEditBox=(index)=>{
        handleShow();
        setEditIndex(index);
    }
    const handleShow = () => setShow(true);

    React.useEffect(() => {
        setpDB(props.patientDatabase[editIndex])
    }, [editIndex])

    const editDetail=(event)=>{
        const item={...pDB}
        item.Comment=event.target.value
        setpDB(item)
    }
    const editDischarge=(event)=>{
        if(new Date(event.target.value)<new Date(props.currDate)){
            window.alert("Invalid Date. Please choose a date after admission date.")
            return;
        }
        const item={...pDB}
        item.DischargeDate=event.target.value
        setpDB(item)
    }
    const editDischargeComment=(x)=>{
        const item={...pDB}
        item.DischargeComment=x
        if(x=="Cured"){
            item.DeathTime=''
            item.DeathDate=''
        }
        setpDB(item)
    }
    const editDeathTime=(event)=>{
        const item={...pDB}
        item.DeathTime=event.target.value
        setpDB(item)
    }
    const editDeathDate=(event)=>{
        if(new Date(event.target.value)>new Date(pDB.DischargeDate)){
            window.alert("Invalid Date. Please choose a date before discharge date.")
            return;
        }
        else if(new Date(event.target.value)<new Date(props.currDate)){
            window.alert("Invalid Date. Please choose a date after admission date.")
            return;
        }
        
        const item={...pDB}
        item.DeathDate=event.target.value
        setpDB(item)
    }
    return (
        <div>
        { props.patientDatabase.length==0?<h1>No Patients added yet!</h1>:
            <>
                <Table striped bordered hover>
                <thead>
                    <tr>
                    <th>Edit</th>
                    <th>Patient Id</th>
                    <th>Name</th>
                    <th>Phone Number</th>
                    <th>Emergency Contact</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Blood Type</th>
                    <th>Weight</th>
                    <th>Height</th>
                    <th>Symptoms</th>
                    <th>Severity</th>
                    <th>Medical Details</th>
                    <th>Date of Admission</th>
                    <th>Date of Discharge</th>
                    <th>Discharge Comments</th>
                    <th>Date and time of Death(if deceased)</th>
                    </tr>
                </thead>
                <tbody>
                {props.patientDatabase.map((item,index)=>
                    <tr key={index}>
                    <td onClick={()=>openEditBox(index)}>Edit</td>
                    <td>{index+1}</td>
                    <td>{props.patientDatabase[index].Name}</td>
                    <td>{props.patientDatabase[index].Phone}</td>
                    <td>{props.patientDatabase[index].EmgPhone}</td>
                    <td>{props.patientDatabase[index].Age}</td>
                    <td>{props.patientDatabase[index].Gender}</td>
                    <td>{props.patientDatabase[index].Blood}</td>
                    <td>{props.patientDatabase[index].Weight}</td>
                    <td>{props.patientDatabase[index].Height}</td>
                    <td>{Object.keys(props.patientDatabase[index].Symptoms).map((item,ind)=>
                                                 props.patientDatabase[index].Symptoms[item]=="Yes"?
                                                                            <div key={ind}>{item}, </div>
                                                                             :null 
                                                                            )}
                    </td>
                    <td>{(props.patientDatabase[index].Age>=46 || (props.patientDatabase[index].Symptoms["Shortness of breath"]=="Yes"||props.patientDatabase[index].Symptoms["Bluish lips or face"]=="Yes"||props.patientDatabase[index].Symptoms["Constant pain or pressure in your chest"]=="Yes"))?
                            "Emergency"
                            :"Mild"}
                    </td>
                    <td>{props.patientDatabase[index].Comment}</td>
                    <td>{props.patientDatabase[index].AdmissionDate}</td>
                    <td>{props.patientDatabase[index].DischargeDate}</td>
                    <td>{props.patientDatabase[index].DischargeComment}</td>
                    <td>{props.patientDatabase[index].DeathTime}, {props.patientDatabase[index].DeathDate}</td>
                    </tr>
                )
                }   
                </tbody>
                </Table>
                <Modal show={show} onHide={handleClose}>
                    <Modal.Header closeButton>
                    <Modal.Title>Update Patient Details</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Form.Group controlId="exampleForm.ControlTextarea1">
                            <Form.Label>Comments/ Medical Details</Form.Label>
                            <Form.Control as="textarea" rows={3} value={pDB.Comment} onChange={(event)=>editDetail(event)} />
                        </Form.Group>
                        
                        <Form.Label as="legend">
                                   Discharge Date
                                </Form.Label>
                                <input type="date" id="appt" name="appt" value={pDB.DischargeDate} onChange={(event)=>editDischarge(event)}/>
                        <Form.Label as="legend">
                            Discharge Comment
                        </Form.Label>
                            <Form.Check
                            type="radio"
                            label="Deceased"
                            name="formHorizontalRadios"
                            id="formHorizontalRadios1"
                            onChange={()=>editDischargeComment("Deceased")}
                            />
                            <Form.Check
                            type="radio"
                            label="Cured"
                            name="formHorizontalRadios"
                            id="formHorizontalRadios2"
                            onChange={()=>editDischargeComment("Cured")}
                            />
                        {pDB.DischargeComment=="Deceased"?
                            <>
                                <Form.Label as="legend">
                                    Time of death
                                </Form.Label>
                                <input type="time" id="appt" name="appt" value={pDB.DeathTime} onChange={(event)=>editDeathTime(event)}/>
                                <Form.Label as="legend">
                                    Date of death
                                </Form.Label>
                                <input type="date" id="appt" name="appt" value={pDB.DeathDate} onChange={(event)=>editDeathDate(event)}/>
                            </>
                            :null
                        }
                    </Modal.Body>
                    <Modal.Footer>
                    <Button variant="primary" onClick={handleClose}>
                        Close
                    </Button>
                    </Modal.Footer>
                </Modal>
            </>
        }
        </div>
    )
}
