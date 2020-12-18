import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import AddForm from './Form'
import Event from './Event'
import ViewEvent from './ViewEvent'
import BookEvent from './BookEvent'
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
  const [showViewEvent,setShowViewEvent]=React.useState(false);
  const [event,setEvent]=React.useState(0);
  const [seatMatrix,setSeatMatrix]=React.useState([]);
  const [booked,setBooked]=React.useState([])
  const [currDate,setCurrDate]=React.useState(yyyy+"-"+mm+"-"+dd);

  React.useEffect(() => {
    if(event==0){
      return;
    }
    const arr=[...seatMatrix]
      let x=[]
      for(let k=0;k<event[event.length-1].segments.length;k++){
        let segx=[]
        for(let i=0;i<event[event.length-1].segments[k].rows;i++){
          let rowx=[]
          for(let j=0;j<event[event.length-1].segments[k].cols;j++){
            rowx.push(0)
          }
          segx.push(rowx)
        }
        x.push(segx)
      }
      arr.push(x)
    setSeatMatrix(arr)
  }, [event])
  
  const showComponent=(comp)=>{
    setShowForm(false);
    setShowDetails(false);
    setShowViewEvent(false);
    switch (comp){
      case "form":setShowForm(true);
                  break;
      case "details":setShowDetails(true);
                    break;
      case "viewEvent":setShowViewEvent(true);
                    break;
    }
  }
  return (
    <div>
      <Jumbotron style={{textAlign:'center',height:'200px',paddingTop:'10px'}}>
        <h1>Welcome to Escapeezy!</h1>
        <p>
          Choose the operation you would like to perform.
        </p>
        <p>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("form")}>Create Event Hall (Admin)</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("viewEvent")}>Event Statistics</Button>
          <Button variant="primary" style={{margin:'10px'}} onClick={()=>showComponent("details")}>Book Tickets (Customer)</Button>
        </p>
    </Jumbotron>
      <div style={{width:'80%',margin:'3% 10%'}}>
        {showForm?<AddForm currDate={currDate} event={event} booked={booked} sendInfo={setEvent} sendBooked={setBooked} navigate={showComponent}/>:null}
        
      </div>
      {showViewEvent?<ViewEvent eventList={event} booked={booked}/>:null}
      {showDetails?<BookEvent event={event} seats={seatMatrix} sendSeatInfo={setSeatMatrix} booked={booked} sendBooked={setBooked}/>:null}
      {/* {showDetails?<PatientDB currDate={currDate} sendInfo={setPatientDatabase} patientDatabase={patientDatabase}/>:null} */}
   </div>
  );
}

export default App;
