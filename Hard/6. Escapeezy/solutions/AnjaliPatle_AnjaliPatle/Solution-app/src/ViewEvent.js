import React from 'react'
import Card from 'react-bootstrap/Card'
import ListGroup from 'react-bootstrap/ListGroup'
import Button from 'react-bootstrap/Button'

export default function ViewEvent(props) {
    const calculateTotal=(ind)=>{
        let x=0;
        for(let i=0;i<props.booked[ind].length;i++){
            x+=props.booked[ind][i]
        }
        return x
    }
    const calculateTotalPrice=(ind)=>{
        let x=0;
        for(let i=0;i<props.booked[ind].length;i++){
            x+= props.eventList[ind].segments[i].price*props.booked[ind][i]
        }
        return x
    }

    return (
        <div style={{display:"flex",flexWrap:"wrap"}}>
            {props.eventList==0?<h1>No events to show</h1>:
                props.eventList.map((item,index)=>
                    <Card style={{ width: '20rem',margin:"50px" }}>
                        <Card.Header style={{background:"blue",color:"white"}}>{item.name}</Card.Header>
                        <ListGroup variant="flush">
                        {  props.eventList[index].tierName.map((seg,i)=>
                                <ListGroup.Item>
                                    <p>Total seats booked in {props.eventList[index].tierName[i].name}: {props.booked[index][i]}</p>
                                    <p>Total amount collected from {props.eventList[index].tierName[i].name}: {props.booked[index][i] * props.eventList[index].segments[i].price}</p>
                                </ListGroup.Item>
                            )
                        }
                        <ListGroup.Item>
                                <p>Total seats booked: {calculateTotal(index)}</p>
                                <p>Total amount collected: {calculateTotalPrice(index)}</p>
                        </ListGroup.Item>

                        </ListGroup>
                    </Card>
                )
            }
        </div>
    )
}
