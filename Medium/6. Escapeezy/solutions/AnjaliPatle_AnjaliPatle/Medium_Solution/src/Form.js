import React from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


export default function AddForm(props) {

    const [name,setName]=React.useState('')
    const [date,setDate]=React.useState('')
    const [time,setTime]=React.useState('')
    const [noOfTiers,setNoOfTiers]=React.useState(0)
    const [segments,setSegments]=React.useState([{}])
    const [rows,setRows]=React.useState(0)
    const [cols,setCols]=React.useState(0)
    const [price,setPrice]=React.useState(0)
    const [disableSubmit,setDisableSubmit]=React.useState(true)
    
    
    

    React.useEffect(() => {
        let flag=0;
        for(let i=0;i<noOfTiers;i++){
            if(segments[i].rows==0||segments[i].rows==''||segments[i].cols==0||segments[i].cols==''||segments[i].price==0||segments[i].price==''){
                flag=1;
                break;
            }
        }
        if(name!=""&& date!=""&& time!=""&& flag==0 && noOfTiers!=0 )
            setDisableSubmit(false)
    }, [name,date,time,segments])

    React.useEffect(() => {
        let arr=[]
        for(let i=0;i<noOfTiers;i++){
            arr.push({rows:0,cols:0,price:0})
        }
        setSegments(arr)
    }, [noOfTiers])

    const changeSegment=(type,value,ind)=>{
        const seg=[...segments]
        seg[ind][type]=Number(value);
        setSegments(seg)
    }

    const addEvent=(e)=>{
        e.preventDefault();
        
        props.sendInfo({
            name,
            date,
            time,
            segments,
            noOfTiers
        });
        window.alert("Added Succesfully!");
        props.navigate("details")
    }
    
    return (
        <div>
            <Form>
                    <Form.Label>Event Name</Form.Label>
                    <Form.Control placeholder="Enter Name" required value={name} onChange={(event)=>setName(event.target.value)} />
                    <Form.Label>Select Date</Form.Label>
                    <Form.Control type="date" value={date} onChange={(event)=>setDate(event.target.value)} />
                    <Form.Label>Select Time</Form.Label>
                    <Form.Control type="time" value={time} onChange={(event)=>setTime(event.target.value)} />
                    <Form.Label>Enter Number of Seat Allocation Segments</Form.Label>
                    <Form.Control type="number" value={noOfTiers} onChange={(event)=>setNoOfTiers(event.target.value)} />
                    <br/>
                    {
                        segments.map((item,index)=>
                        <>
                            <h2>Enter details for Segment {index+1}</h2>
                            <Form.Label>Number of rows</Form.Label>
                            <Form.Control type="number" value={segments[index]?segments[index].rows:""} onChange={(event)=>changeSegment("rows",event.target.value,index)} />
                            
                            <Form.Label>Number of Columns</Form.Label>
                            <Form.Control type="number" value={segments[index]?segments[index].cols:""} onChange={(event)=>changeSegment("cols",event.target.value,index)} />
                            
                            <Form.Label>Price per seat (in Rs.</Form.Label>
                            <Form.Control type="number" value={segments[index]?segments[index].price:""} onChange={(event)=>changeSegment("price",event.target.value,index)} />
                            
                            <br/>
                        </>
                        )
                    }
                    
                
                <Button variant="primary" type="submit" onClick={(e)=>addEvent(e)} disabled={disableSubmit}>
                    Submit
                </Button>
            </Form>
        </div>
    )
}
