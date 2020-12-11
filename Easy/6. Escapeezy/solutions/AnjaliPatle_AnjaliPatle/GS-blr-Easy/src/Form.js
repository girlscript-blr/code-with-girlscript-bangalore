import React from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


export default function AddForm(props) {

    const [name,setName]=React.useState('')
    const [rows,setRows]=React.useState(0)
    const [cols,setCols]=React.useState(0)
    const [price,setPrice]=React.useState(0)
    const [disableSubmit,setDisableSubmit]=React.useState(true)
    
    
    

    React.useEffect(() => {
        if(name!="" && rows!="" && cols!="" && price!="" && rows>0 && cols>0 && price>0)
        setDisableSubmit(false)
    }, [name,rows,cols,price])

    
    const addEvent=(e)=>{
        e.preventDefault();
        
        props.sendInfo({
            name,
            row:Number(rows),
            col:Number(cols),
            price:Number(price)
        });
        window.alert("Added Succesfully!");
        props.navigate("details")
    }
    return (
        <div>
            <Form>
                    <Form.Label>Event Name</Form.Label>
                    <Form.Control placeholder="Enter Name" required value={name} onChange={(event)=>setName(event.target.value)} />
                    
                    <Form.Label>Number of rows</Form.Label>
                    <Form.Control type="number" value={rows} onChange={(event)=>setRows(event.target.value)} />
                    
                    <Form.Label>Number of Columns</Form.Label>
                    <Form.Control type="number" value={cols} onChange={(event)=>setCols(event.target.value)} />
                    
                    <Form.Label>Price per seat (in Rs.</Form.Label>
                    <Form.Control type="number" value={price} onChange={(event)=>setPrice(event.target.value)} />
                    
                
                <Button variant="primary" type="submit" onClick={(e)=>addEvent(e)} disabled={disableSubmit}>
                    Submit
                </Button>
            </Form>
        </div>
    )
}
