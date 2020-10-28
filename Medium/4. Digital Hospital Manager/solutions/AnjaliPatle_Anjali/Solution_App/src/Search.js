import React from 'react'
import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'


export default function Search(props) {
    const [searchText,setSearchText]=React.useState("");
    const [data,setData]=React.useState([])

     const searchPatient=()=>{
         let x=searchText.trim()
        const items = props.patientDatabase.filter((data)=>{
            if(searchText == null||searchText=="")
                return null
            else if(data.Name.toLowerCase().includes(searchText.toLowerCase()) || (data.ID==searchText)){
                return data
            }
        })
        setData(items)
    }
    

    return (
        <div>
        { props.patientDatabase.length==0?<h1>No Patients added yet!</h1>:
            <>
                <input type="text" placeholder="Search Patient by ID or Name" value={searchText} onChange={(e)=>setSearchText(e.target.value)} style={{width:'40%',padding:'10px'}}/>
                <Button variant="primary" onClick={searchPatient} style={{padding:'12px'}}>
                    Search
                </Button>
                {data.map((i,index)=>
                <>
                        <Table striped bordered hover>
                            <thead>
                                <tr>
                                <th>Patient Details</th>
                                <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th>Patient Id</th>
                                    <th>{i.ID}</th>
                                </tr>
                                <tr>
                                    <th>Patient Full Name</th>
                                    <th>{i.Name}</th>
                                </tr>
                                <tr>
                                    <th>Phone Number</th>
                                    <th>{i.Phone}</th>
                                </tr>
                                <tr>
                                    <th>Emergency Contact Number</th>
                                    <th>{i.EmgPhone}</th>
                                </tr>
                                <tr>
                                    <th>Age</th>
                                    <th>{i.Age}</th>
                                </tr>
                                <tr>
                                    <th>Gender</th>
                                    <th>{i.Gender}</th>
                                </tr>
                                <tr>
                                    <th>Blood Type</th>
                                    <th>{i.Blood}</th>
                                </tr>
                                <tr>
                                    <th>Weight</th>
                                    <th>{i.Weight}</th>
                                </tr>
                                <tr>
                                    <th>Height</th>
                                    <th>{i.Height}</th>
                                </tr>
                                <tr>
                                    <th>Symptoms</th>
                                    <th>{Object.keys(i.Symptoms).map((item,ind)=>
                                                 i.Symptoms[item]=="Yes"?
                                                                            <div key={ind}>{item}, </div>
                                                                             :null 
                                                                            )}
                                    </th>
                                </tr>
                                <tr>
                                    <th>Severity</th>
                                    <th>{(i.Age>=46 || (i.Symptoms["Shortness of breath"]=="Yes"||i.Symptoms["Bluish lips or face"]=="Yes"||i.Symptoms["Constant pain or pressure in your chest"]=="Yes"))?
                                            "Emergency"
                                            :"Mild"}
                                    </th>
                                </tr>
                                <tr>
                                    <th>Medical Details</th>
                                    <th>{i.Comment}</th>
                                </tr>
                                <tr>
                                    <th>Date of Admission</th>
                                    <th>{i.AdmissionDate}</th>
                                </tr>
                                <tr>
                                    <th>Date of Discharge</th>
                                    <th>{i.DischargeDate}</th>
                                </tr>
                                <tr>
                                    <th>Discharge Comment</th>
                                    <th>{i.DischargeComment}</th>
                                </tr>
                                <tr>
                                    <th>Death Date and Time</th>
                                    <th>{i.DischargeDate} {i.DeathTime}</th>
                                </tr>
                            </tbody>
                        </Table>
                        <hr/>
                </>
                )}
            </>
        }
        </div>
    )
}
