import React, {useState, useEffect} from 'react';
import HospitalLogo from '../assets/hospital.png';
import bedOccupancy from '../critical_care_occupancy';

export default function Hospital(props) {

    var region = props.region

    var occupied = bedOccupancy[0]["East of England"].slice(-1)[0].Occupied;
    var available = bedOccupancy[0]["East of England"].slice(-1)[0].Unoccupied;

    const bigRegions = ["London", "South East", "East of England", "South West", "Midlands","North East", "North West"];
    const london = ["Greater London"];
    const midlands = ["East Midlands", "West Midlands"]

    if (london.includes(region)) {
        region = "London"
    } else if (midlands.includes(region)) {
        region = "Midlands"
    }

    if (bigRegions.includes(region)) {
        occupied = bedOccupancy[0][region].slice(-1)[0].Occupied;
        available = bedOccupancy[0][region].slice(-1)[0].Unoccupied;
    }
    

    const capacity = Math.round((occupied - available)/occupied*100)


    return (
        <div className="panel">
            <div className="hospital">
                <img src={HospitalLogo} alt=""/>
                <h3>Critical care services in {region} hospitals are running at</h3>
                <h1>{capacity}%</h1>
                <h3>capacity.</h3>
                <p>This means there might not be enough beds for you if you fall ill. </p>
            </div>
        </div>
    )
}
