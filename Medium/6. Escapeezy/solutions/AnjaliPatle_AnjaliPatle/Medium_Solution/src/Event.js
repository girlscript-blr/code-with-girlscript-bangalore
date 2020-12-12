import React from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default function Event(props) {
    const [event,setEvent]=React.useState(props.event);
    const [price,setPrice]=React.useState(0);
    const [eventExist,setEventExist]=React.useState(false)

    React.useEffect(() => {
        if(props.event==0){
            setEventExist(false)
        }
        else setEventExist(true)
    }, [])

    const selectSeat=(seg,row,col)=>{
        if(props.seats[seg][row][col]==2){
            return;
        }
        const s=[...props.seats]
        s[seg][row][col]=1-s[seg][row][col];
        props.sendSeatInfo(s)
    }
    
    React.useEffect(() => {
        if(props.seats.length==0){
            return
        }
        let p=0;
        for(let k=0;k<event.segments.length;k++){
            for(let i=0;i<event.segments[k].rows;i++){
                for(let j=0;j<event.segments[k].cols;j++){
                    if(props.seats[k][i][j]==1){
                        p+=event.segments[k].price;
                    }
                }
            }
        }
        setPrice(p)
    }, [props.seats])
    const calculateSeatRow=(segno,n)=>{
        let ans=""
        const alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for(let k=0;k<segno;k++){
            n+=event.segments[k].rows
        }
        let x=Number(n)+1;
        while(x>0){
            if(x%26==0){
                ans+="Z";
                x=Math.floor(x/26) -1;
            }
            else{
                ans+=alph[(x%26)-1];
                x=Math.floor(x/26);
            }
        }
        return ans.split('').reverse().join('') 
    }

    const bookSeats=(e)=>{
        e.preventDefault();
        let n=0;
        let arr=[]
        const s=[...props.seats]
        for(let k=0;k<event.segments.length;k++){
            for(let i=0;i<event.segments[k].rows;i++){
                for(let j=0;j<event.segments[k].cols;j++){
                    if(props.seats[k][i][j]==1){
                        arr.push(calculateSeatRow(k,i)+(j+1));
                    s[k][i][j]=2;
                    n++;
                    }
                }
            }
        }
        if(n==0)
        window.alert("No seats selected. Please select some seats to book.");
        else{
            props.sendSeatInfo(s)
            window.alert("Seat No. "+arr.map((item)=>item)+" CONFIRMED for " + event.name+ " Date: "+event.date+" & Time: "+event.time+" .Price to be Paid: Rs. "+price);
        }
    }

    return (
        eventExist==true?
        <div style={{textAlign:"center"}}>
            <h1 style={{color:"red",border:"1px dashed red",padding:"10px"}}>{event.name}</h1>

            <br/>

            {/* <div>
                <h4>Price per ticket: 
                    {
                        event.segments.map((item,ind)=>
                            <p>Segment {ind+1}: {Number(item.price)}</p>
                        )
                    }
                </h4>
            </div> */}

            <div style={{display:"flex",justifyContent:"center",margin:"40px 0px"}}>
                <div style={{height:"15px",width:"15px",padding:"2px",margin:"5px",borderRadius:"2px",color:"white",background:"#bdab22"}}>
                </div>
                Available Seats
                <div style={{height:"15px",width:"15px",padding:"2px",margin:"5px",marginLeft:"30px",borderRadius:"2px",color:"white",background:"#3a9e10"}}>
                </div>
                Selected Seats
                <div style={{height:"15px",width:"15px",padding:"2px",margin:"5px",marginLeft:"30px",borderRadius:"2px",color:"white",background:"grey"}}>
                </div>
                Unavailable Seats
            </div>

            <div style={{display:"flex",justifyContent:"center",marginTop:"40px",marginBottom:"40px"}}>
            <div>
            {
                props.seats.map((seg,i)=>
                    <div>
                        SEGMENT {i+1} PRICE: {event.segments[i].price}
                        {seg.map((item,index)=>
                            <div>
                                <div style={{display:"flex"}}>
                                    {
                                        item.map((seat,ind)=>
                                            
                                            <div style={{height:"30px",width:"50px",padding:"2px",margin:"5px",borderRadius:"2px",color:"white",cursor:"pointer",background:seat==0?"#bdab22":seat=="2"?"grey":"#3a9e10"}}
                                                onClick={()=>{selectSeat(i,index,ind)}}>
                                                <div style={{fontSize:"12px"}} >{calculateSeatRow(i,index)} {ind+1}</div>
                                            </div>
                                        )
                                        
                                    }
                                </div>
                            </div>
                        )}
                        </div>
                )
            }
            </div>
            </div>
            <h4 style={{margin:"20px 0px 40px 0px",color:"green"}}>Price to be paid: {price}</h4>
            <Button variant="primary" type="submit" style={{marginBottom:"50px"}} onClick={(e)=>bookSeats(e)}>
                    Book Tickets
            </Button>

        </div>
        :<h1>No Event Added!</h1>
    )
}
