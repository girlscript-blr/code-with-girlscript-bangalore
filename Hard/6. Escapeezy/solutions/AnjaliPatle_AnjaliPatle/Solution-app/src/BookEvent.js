import React from 'react'
import Card from 'react-bootstrap/Card'
import Event from './Event'

export default function BookEvent(props) {
    const [showList,setShowList]=React.useState(true)
    const [index,setIndex]=React.useState([])

    const renderEvent=(ind)=>{
        setIndex(ind);
        setShowList(false);
    }

    return (
        showList?
        <div style={{display:"flex",flexWrap:"wrap"}}>
            {
                props.event==0?
                    <h1>No events to show</h1>:
                    props.event.map((item,ind)=>
                        <Card style={{ width: '18rem',margin:"50px",border:"2px solid black" }}>
                            <Card.Body>
                                <Card.Title>{item.name}</Card.Title>
                                <div onClick={()=>renderEvent(ind)} style={{border:'1px solid gray',cursor:'pointer',padding:"5px"}}>
                                    Book Tickets
                                </div>
                            </Card.Body>
                        </Card>
                    )
            } 
        </div>:<Event index={index} event={props.event} seats={props.seats} viewOther={setShowList} sendSeatInfo={props.sendSeatInfo} booked={props.booked} sendBooked={props.sendBooked}/>
    )
}
