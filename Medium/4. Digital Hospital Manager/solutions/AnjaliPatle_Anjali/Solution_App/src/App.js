import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import AddForm from './Form'
import PatientDB from './PatientDB'
import Search from './Search'
import DBDetails from './DBDetails'
import './App.css';

var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1; 
  var yyyy = today.getFullYear();
  if(dd<10) 
  {
    dd='0'+dd;
  } 
  if(mm<10) 
  {
      mm='0'+mm;
  }   
function App() {
  const [showForm,setShowForm]=React.useState(false);
  const [showDetails,setShowDetails]=React.useState(false);
  const [showSearch,setShowSearch]=React.useState(false);
  const [showDB,setShowDB]=React.useState(false);
  const [patientDatabase,setPatientDatabase]=React.useState([]);
  const [currDate,setCurrDate]=React.useState(yyyy+"-"+mm+"-"+dd);

  
  const showComponent=(comp)=>{
    setShowForm(false);
    setShowDetails(false);
    setShowSearch(false);
    setShowDB(false);
    switch (comp){
      case "form":setShowForm(true);
                  break;
      case "details":setShowDetails(true);
                    break;
      case "search":setShowSearch(true);
                    break;
      case "db":setShowDB(true);
                  break;
    }
  }
  return (
    <div>
      <Jumbotron style={{textAlign:'center',height:'200px',paddingTop:'10px'}}>
        <h1>Welcome to Hospital Database!</h1>
        <p>
          Choose the operation you would like to perform.
        </p>
        <p>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("form")}>Add Patient</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("details")}>View/Update Patient Details</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("search")}>Search Patient</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("db")}>View other databse Details</Button>
        </p>
    </Jumbotron>
      <div style={{width:'80%',margin:'3% 10%'}}>
        {showForm?<AddForm currDate={currDate} sendInfo={setPatientDatabase} patientDatabase={patientDatabase} showDB={showComponent}/>:null}
        
        {showSearch?<Search patientDatabase={patientDatabase}/>:null}
        {showDB?<DBDetails currDate={currDate} patientDatabase={patientDatabase}/>:null}
      </div>
      {showDetails?<PatientDB currDate={currDate} sendInfo={setPatientDatabase} patientDatabase={patientDatabase}/>:null}
   </div>
  );
}

export default App;
