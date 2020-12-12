import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import AddForm from './Form'
import Event from './Event'
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
  const [event,setEvent]=React.useState(0);
  const [seatMatrix,setSeatMatrix]=React.useState([]);
  const [currDate,setCurrDate]=React.useState(yyyy+"-"+mm+"-"+dd);

  React.useEffect(() => {
    const arr=[]
    if(event==0){
      return;
    }
    for(let k=0;k<event.segments.length;k++){
      let segx=[]
      for(let i=0;i<event.segments[k].rows;i++){
        let rowx=[]
        for(let j=0;j<event.segments[k].cols;j++){
          rowx.push(0)
        }
        segx.push(rowx)
      }
      arr.push(segx)
    }
    setSeatMatrix(arr)
  }, [event])
  
  const showComponent=(comp)=>{
    setShowForm(false);
    setShowDetails(false);
    switch (comp){
      case "form":setShowForm(true);
                  break;
      case "details":setShowDetails(true);
                    break;
    }
  }
  return (
    <div>
      <Jumbotron style={{textAlign:'center',height:'200px',paddingTop:'10px'}}>
        <h1>Welcome to Janta Circus!</h1>
        <p>
          Choose the operation you would like to perform.
        </p>
        <p>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("form")}>Create Event Hall (Admin)</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("details")}>Book Tickets (Customer)</Button>
        </p>
    </Jumbotron>
      <div style={{width:'80%',margin:'3% 10%'}}>
        {showForm?<AddForm currDate={currDate} sendInfo={setEvent}  navigate={showComponent}/>:null}
        
      </div>
      {showDetails?<Event event={event} seats={seatMatrix} sendSeatInfo={setSeatMatrix}/>:null}
      {/* {showDetails?<PatientDB currDate={currDate} sendInfo={setPatientDatabase} patientDatabase={patientDatabase}/>:null} */}
   </div>
  );
}

export default App;
