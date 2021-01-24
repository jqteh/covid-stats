import React, {useState, useEffect} from 'react';
import HospitalLogo from '../assets/hospital.png';
import bedOccupancy from '../critical_care_occupancy';

export default function Hospital(props) {

    var occupied = bedOccupancy[0]["East of England"].slice(-1)[0].Occupied;
    var available = bedOccupancy[0]["East of England"].slice(-1)[0].Unoccupied;

    const bigRegions = ["London", "South East", "East of England", "South West", "Midlands","North East", "North West"]

    if (bigRegions.includes(props.region)) {
        occupied = bedOccupancy[0][props.region].slice(-1)[0].Occupied;
        available = bedOccupancy[0][props.region].slice(-1)[0].Unoccupied;
    }
    

    const capacity = Math.round((occupied - available)/occupied*100)


    return (
        <div className="panel">
            <div className="hospital">
                <img src={HospitalLogo} alt=""/>
                <h3>Critical care services in {props.region} hospitals are running at</h3>
                <h1>{capacity}%</h1>
                <h3>capacity.</h3>
                <p>This means there might not be enough beds for you if you fall ill. </p>
                <button onClick={()=>{console.log(bedOccupancy[0])}}>check</button>
            </div>
        </div>
    )
}
